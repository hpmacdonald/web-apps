from django.conf.urls import url
from . import views
                    
urlpatterns = [
    url(r'^$', views.index),
    url(r'^shows$', views.shows),
    url(r'^new_show$', views.create),
    url(r'^edit/(?P<my_val>\d+)$', views.edit),
    url(r'^show_each/(?P<my_val>\d+)$', views.show_individual),
    url(r'^process_edit/(?P<my_val>\d+)$', views.process_edit),
    url(r'^process_delete/(?P<my_val>\d+)$', views.delete), 
]
