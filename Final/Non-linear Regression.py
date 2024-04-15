#STEP 1: Import the data

#Using the Excel file 'Michaelis-Menten.xls' to get the data
#You will need Pandas and XLRD installed on your computers

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import least_squares 

data = pd.read_excel('Final/', sheet_name='')

#STEP 2: Convert the Pandas dataframes into arrays

time = data[''].values
conc = data[''].values
#vel = data[''].values #TO CHANGE

#STEP 3: Plot the data

plt.plot(time, conc, "bo")
plt.xlabel("Time (min)")
plt.ylabel("$C_S$ (M)")
plt.show()

#We always need to define the model before we perform non-linear regression

def michaelis(substrate,params):
    #params = [vmax, Km]
    velocity = (params[0]*substrate)/(params[1]+substrate)
    return velocity

#Now let's define the residual

#IF VELOCITY IS NOT GIVEN IN THE DATA:
def derivative(S,t):
    j = len(S)
    D = np.zeros(j)
    for i in range(0,j-1):
        D[i] = (S[i+1] - S[i])/(t[i+1] - t[i]); #Forward difference formula
    return D

v = -derivative(conc,time)

#IF VELOCITY IS GIVEN IN THE DATA
#v = -vel

def residual(params):
    return michaelis(conc,params) - v

#Run the regression function

from scipy.optimize import least_squares 

fit_nl = least_squares(residual, [1,5]) #Fitting, [1,5] is the initial guess for params

velfit_nl = michaelis(conc, fit_nl.x) #Data for trendline, parameters stored in the x-array of fit2

#Plot
plt.plot(conc, v, "ko", label = 'v from experimental data')
plt.plot(conc, velfit_nl, "g", label = 'v from fit')
plt.xlabel("$C_S$ (M)")
plt.ylabel('Reaction velocity (M/min)')
plt.legend()
plt.show()

vmax_nl = fit_nl.x[0]
Km_nl = fit_nl.x[1]

print('vmax estimated by non-linear regression is', round(vmax_nl,2), 'M/min')
print('Km estimated by non-linear regression is', round(Km_nl,2), 'M')
