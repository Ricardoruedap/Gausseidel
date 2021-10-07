#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Sep 29 11:13:32 2021

@author: eduardomv
"""
import numpy as np
# Pivoteo parcial por filas
# Solución a Sistemas de Ecuaciones

# INGRESO
A = np.array([[4,2,5],
              [2,5,8],
              [5,4,3]])

B = np.array([[60.70],
              [92.90],
              [56.30]])

# PROCEDIMIENTO
# Matriz aumentada
AB  = np.concatenate((A,B),axis=1)
AB0 = np.copy(AB)

# Pivoteo parcial por filas
tamano = np.shape(AB)
n = tamano[0]
m = tamano[1]

# Para cada fila en AB
for i in range(0,n-1,1):
    # columna desde diagonal i en adelante
    fila = abs(AB[i:,i])
    dondemax = np.argmax(fila)
    
    # dondemax no está en diagonal
    if (dondemax !=0):
        # intercambia filas
        temporal = np.copy(AB[i,:])
        AB[i,:]  = AB[dondemax+i,:]
        AB[dondemax+i,:] = temporal

# SALIDA
print('Matriz aumentada:')
print(AB0)
print('Pivoteo parcial por filas')
print(AB)
