from django.http import request
from django.shortcuts import render
from . import regresion
import json


def fit(f_type, xvalues, yvalues):
    if f_type == 'cuadratic':
        print(f_type)
    return

# Create your views here.
def HomeView(request):
    if request.method == 'POST':
        xvalues = request.POST.get("xvalues")
        yvalues = request.POST.get("yvalues")
        if xvalues=="" or yvalues=="":
            return render(request, 'ajusteCurvas/ajusteCurvas.html', {})
        xvalues = list(map(float, xvalues.split()))
        yvalues = list(map(float, yvalues.split()))

        yvalues = [x for y, x in sorted(zip(xvalues, yvalues))]
        xvalues.sort()

        xvalues_json = json.dumps(xvalues)
        yvalues_json = json.dumps(yvalues)

        chartX, chartY, a, b, c = regresion.regresionCuadratica(xvalues, yvalues)

        ctx={'resultado':15, 'xvalues':xvalues_json, 'yvalues':yvalues_json, 'xchart': chartX, 'ychart':chartY, 'a':a, 'b':b, 'c':c}
    else:
        ctx = {}
    return render(request, 'ajusteCurvas/ajusteCurvas.html', ctx)