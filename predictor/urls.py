from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('predecir/', views.predecir, name='predecir'),
    path('api/guia/reparto/', views.guia_reparto, name='guia_reparto'),
]
