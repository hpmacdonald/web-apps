from django.conf.urls import url
from . import views
                    
urlpatterns = [
    url(r'^$', views.index),
    url(r'^success$', views.success),
    url(r'^register_user$', views.add_user),
    url(r'^login_user$', views.login),
    url(r'^go_to_message$', views.messages),
    url(r'^create_bio$', views.profile),
    url(r'^messages$', views.message_display),
    url(r'^edit_message/(?P<my_val>\d+)$', views.edit),
    url(r'^process_edit/(?P<my_val>\d+)$', views.apply_edit),
    url(r'^logout$', views.logout),
    url(r'^process_delete/(?P<my_val>\d+)$', views.delete),
    url(r'^like_this/(?P<my_val>\d+)$', views.likes),
    url(r'^single_message/(?P<my_val>\d+)$', views.view_message),

]
