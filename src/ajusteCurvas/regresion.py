from . import gaussElimination


def cuadratic(a, b, c, xVal):
    return a*xVal*xVal + b*xVal + c


def regresionCuadratica(xvalues, yvalues):
    size = len(xvalues)
    
    #Lado izquierdo
    sumX = sum(xvalues)
    sumX2 = sum([x**2 for x in xvalues])
    sumX3 = sum([x**3 for x in xvalues])
    sumX4 = sum([x**4 for x in xvalues])
    
    #Lado derecho
    sumY = sum(yvalues)
    sumXY = sum([x*y for x,y in zip(xvalues,yvalues)])
    sumX2Y = sum([x**2*y for x,y in zip(xvalues, yvalues)])

    # La ecuacion tiene la forma: y = a0 + a1*x + a2*x**2
    # Sistema de ecuaciones
    # a0*n      +   a1*sumX     +   a2*sumX2 = sumY
    # a0*sumX   +   a1*sumX2    +   a2*sumX3 = sumXY
    # a0*sumX2  +   a1*sumX3    +   a2*sumX4 = sumX2Y
    
    ecuaciones = [
        [size, sumX, sumX2, sumY],
        [sumX, sumX2, sumX3, sumXY],
        [sumX2, sumX3, sumX4, sumX2Y],
        ]

    coeficientes = gaussElimination.gaussElimination(ecuaciones)

    chartX = list(range(int(min(xvalues)), int(max(xvalues))))
    chartY = [cuadratic(coeficientes[2], coeficientes[1], coeficientes[0], x) for x in chartX]

    return chartX, chartY, coeficientes[2], coeficientes[1], coeficientes[0]
#modificar para que sea una linea
def regresionLineal(xvalues, yvalues):
    size = len(xvalues)
    
    #Lado izquierdo
    sumX = sum(xvalues)
    sumX2 = sum([x**2 for x in xvalues])
    sumX3 = sum([x**3 for x in xvalues])
    sumX4 = sum([x**4 for x in xvalues])
    
    #Lado derecho
    sumY = sum(yvalues)
    sumXY = sum([x*y for x,y in zip(xvalues,yvalues)])
    sumX2Y = sum([x**2*y for x,y in zip(xvalues, yvalues)])

    # La ecuacion tiene la forma: y = a0 + a1*x + a2*x**2
    # Sistema de ecuaciones
    # a0*n      +   a1*sumX     +   a2*sumX2 = sumY
    # a0*sumX   +   a1*sumX2    +   a2*sumX3 = sumXY
    # a0*sumX2  +   a1*sumX3    +   a2*sumX4 = sumX2Y
    
    ecuaciones = [
        [size, sumX, sumX2, sumY],
        [sumX, sumX2, sumX3, sumXY],
        [sumX2, sumX3, sumX4, sumX2Y],
        ]

    coeficientes = gaussElimination.gaussElimination(ecuaciones)

    chartX = list(range(int(min(xvalues)), int(max(xvalues))))
    chartY = [cuadratic(coeficientes[2], coeficientes[1], coeficientes[0], x) for x in chartX]

    return chartX, chartY, coeficientes[2], coeficientes[1], coeficientes[0]
