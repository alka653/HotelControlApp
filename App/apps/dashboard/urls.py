from django.conf.urls import patterns, url

urlpatterns = patterns('App.apps.dashboard.views',
	url(r'^$', 'home', name = 'home'),
	url(r'^Logout/$', 'logout_user', name = 'logout_user'),
	url(r'^Room/(?P<space_tag>[-\w]+)/$', 'space', name = 'space'),
	url(r'^Simulator/$', 'simulator', name = 'simulator'),
	url(r'^Sensor/$', 'sensor', name = 'sensor'),
	url(r'^State-space/$', 'state_space', name = 'state_space'),
	url(r'^Sensor-data/$', 'data_sensor', name = 'data_sensor'),
	url(r'^Save-data/$', 'send_data_sensor', name = 'send_data_sensor'),
)
