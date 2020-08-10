from django.conf.urls import url
from . import views
                    
urlpatterns = [
    url(r'^$', views.index),
    url(r'^cavegold$', views.cavegold),
    url(r'^housegold$', views.housegold),
    url(r'^farmgold$', views.farmgold),
    url(r'^casinogold$', views.casinogold),
    url(r'^clear$', views.clear),
]