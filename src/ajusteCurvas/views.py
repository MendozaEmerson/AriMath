from django.http import request
from django.shortcuts import render
import json

def cuadratic(a, b, c, xVal):
    return a*xVal*xVal + b*xVal + c

def fit(x,y):

    return

# Create your views here.
def HomeView(request):
    if request.method == 'POST':
        numberInputs = int((len(request.POST)-1)/2)
        print(numberInputs)
        xvalues = []
        yvalues = []
        for i in range(numberInputs):
            xi = request.POST.get('x'+str(i))
            xvalues.append(0 if xi=='' else int(xi))
        for i in range(numberInputs):
            yi = request.POST.get('y'+str(i))
            yvalues.append(0 if yi=='' else int(yi))
        a=1
        b=1
        c=1
        #xvalues = [1,2,3,4,5,6,7,8,9]
        #yvalues = [cuadratic(a,b,c,yi) for yi in xvalues]

        xvalues_json = json.dumps(xvalues)
        yvalues_json = json.dumps(yvalues)

        ctx={'resultado':15, 'xvalues':xvalues_json, 'yvalues':yvalues_json}
    else:
        ctx = {}
    return render(request, 'ajusteCurvas/ajusteCurvas.html', ctx)