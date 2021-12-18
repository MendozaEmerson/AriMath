from django.urls import path, include
from . import views

urlpatterns = [
    path('NewtonRaphson', views.NewtonView , name='NewtonView'),
    path('Biseccion', views.BiseccionView , name='BiseccionView'),
    path('', views.homeECN , name='nolineal'),
]