from django.conf.urls import url
from . import views

                    
urlpatterns = [
    url(r'^$', views.index),
    url(r'^success$', views.success),
    url(r'^register_user$', views.add_user),
    url(r'^login_user$', views.login),
    url(r'^add_new_message$', views.process_message),
    url(r'^comments/(?P<message_id>\d+)$', views.add_comment),
    url(r'^add$', views.adding),
    url(r'^delete/(?P<message_id>\d+)$', views.destroy),
    url(r'^scroll$', views.scroll),


]
