from django.http import request
from django.shortcuts import render

def home(request):
    return render(request, 'home/index.html', {})