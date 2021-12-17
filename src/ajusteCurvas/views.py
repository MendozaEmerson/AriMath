from django.http import request
from django.shortcuts import render
from . import regresion
import json

def fit(f_type, xvalues, yvalues):
    if f_type == 'cuadratic':
        print(f_type)
    return

# Create your views here.
def RegresionCuadratica(request):
    if request.method == 'POST':
        xvalues = request.POST.get("xvalues")
        yvalues = request.POST.get("yvalues")
        if xvalues=="" or yvalues=="":
            return render(request, 'ajusteCurvas/regresionCuadratica/regresionCuadratica.html', {})
        xvalues = list(map(float, xvalues.split()))
        yvalues = list(map(float, yvalues.split()))

        yvalues = [x for y, x in sorted(zip(xvalues, yvalues))]
        xvalues.sort()

        xvalues_json = json.dumps(xvalues)
        yvalues_json = json.dumps(yvalues)

        chartX, chartY, a, b, c = regresion.regresionCuadratica(xvalues, yvalues)

        ctx={'resultado':'si', 'xvalues':xvalues_json, 'yvalues':yvalues_json, 'xchart': chartX, 'ychart':chartY, 'a':a, 'b':b, 'c':c}
    else:
        ctx = {}
    return render(request, 'ajusteCurvas/regresionCuadratica/regresionCuadratica.html', ctx)

def RegresionLineal(request):
    if request.method == 'POST':
        xvalues = request.POST.get("xvalues")
        yvalues = request.POST.get("yvalues")
        if xvalues=="" or yvalues=="":
            return render(request, 'ajusteCurvas/regresionLineal/regresionLineal.htm', {})
        xvalues = list(map(float, xvalues.split()))
        yvalues = list(map(float, yvalues.split()))

        yvalues = [x for y, x in sorted(zip(xvalues, yvalues))]
        xvalues.sort()

        xvalues_json = json.dumps(xvalues)
        yvalues_json = json.dumps(yvalues)
        # chart x y y son coordenadas paa la recta solo necesito dos coeficientes y usar una funcion de regresion lineal
        chartX, chartY, a, b, c = regresion.regresionLineal(xvalues, yvalues)

        ctx={'resultado':15, 'xvalues':xvalues_json, 'yvalues':yvalues_json, 'xchart': chartX, 'ychart':chartY, 'a':a, 'b':b, 'c':c}
    else:
        ctx = {}
    return render(request, 'ajusteCurvas/regresionLineal/regresionLineal.html', ctx)