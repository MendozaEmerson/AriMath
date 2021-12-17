from django.shortcuts import render
import numpy as np

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
        Ec1_str = request.POST.get("Ecuacion1").split(' ')
        Ec1_str.split(' ')
        Ec1 = [float(x) for x in Ec1_str]
        
        datos = {}

    else:
        datos = {}

    return
