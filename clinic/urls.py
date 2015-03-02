from django.conf.urls import patterns, include, url
from . import views

urlpatterns = patterns('',
    url(r'^$', views.appointment_list),
    url(r'^appointment/(?P<pk>[0-9]+)/$', views.appointment_detail),
    url(r'^appointment/new/$', views.appointment_new, name='appointment_new'),
    url(r'^appointment/(?P<pk>[0-9]+)/edit/$', views.appointment_edit, name='appointment_edit'),
)
