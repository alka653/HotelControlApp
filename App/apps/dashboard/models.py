# -*- encoding: utf-8 -*-
from django.db import models
from datetime import datetime

class Area(models.Model):
	name = models.CharField(max_length = 50)

	def __str__(self):
		return self.name

	def __unicode__(self):
		return self.name

class Space(models.Model):
	name = models.CharField(max_length = 50)
	area = models.ForeignKey(Area)
	space_tag = models.CharField(max_length = 30, blank = True)

	def __str__(self):
		return self.name

	def __unicode__(self):
		return self.name

class Sensor(models.Model):
	name = models.CharField(max_length = 50)
	space = models.ForeignKey(Space)

	def __str__(self):
		return self.name

class Value(models.Model):
	sensor = models.ForeignKey(Sensor)
	value = models.IntegerField()
	hour = models.IntegerField()
	date = models.DateField(default = datetime.now)

	def __str__(self):
		return str(self.sensor)
