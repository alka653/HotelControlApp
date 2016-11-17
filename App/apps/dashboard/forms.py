# -*- encoding: utf-8 -*-
from django.forms import *
from django import forms
from .models import *

class RoomForm(forms.ModelForm):
	class Meta:
		model = Area
		fields = '__all__'
		widgets = {
			'name': TextInput(attrs = {'class': 'form-control', 'maxlength': '45', 'required': True}),
		}
		labels = {
			'name': 'Nombre del salón',
		}

class AreaForm(forms.ModelForm):
	class Meta:
		model = Space
		fields = '__all__'
		exclude = ('area', 'space_tag')
		widgets = {
			'name': TextInput(attrs = {'class': 'form-control', 'maxlength': '45', 'required': True}),
		}
		labels = {
			'name': 'Nombre del área',
		}

class SensorForm(forms.ModelForm):
	class Meta:
		model = Sensor
		fields = '__all__'
		exclude = ('space', )
		widgets = {
			'name': TextInput(attrs = {'class': 'form-control', 'maxlength': '45', 'required': True}),
		}
		labels = {
			'name': 'Nombre del sensor',
		}