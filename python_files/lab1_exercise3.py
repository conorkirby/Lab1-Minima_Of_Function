# -*- coding: utf-8 -*-
"""
Created on Wed Oct  4 11:24:18 2023

@author: Conor Kirby
"""

import numpy as np
import matplotlib.pyplot as plt

k = 1.44
A = 1090
p = 0.033

def V(x): 
    return A*np.exp(-x/p) -k/x

x = np.linspace(0.1, 1.00, 100)
plt.ylim(-50, 100)
plt.plot(x, V(x))

def F(x):
    return -(A*np.exp(-x/p)*(-1/p) + k/(x**2))

plt.plot(x, F(x), "r")
plt.show

# V1 = A*np.exp(-x/p)*(-1/p) + k/(x**2)
def V11(x):
    return A*np.exp(-x/p)*(1/(p**2)) - 2*k/(x**3)

plt.plot(x, V11(x), "g")
plt.title("V(x), Force, V''(x)")
plt.xlabel("X Values")
plt.ylabel("Potential Energy (J) & Force (N)")
plt.legend(["Potential Energy", "Force(x)", "V''(x)"], facecolor='white', framealpha=1, labelcolor = 'black')
#plt.savefig('C:/Users/Conor Kirby/OneDrive/Desktop/f_vfv11.pdf')
plt.show()



tol_list = []
nsteps_list = []
exp_array = np.arange(-10.0, -1.0, 0.25)

for exp in exp_array:
    tol = 10**exp
    tol_list.append(tol)
#print(tol_list)

for tol in tol_list:
    x1 = -2
    nsteps = 0
    while abs(V(x1))>tol:
        x1 = x1 - V(x1)/-F(x1)
        nsteps += 1
    #print(nsteps)  
    nsteps_list.append(nsteps)

print(x1) #min = 0.15783985885829135
print(nsteps_list)    
plt.plot(-np.log10(tol_list), nsteps_list, '--mo')
plt.ylabel("Number of Steps")
plt.xlabel("-log10(tolerance)")
plt.title("Newton-Raphson Method for Ionic Interaction Potentials Exp")
plt.savefig('C:/Users/Conor Kirby/OneDrive/Desktop/f_nrmforexercise3.pdf')
plt.show()


print(F(x1)) # Value of F(x) at min of V(x) = 218.6843.... electrostatic intermolecular force??
print(V11(x1))