from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('ajouter/', views.ajouter_vehicule, name='ajouter_vehicule'),
]
