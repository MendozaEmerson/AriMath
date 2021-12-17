from . import gaussElimination


def cuadratic(a, b, c, xVal):
    return a*xVal*xVal + b*xVal + c
def lineal(m,b,xVal):
    return b+m*xVal

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
#_Regresion_Lineal
def regresionLineal(xvalues, yvalues):

    #Se definira para una regresion lineal Simple
    size = len(xvalues)
    
    #Lado izquierdo
    sumX = sum(xvalues)                   #Sumatorio de X
    sumX2 = sum([x**2 for x in xvalues])  #Sumatorio de x^2

    sumXX = sumX*sumX
    #Lado derecho
    sumY = sum(yvalues)                    #sumatoria de y
    sumXY = sum([x*y for x,y in zip(xvalues,yvalues)])   #sumatorio de x*y 
  

    promX = sumX/size
    promY = sumY/size
    sumSSXX = sumX2-((sumX*sumX)/size)
    sumSSXY = sumXY-((sumX*sumY)/size)
    # Sistema de ecuaciones
    # m = n(sumXY)-(sumX*sumY)/(n(sumX2)-(sumX**2))
    # b = promY - m*(promX)
  
    m = sumSSXY/sumSSXX
    b = promY - promX*m

    coeficientes = [m,b]
    chartX = list(range(int(min(xvalues)), int(max(xvalues))))
    chartY = [lineal( coeficientes[0], coeficientes[1], x) for x in chartX]
  
    return chartX, chartY, coeficientes[1], coeficientes[0]
