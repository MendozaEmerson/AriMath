from django.urls import path, include
from . import views

urlpatterns = [
    path('NewtonRaphson', views.NewtonView , name='NewtonView')
]