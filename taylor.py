
import numpy as np
import sympy as sym


x  = sym.Symbol('x')
fx = sym.sympify(sym.E**x) 
muestras = 51
x0 = 0
grado = 4      
n  = grado + 1  

k = 0
polinomio = 0
while (k < n):
    derivada   = fx.diff(x,k)
    derivadax0 = derivada.subs(x,x0)
    divisor   = np.math.factorial(k)
    terminok  = (derivadax0/divisor)*(x-x0)**k
    polinomio = polinomio + terminok
    k = k + 1

polinomioSustitucion = polinomio.subs(x,0.8)
print("El polinomio es:\n")
print(polinomio)
print("El resultado de P(0.8):\n")
print(polinomioSustitucion)