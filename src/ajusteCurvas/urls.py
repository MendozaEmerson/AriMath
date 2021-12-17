from django.urls import path, include
from . import views

urlpatterns = [
    path('regresionCuadratica/', views.HomeView , name='HomeView')
]