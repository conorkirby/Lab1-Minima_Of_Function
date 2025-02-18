# -*- coding: utf-8 -*-
"""
Created on Wed Sep 27 09:08:50 2023

@author: Conor Kirby
"""
import numpy as np
import matplotlib.pyplot as plt

#Excercise 1: Choosing Parabola

def f(x):
    a = 1
    b = -4
    c = 3
    return a*x*x + b*x + c

x = np.linspace(0, 4, 100)

plt.plot(x, f(x))
plt.plot(x, 0.0 * x, color = 'red')
plt.title("Finding the Roots of a Function Using Bisection Method")
plt.legend(["f(x)", "y = 0"])
#plt.savefig('C:/Users/Conor Kirby/OneDrive/Desktop/f.plot1.pdf')
plt.show()
#finding root 1
nsteps_list = np.array([])
tol_list = np.array([0.01, 0.001, 0.0001, 0.00001, 0.000001, 0.0000001, 0.00000001, 0.000000001, 0.0000000001])

for tol in (tol_list):
    print(tol)
    x1 = -1
    x3 = 2.5
    x2 = 0.5*(x1 + x3)
    print(nsteps_list)
     #number of steps
    nsteps = 0
    while abs(f(x2)) > tol: #tolerance of 0.0001
        x2 = 0.5*(x1 + x3)
        nsteps = nsteps + 1
        if f(x2) < 0:
            #plt.plot(x2, f(x2), '--o')
            x3 = x2
        elif f(x2) > 0:
            #plt.plot(x2, f(x2), '--o')
            x1 = x2
        else:
            print(str(x2) + " is the root.")
    print(nsteps)
    nsteps_list = np.append(nsteps_list, nsteps)    
print(nsteps_list)
plt.plot(-np.log10(tol_list), nsteps_list, '--ro')
plt.ylabel("Number of Steps")
plt.xlabel("-np.log10(tolerance)")
plt.title('Convergence Behaviour of the Bisection Method')
#plt.savefig('C:/Users/Conor Kirby/OneDrive/Desktop/f.bisectionmethod.pdf')
plt.show()
print(x2)




