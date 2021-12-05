from django.shortcuts import render
import numpy as np
from sympy import *

def newtonRaphson(f, fderivative, xn, e, N):
    imprimir=['','','']
    resultados=[]
    x = symbols('x')
    step = 1
    flag = 1
    condition = True
    while condition:
        if np.float64(fderivative.evalf(subs={x: xn})) == 0.0:
            imprimir[0]='Error de division entre 0!'
            break
        x0 = xn
        fx0=np.float64(f.evalf(subs={x: xn}))
        xn = xn - np.float64(f.evalf(subs={x: xn})) / \
            np.float64(fderivative.evalf(subs={x: xn}))
        partes=[]
        partes.append(step)
        partes.append('x0 =%0.6f'%x0)
        partes.append('f(x0) = %0.6f'%fx0)
        partes.append('x1 =%0.6f'%xn)
        partes.append('f(x1) = %0.6f'%np.float64(f.evalf(subs={x: xn})))
        resultados.append(partes)
        step += 1
        if step > N:
            flag = 0
            break
        condition = abs(np.float64(f.evalf(subs={x: xn}))) > e
    imprimir[1]=resultados
    if flag == 1:
        imprimir[2]='\nRaiz requerida es: %0.8f' % xn
    else:
        imprimir[2]='\nNo convergente.'
    return imprimir

# Create your views here.
def NewtonView(request):
    if request.method == 'POST':
        x = symbols('x')

        f = parse_expr(request.POST.get("funcion"))
        fderivative = f.diff(x)

        xn = np.float64(request.POST.get("punto"))
        e = np.float64(request.POST.get("error"))
        N = np.float64(request.POST.get("pasos"))
        imprimir = newtonRaphson(f, fderivative, xn, e, N)
        ctx ={
            'error':imprimir[0],
            'iteraciones':imprimir[1],
            'resultado':imprimir[2],
        }
    else:
        ctx = {}
    return render(request, 'ecuacionesNoLineales/Newton-Raphson/newton.html', ctx)
