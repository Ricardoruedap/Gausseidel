#!/usr/bin/env python3
# -*- coding: utf-8 -*-
'''
De ejemplo se solucionará el sistema de ecuaciones:
    3x + y - 3z = 7
    5x - 4y + z = -19
    x - y - 4z = 4

'''
import numpy as np

def leer_txt(text_basis):
    a_temp, b_temp = text_basis.strip().split("=")
    b_temp = eval(b_temp.strip(""))
    a_temp = a_temp[:-1]
    a_temp = [eval(i) for i in a_temp.split()]
    
    return a_temp, b_temp

A = []
b = []

with open("/Users/eduardomv/Desktop/A C T U A R Í A/3er SEMESTRE/Métodos Numéricos/Gauss Seidel/Sistema con Pivoteo.txt", "r") as f:
    flag = 0
    for line in f:
        if line.strip() != "X":
            pass
        else:
            flag = 1
            continue
        if line == "Y":
            break
        
        if flag == 1:
            aux_1, aux_2 = leer_txt(line)
            A.append(aux_1)
            b.append(aux_2)

print("A = ", A)
print("b = ", b)

def Matriz_cuadrada(M):
    if len(M) != len(M[0]):
        print("La matriz no es cuadrada.\n")
    else:
        print("La matriz sí es cuadrada.\n")

Matriz_cuadrada(A)
A_np = np.array(A)
b_np = np.array(b)

def Pivoteo_C(R, v):
    t = np.shape(R)
    n = t[0]
    for i in range(0, n-1, 1):
        filaR = abs(R[i:, i])
        maxR = np.argmax(filaR)
        if(maxR != 0):
            aux = np.copy(R[:, i])
            R[:,i] = R[:,maxR+i]
            R[:,maxR+i] = aux
            print("A =", R)
            auxv = np.copy(v[i])
            v[i] = v[maxR+i]
            v[maxR+i] = auxv
            print("b =", v)
        return R, v

iter_max = 1000
umbral = 0.00001
def Gauss_Seidel_Numpy(A_np, b_np):
    n=len(A[0])
    aux_np = np.zeros(n)
    x_np = np.zeros(n)
    for i in range(iter_max):
        for i in range(n):
            aux_np[i] = 0
            x_np[i] = (b_np[i]-np.sum(x_np*aux_np*A_np[i,:]))/A_np[i][i]
            aux_np[i] = 1
        current_b = np.dot(A_np,x_np)
        error = np.sum(np.abs(current_b-b_np))
        if error < umbral:
            return x_np

print("\nResultado mediante función numpy: (x, y, z)")
print(Gauss_Seidel_Numpy(A_np, b_np))