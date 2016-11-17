from django.conf.urls import patterns, url
from .views import *

urlpatterns = patterns('App.apps.dashboard.views',
	url(r'^$', 'home', name = 'home'),
	url(r'^Logout/$', 'logout_user', name = 'logout_user'),
	url(r'^Room/(?P<space_tag>[-\w]+)/$', 'space', name = 'space'),
	url(r'^Simulator/$', 'simulator', name = 'simulator'),
	url(r'^Sensor/$', 'sensor', name = 'sensor'),
	url(r'^Graphs-month/$', 'graph_month', name = 'graph_month'),
	url(r'^State-space/$', 'state_space', name = 'state_space'),
	url(r'^Sensor-data/$', 'data_sensor', name = 'data_sensor'),
	url(r'^Save-data/$', 'send_data_sensor', name = 'send_data_sensor'),
	url(r'^crear-salon/$', RoomCreateView.as_view(), name='add-room'),
	url(r'^crear-area/(?P<pk>\d+)/$', AreaCreateView.as_view(), name='add-area'),
	url(r'^crear-sensor/(?P<pk>\d+)/$', SensorCreateView.as_view(), name='add-sensor'),
)
