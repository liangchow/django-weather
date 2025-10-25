from django.urls import path
from . import views

urlpatterns = [
    path('', views.weather, name='home'),
    path('weather/', views.weather, name='weather'),
]