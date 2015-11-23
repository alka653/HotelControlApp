from django.contrib.auth.decorators import login_required
from django.shortcuts import render, render_to_response
from django.http import HttpResponseRedirect, HttpResponse
from django.contrib.auth import logout
from django.core.urlresolvers import reverse
from django.contrib.auth.models import User
from django.template import RequestContext
from .models import *
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
		value_sensor = Value.objects.filter(sensor = request.GET['sensor_id'])
		response = list(value_sensor.values('value', 'hour'))
	else:
		return HttpResponse('/')
	return HttpResponse(json.dumps(response), content_type = 'application/json')

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
			val = last_value.hour+1
		except Value.DoesNotExist:
			val = 1
		sensor_value =Value(sensor = sensor, value = value, hour = val)
		sensor_value.save()
		response['response'] = val
	else:
		return HttpResponse('/')
	return HttpResponse(json.dumps(response), content_type = 'application/json')

def logout_user(request):
	logout(request)
	return HttpResponseRedirect('/')
