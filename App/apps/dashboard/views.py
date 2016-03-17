from django.http import HttpResponseRedirect, HttpResponse
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, render_to_response
from django.core.urlresolvers import reverse
from django.contrib.auth.models import User
from django.template import RequestContext
from django.contrib.auth import logout
from django.db.models import Avg
from .models import *
import datetime
import json

@login_required
def home(request):
	areas = Area.objects.all()
	spaces = Space.objects.all()
	return render(request, 'principal/home.html', {'title': 'Bienvenido', 'areas': areas, 'spaces': spaces})

@login_required
def space(request, space_tag):
	space = Space.objects.get(space_tag = space_tag)
	sensor = Sensor.objects.filter(space = space)
	return render(request, 'principal/space.html', {'title': space.name, 'space': space, 'sensor': sensor})

def sensor(request):
	response = {}
	if request.is_ajax():
		sensor = Sensor.objects.filter(space = request.GET['space_id'])
		response = list(sensor.values('name', 'pk'))
	else:
		return HttpResponse('/')
	return HttpResponse(json.dumps(response), content_type = 'application/json')

def data_sensor(request):
	response = {}
	if request.is_ajax():
		today = datetime.datetime.now()
		date = today.strftime('%Y-%m-%d')
		value_sensor = Value.objects.filter(sensor = request.GET['sensor_id'], date = date)
		response = list(value_sensor.values('value', 'hour'))
	else:
		return HttpResponse('/')
	return HttpResponse(json.dumps(response), content_type = 'application/json')

@login_required
def simulator(request):
	sensors = Sensor.objects.all()
	return render(request, 'admin/simulator.html', {'title': 'Simualtor', 'sensors': sensors})

def send_data_sensor(request):
	response = {}
	if request.is_ajax():
		value = request.GET['value_sensor']
		sensor_id = request.GET['sensor_id']
		sensor = Sensor.objects.get(pk = sensor_id)
		try:
			last_value = Value.objects.filter(sensor = sensor).latest('hour')
			val = last_value.hour + 1
		except Value.DoesNotExist:
			val = 1
		sensor_value = Value(sensor = sensor, value = value, hour = val)
		sensor_value.save()
		response['response'] = val
	else:
		return HttpResponse('/')
	return HttpResponse(json.dumps(response), content_type = 'application/json')

def state_space(request):
	response = {}
	sen = []
	val = []
	t_val = 0
	total_value = 0
	i = 0
	count = 0
	space_tag = ''
	attr = ''
	today = datetime.datetime.now()
	date = today.strftime('%Y-%m-%d')
	if request.is_ajax():
		space_ = Space.objects.get(pk = request.GET['space'])
		sensors = Sensor.objects.filter(space = space_)
		for sensor in sensors:
			try:
				values = Value.objects.filter(sensor = sensor.pk, date = date).latest('hour')
				val.append(values.value)
				space_tag = str(sensor.space.space_tag)
				sen.append(values.value)
				count = count + 1
			except Value.DoesNotExist:
				val.append(0)
		for v in val:
			t_val += v
			i = i + 1
		if count > 0:
			total_value = t_val / count
			if total_value == 0:
				attr = 'white'
			if total_value > 0:
				attr = 'green'
			if total_value > 80:
				attr = 'yellow'
			if total_value >= 150:
				attr = 'red'
			response['value'] = str(total_value)
			response['space_tag'] = str(space_tag)
			response['id'] = str(attr)
			response['text'] = str('Average value')
		else:
			response['value'] = 'None'
			response['space_tag'] = str(space_.space_tag)
			response['id'] = str('white')
			response['text'] = str('Fail found data sensor')
	else:
		return HttpResponse('/')
	return HttpResponse(json.dumps(response), content_type = 'application/json')


def graph_month(request):
	from datetime import datetime, timedelta
	param = {}
	sensor_count = Sensor.objects.count()
	value = Value.objects.filter(date__gte = datetime.now() - timedelta(days = 30)).aggregate(Avg('value'))
	value_2 = Value.objects.filter(date__gte = datetime.now() - timedelta(days = 2)).aggregate(Avg('value'))
	value_avg =	round((( value['value__avg'] - value_2['value__avg'] ) / value['value__avg'] ) * 100, 2)
	if value_avg < 0:
		param['type'] = 'red'
		param['ord'] = 'asc'
	else:
		param['type'] = 'green'
		param['ord'] = 'desc'
	return render(request, 'principal/graph.html', {'param': param, 'value_avg': abs(value_avg), 'value_last': round(value_2['value__avg'], 2)})

def logout_user(request):
	logout(request)
	return HttpResponseRedirect('/')