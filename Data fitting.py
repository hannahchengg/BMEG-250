#STEP 1: Import the data

#Using the Excel file 'Michaelis-Menten.xls' to get the data
#You will need Pandas and XLRD installed on your computers

import pandas as pd

data = pd.read_excel(r'Michaelis-Menten.xls', sheet_name='Data')

#STEP 2: Convert the Pandas dataframes into arrays

time = data['Time (min)'].values
conc = data['Concentration of S (M)'].values

#STEP 3: Plot the data

import matplotlib.pyplot as plt

plt.plot(time, conc, "bo")
plt.xlabel("Time (min)")
plt.ylabel("$C_S$ (M)")
plt.show()

#One can use linear or non-linear regression to fit the data
#We will use both approaches

#STEP 4: Linear regression

#In order to use linear regression, we need to first estimate v
# v  = -dCS/dt

#Let's write a function to estimate v

import numpy as np

def derivative(S,t):
    j = len(S)
    D = np.zeros(j)
    for i in range(0,j-1):
        D[i] = (S[i+1] - S[i])/(t[i+1] - t[i]); #Forward difference formula
    return D

#Estimating the derivative

v = -derivative(conc,time)

#Quick check: Does the plot look sigmoidal?

plt.plot(conc,v, "go")
plt.xlabel("$C_S$ (M)")
plt.ylabel("Reaction velocity (M/min)")
plt.show()

#Are there any instances of v being negative?

plt.plot(conc,v, "go")
plt.xlabel("$C_S$ (M)")
plt.axhline(y=0, color='k', linestyle='--')
plt.ylabel("Reaction velocity (M/min)")
plt.show()

#Let's make sure that we don't have any instances of division by zero from here onwards

v_truncated = v[v > 0]
conc_truncated = conc[conc > 0]

#Confirm with plotting

plt.plot(conc_truncated,v_truncated, "ko")
plt.axhline(y=0, color='k', linestyle='--')
plt.xlabel("$C_S$ (M)")
plt.ylabel("Reaction velocity (M/min)")
plt.show()

#Let's perform linear regression

recvel = 1/v_truncated #reciprocal of velocity
recconc = 1/conc_truncated #reciprocal of concentration of S

from sklearn.linear_model import LinearRegression

model = LinearRegression()
recconcreshaped = recconc.reshape((-1, 1)) #Transpose of the array, needed for linear fitting
model.fit(recconcreshaped, recvel) #Performing the linear regression

#Let's find the R^2 value, slope and intercept

intercept = model.intercept_ #This is 1/vmax
slope = model.coef_ #This is Km/vmax
score = model.score(recconcreshaped, recvel) #R^2 value, the quality of the fit

#Let's draw the trendline and gauge if the fit is good

fit = model.predict(recconcreshaped) #Calculating the trendline
plt.plot(recconc, recvel, "ko", label = 'Data set')
plt.plot(recconc, fit, "r", label = 'Fit')
plt.xlabel(r'$\frac{1}{C_S}$')
plt.ylabel(r'$\frac{1}{v}$')
plt.show()

#Printing the relevant information

vmax_linear = 1/intercept
Km_linear = slope/intercept

print('vmax:',np.round(vmax_linear,2))
print('Km:',np.round(Km_linear,2))
print('R^2:',np.round(score,2))

#Step 4: Non-linear regression

#We always need to define the model before we perform non-linear regression

def michaelis(substrate,params):
    #params = [vmax, Km]
    velocity = (params[0]*substrate)/(params[1]+substrate)
    return velocity

#Now let's define the residual

def residual(params):
    return michaelis(conc,params) + derivative(conc,time)

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

print('')
print('vmax estimated by non-linear regression is', round(vmax_nl,2), 'M/min')
print('Km estimated by non-linear regression is', round(Km_nl,2), 'M')

#It is clear that non-linear regression is the more accurate method

#Let's try linear regression by removing the last 5 points

l = len(recvel)
recvmod = recvel[0:l-5]
reccmod = recconc[0:l-5]

model2 = LinearRegression()
reccmodrs = reccmod.reshape((-1, 1)) #Transpose of the array
model2.fit(reccmodrs, recvmod) #Performing the linear regression

#Let's find the R^2 value, slope and intercept using the new dataset

intercept2 = model2.intercept_ #This is 1/vmax
slope2 = model2.coef_ #This is Km/vmax
score2 = model2.score(reccmodrs, recvmod) #R^2 value, the quality of the fit

#Let's draw the trendline and gauge if the fit is good this time around

fit2 = model.predict(reccmodrs) #Calculating the trendline
plt.plot(reccmod, recvmod, "ko", label = 'Data set')
plt.plot(reccmod, fit2, "r", label = 'Fit')
plt.xlabel(r'$\frac{1}{C_S}$')
plt.ylabel(r'$\frac{1}{v}$')
plt.show()

#Printing the relevant information

vmax_linear2 = 1/intercept2
Km_linear2 = slope/intercept2

print('')
print('vmax:',np.round(vmax_linear2,2))
print('Km:',np.round(Km_linear2,2))
print('R^2:',np.round(score2,2))
