import math
import numpy as np

#Iniciamos el algoritmo con las siguientes variables
cifras = -1 #Iniciamos para ingresar en el bucle while uno
ea = 1000 
tabla = []
while cifras < 0: #while uno

    cifras = int(input("Ingrese la cantidad de cifras"))

    if cifras < 0: 
        print("No se puede efectuar, ingrese una cantidad positiva")
    else:
        es = 0.5*(10**(2-cifras))

valorDeX = 0   
#Para evitar ceros en el denominador
while valorDeX == 0:
    valorDeX = float(input("Ingrese el valor de x, debe de ser psotiva"))
    if valorDeX == 0:
        print("Ingrese un valor distinto de cero")

#Es float para poder determinar cualquier valor real
actual = 1/valorDeX + 1
n = 1 #Contador parar el exponente de x
p = 2 #Contador para el denominador


while ea > es: 
    anterior = actual 
    actual = actual + (valorDeX**n)/((math.factorial(p-1))*p)
    ea = abs((actual-anterior)/actual)*100
    n = n + 1 
    p = p +1
    tabla.append([n,actual,ea])
tabla = np.array(tabla)
np.savetxt("tablaDeIteraciones.csv",tabla,delimiter=",")
print(actual)

    

