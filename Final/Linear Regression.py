#STEP 1: Import the data

#Using the Excel file 'Michaelis-Menten.xls' to get the data
#You will need Pandas and XLRD installed on your computers

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
#TO CHANGE
data = pd.read_excel('Final/', sheet_name='')

#STEP 2: Convert the Pandas dataframes into arrays

time = data[''].values #TO CHANGE
conc = data[''].values #TO CHANGE
#vel = data[''].values #TO CHANGE

#STEP 3: Plot the data

plt.plot(time, conc, "bo")
plt.xlabel("Time (min)")
plt.ylabel("$C_S$ (M)")
plt.show()

#STEP 4: Linear regression

#In order to use linear regression, we need to first estimate v
# v  = -dCS/dt

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
