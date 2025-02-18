# -*- coding: utf-8 -*-
"""
Created on Wed Oct  4 10:11:50 2023

@author: Conor Kirby
"""
import numpy as np
import matplotlib.pyplot as plt

def f(x):
    a = 1
    b = -4
    c = 3
    return a*x*x + b*x + c

def f1(x):
    a = 1
    b = -4
    return 2*a*x + b
    

x1 = -2
x = np.linspace(-2, 6, 100)
plt.plot(x, f(x))
plt.plot(x, f1(x))
plt.plot(x1, f1(x1), "ro")
plt.title("Finding the Roots of a Function Using the Newton-Raphson Method")
plt.legend(["f(x)", "The Derivative of f(x)"])
#plt.savefig('C:/Users/Conor Kirby/OneDrive/Desktop/f.plot2.pdf')
plt.show()


tol_list = []
nsteps_list = []
exp_array = np.arange(-40.0, -2.0, 1)

for exp in exp_array:
    tol = 10**exp
    tol_list.append(tol)
#print(tol_list)
for tol in tol_list:
    x1 = -2
    nsteps = 0
    while abs(f(x1))>tol:
        x1 = x1 - f(x1)/f1(x1)
        nsteps += 1
    #print(nsteps)  
    nsteps_list.append(nsteps)
print(nsteps_list)    
plt.plot(-np.log10(tol_list), nsteps_list, '--ro')
plt.ylabel("Number of Steps")
plt.xlabel("-log10(tolerance)")
plt.title("Convergence Behaviour of the Newton-Raphson Method")
#print(nsteps) #much more efficient than the bisection method 
print(x1)
print(f(x1))
    

#plt.savefig('C:/Users/Conor Kirby/OneDrive/Desktop/f.convofNRM.pdf')


