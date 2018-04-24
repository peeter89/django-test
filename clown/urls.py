from django.conf.urls import include, re_path
from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
]
