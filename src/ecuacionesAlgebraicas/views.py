from django.shortcuts import render
import numpy as np
from sympy.parsing.sympy_parser import parse_expr

def gaussJordan(a, b):
    valores = []

    # CONVERSION
    A = np.array(a)

    B = np.array(b)

    # PROCEDIMIENTO
    casicero = 1e-15 # Considerar como 0

    # Evitar truncamiento en operaciones
    A = np.array(A,dtype=float) 

    # Matriz aumentada
    AB = np.concatenate((A,B),axis=1)
    AB0 = np.copy(AB)
    valores.append(AB0)

    # Pivoteo parcial por filas
    tamano = np.shape(AB)
    n = tamano[0]
    m = tamano[1]

    # Para cada fila en AB
    for i in range(0,n-1,1):
        # columna desde diagonal i en adelante
        columna = abs(AB[i:,i])
        dondemax = np.argmax(columna)
        
        # dondemax no está en diagonal
        if (dondemax !=0):
            # intercambia filas
            temporal = np.copy(AB[i,:])
            AB[i,:] = AB[dondemax+i,:]
            AB[dondemax+i,:] = temporal
            
    AB1 = np.copy(AB)
    valores.append(AB1)

    # eliminacion hacia adelante
    for i in range(0,n-1,1):
        pivote = AB[i,i]
        adelante = i + 1
        for k in range(adelante,n,1):
            factor = AB[k,i]/pivote
            AB[k,:] = AB[k,:] - AB[i,:]*factor
    AB2 = np.copy(AB)
    valores.append(AB2)
    
    # elimina hacia atras
    ultfila = n-1
    ultcolumna = m-1
    for i in range(ultfila,0-1,-1):
        pivote = AB[i,i]
        atras = i-1 
        for k in range(atras,0-1,-1):
            factor = AB[k,i]/pivote
            AB[k,:] = AB[k,:] - AB[i,:]*factor
        # diagonal a unos
        AB[i,:] = AB[i,:]/AB[i,i]
    X = np.copy(AB[:,ultcolumna])
    X = np.transpose([X])

    valores.append(AB)
    valores.append(X)

    return valores  


# Create your views here.

def JordanView(request):
    if request.method == 'POST':
        Ec1_str = request.POST.get("Ecuacion1")
        e1 = Ec1_str.split(' ')
        Ec1 = [float(x) for x in e1]
        
        Ec2_str = request.POST.get("Ecuacion2")
        e2 = Ec2_str.split(' ')
        Ec2 = [float(x) for x in e2]

        Ec3_str = request.POST.get("Ecuacion3")
        e3 = Ec3_str.split(' ')
        Ec3 = [float(x) for x in e3]

        Ecuaciones = [Ec1, Ec2, Ec3]

        cantidad1 = request.POST.get("resultado1")
        valor1 = cantidad1.split(' ')
        can1 = [float(x) for x in valor1]

        cantidad2 = request.POST.get("resultado2")
        valor2 = cantidad2.split(' ')
        can2 = [float(x) for x in valor2]

        cantidad3 = request.POST.get("resultado3")
        valor3 = cantidad3.split(' ')
        can3 = [float(x) for x in valor3]

        values = [can1, can2, can3]
        print(Ecuaciones)
        print(values)
        imprimir = gaussJordan(Ecuaciones, values) 
        print(imprimir[4])
        datos = {
            'resul':imprimir[4]
        }

    else:
        datos = {}

    return render(request, 'ecuacionesAlgebraicas/GaussJordan/gauss.html', datos)
