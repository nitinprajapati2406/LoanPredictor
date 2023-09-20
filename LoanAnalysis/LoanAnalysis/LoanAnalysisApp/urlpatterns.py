from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.index, name = 'index'),
    path('analyse/', views.analyse, name = 'analyse'),
    path('record/', views.record, name = 'record'),
]