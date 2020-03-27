from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index-list'),
    path('add/', views.add, name='add-list'),
]