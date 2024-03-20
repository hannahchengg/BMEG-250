#Problem 2

#Kinetic data provided in the Excel spreadsheet.
#Units of v and Cs in the spreadshet are uM/min and M.
#Determine vmax and Km for the enzyme

import pandas as pd
from scipy.optimize import least_squares 
import matplotlib.pyplot as plt


df2 = pd.read_excel('Assignment 3/Assignment 3.xlsx', 'Problem 2')

v = df2["v"].values * 10**(-6) #M/min
Cs = df2["CS"].values #M

print(v)
#Define MM Equation
def michaelis(substrate,params):
    #params = [vmax, Km]
    velocity = (params[0]*substrate)/(params[1]+substrate)
    return velocity

#Define Residual Equation
def residual(params):
    return michaelis(Cs,params) - v

#Regression function
fit_nl = least_squares(residual, [0.00012, 0.0001]) #Fitting, [1,5] is the initial guess for params

velfit_nl = michaelis(Cs, fit_nl.x) #Data for trendline, parameters stored in the x-array of fit2

#Plot
plt.plot(Cs, v, "ko", label = 'v from experimental data')
plt.plot(Cs, velfit_nl, "g", label = 'v from fit')
plt.xlabel("$C_S$ (M)")
plt.ylabel('Reaction velocity (M/min)')
plt.legend()
plt.show()

vmax_nl = fit_nl.x[0]
Km_nl = fit_nl.x[1]

print('vmax estimated by non-linear regression is', vmax_nl, 'M/min')
print('Km estimated by non-linear regression is', Km_nl, 'M')