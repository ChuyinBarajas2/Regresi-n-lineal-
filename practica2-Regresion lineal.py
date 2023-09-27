import numpy as np
import math 
import matplotlib.pyplot as plt

listaX=[1.2,1.4,1.6,2.1,2.3,3,3.1,3.3,3.3,3.8,4,4.1,4.1,4.2,4.6,5,5.2,5.4,6,6.1,6.9,7.2,8,8.3,8.8,9.1,9.6,9.7,10.4,10.6]
listaY=[39344,46206,37732,43526,39892,56643,60151,54446,64446,57190,63219,55795,56958,57082,61112,67939,66030,83089,81364,93941,91739,98274,101303,113813,109432,105583,116970,112636,122392,121873]

x= np.array(listaX)
y= np.array(listaY) 

datosX=len(listaX)
datosY=len(listaY)

sumx=sum(listaX)
sumy=sum(listaY)

promediox=sumx/datosX
promedioy=sumy/datosY

m=0
m1=0
m2=0
b=0
regresion=0


def funcionM(X,Y):
    global m,m1,m2
    for i in range (datosX):
        m1=m1+(X[i]-promediox)*(Y[i]-promedioy)
        m2=m2+(X[i]-promediox)**2
    m=m1/m2

    return m
            
def funcionB():
    global b
    b=promedioy-m*(promediox)
    return b
    
def regresion(X):
    return b+m*X

funcionM(listaX,listaY)
funcionB()

linea_regresion = [regresion(xi) for xi in x]


plt.xlabel("Salario")
plt.ylabel("Años")
plt.plot(listaX,listaY, "o", color='blue')
plt.plot(listaX, linea_regresion, label="Regresión Lineal", linestyle='-', color='red')
plt.grid()
plt.legend()
plt.show()