#Problem 3

#The decarboxylation of glyoxylate (S) by a mitochondrial enzyme (E) is inhibited by
#malonate (I). Raw data from an in vitro investigation has been recorded in the sheet
#‘Problem 3’ in the Excel spreadsheet. The units of v, CS and C I are mM/h, mM and mM,
#respectively. Determine the type of inhibition and the values of vmax , K M and KI .

import numpy as np
import pandas as pd
from scipy.integrate import odeint
from scipy.optimize import least_squares 
import matplotlib.pyplot as plt
from cycler import cycler

df3 = pd.read_excel('Assignment 3/Assignment 3.xlsx', 'Problem 3')

v0 = df3["v for CI = 0"].values #mM/min
v1 = df3["v for CI = 1.26"].values #mM/min
v2 = df3["v for CI = 1.95"].values #mM/min
Cs = df3["CS"].values #mM/min

#Define MM Equation
def michaelis(substrate,params):
    #params = [vmax, Km, Ki]
    velocity = (params[0]*substrate)/(params[1]+substrate)
    return velocity

#Define Residual Equation
def residual0(params):
    return michaelis(Cs,params) - v0

def residual1(params):
    return michaelis(Cs,params) - v1

def residual2(params):
    return michaelis(Cs,params) - v2

#Regression function
fit0 = least_squares(residual0, [5,1]) #Fitting, [1,5] is the initial guess for params
fit1 = least_squares(residual1, [5,1]) #Fitting, [1,5] is the initial guess for params
fit2 = least_squares(residual2, [5,1]) #Fitting, [1,5] is the initial guess for params

velfit0 = michaelis(Cs, fit0.x) #Data for trendline, parameters stored in the x-array of fit2
velfit1 = michaelis(Cs, fit1.x) #Data for trendline, parameters stored in the x-array of fit2
velfit2 = michaelis(Cs, fit2.x) #Data for trendline, parameters stored in the x-array of fit2

#Plot
plt.subplot(4,1,1)
plt.plot(Cs, v0, "ko", label = 'v from data CI = 0')
plt.plot(Cs, velfit0, "g", label = 'v from fit CI = 0')
plt.xlabel("$C_S$ (M)")
plt.ylabel('Reaction velocity (M/min)')
plt.legend()
plt.subplot(4,1,2)
plt.plot(Cs, v1, "ko", label = 'v from data CI = 1.26')
plt.plot(Cs, velfit1, "g", label = 'v from fit CI = 1.26')
plt.xlabel("$C_S$ (M)")
plt.ylabel('Reaction velocity (M/min)')
plt.legend()
plt.subplot(4,1,3)
plt.plot(Cs, v2, "ko", label = 'v from data CI = 1.95')
plt.plot(Cs, velfit2, "g", label = 'v from fit CI = 1.95')
plt.xlabel("$C_S$ (M)")
plt.ylabel('Reaction velocity (M/min)')
plt.legend()

plt.subplot(4,1,4)
plt.plot(Cs, velfit0, "r", label = 'v from fit CI = 0')
plt.plot(Cs, velfit1, "g", label = 'v from fit CI = 1.26')
plt.plot(Cs, velfit2, "b", label = 'v from fit CI = 1.95')
plt.xlabel("$C_S$ (M)")
plt.ylabel('Reaction velocity (M/min)')
plt.legend()
plt.tight_layout()
plt.show()

vmax = fit0.x[0]
vmax1 = fit1.x[0]
vmax2 = fit2.x[0]

Km = fit0.x[1]
Km1 = fit1.x[1]
Km2 = fit2.x[1]

t = np.linspace(0, 6)

print('vmax estimated by non-linear regression is', vmax, 'mM/hr')
print('vmax1 estimated by non-linear regression is', vmax1, 'mM/hr')
print('vmax2 estimated by non-linear regression is', vmax2, 'mM/hr')
print('Km estimated by non-linear regression is', Km, 'mM')
print('Km1 estimated by non-linear regression is', Km1, 'mM')
print('Km2 estimated by non-linear regression is', Km2, 'mM')

#since km increases, it must be competitive
MMconst = Km
Ci1 = 1.26
Ci2 = 1.95
Ki1 = Ci1/(Km1/MMconst-1)
Ki2 = Ci2/(Km2/MMconst-1)
print(Ki1)
print(Ki2)

#Ki values are 
0
0.5779666215929721
0.6975009273866488