from django.conf.urls import url,include
from django.contrib import admin
from . import views
from django.contrib.auth import views as auth_views
urlpatterns = [

    url(r'^$', views.home, name='home'),
    url(r"^room/(?P<room_id>[0-9]+)/$", views.room_view, name='room_view'),
]
