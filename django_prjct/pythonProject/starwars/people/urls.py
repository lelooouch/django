from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.get_people_list, name='people_list'),
    path('character/<int:id>/', views.get_character_data, name='character')
]