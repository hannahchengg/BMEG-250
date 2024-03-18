
import numpy as np
import pandas as pd
from scipy.integrate import odeint
import matplotlib.pyplot as plt
from cycler import cycler

df1 = pd.read_excel('C:/Users/hc200/Downloads/BMEG 250/Assignment 3/Assignment 3.xlsx', 'Problem 1')
df2 = pd.read_excel('C:/Users/hc200/Downloads/BMEG 250/Assignment 3/Assignment 3.xlsx', 'Problem 2')
df3 = pd.read_excel('C:/Users/hc200/Downloads/BMEG 250/Assignment 3/Assignment 3.xlsx', 'Problem 3')

#Problem 1

# An inhibitor (I) is added to an enzymatic reaction at a level of 1.0 g/L. 
# The MichaelisMenten constant (KM) for the enzyme is known to be 9.2 g/L. 
# The data that is measured in the laboratory is provided in the sheet ‘Problem 1’ of the Excel spreadsheet. The units
# of v and Cs in the spreadsheet are g L-1 min-1 and g/L, respectively. Is the inhibitor
# competitive or non-competitive? What are the values of vmax and KI?

v = df1['v'].values
Cs = df1["CS"].values
Ci = 1
MMconst = 9.2 #g/L


v_truncated = v[v > 0]
conc_truncated = Cs[Cs > 0]

def michaelis1(substrate,params):
    #params = [vmax, Km]
    velocity = (params[0]*substrate)/(params[1]+substrate)
    return velocity


#Now let's define the residual

def residual(params):
    return michaelis1(Cs,params) - v

#Run the regression function

from scipy.optimize import least_squares 

fit_nl = least_squares(residual, [1,5]) #Fitting, [1,5] is the initial guess for params

velfit_nl = michaelis1(Cs, fit_nl.x) #Data for trendline, parameters stored in the x-array of fit2

#Plot
plt.subplot(3,1,1)
plt.plot(Cs, v, "ko", label = 'v from experimental data')
plt.plot(Cs, velfit_nl, "g", label = 'v from fit')
plt.xlabel("$C_S$ (M)")
plt.ylabel('Reaction velocity (M/min)')
plt.legend()

vmax = fit_nl.x[0]
Km = fit_nl.x[1]

print('')
print('vmax estimated by non-linear regression is', round(vmax,2), 'M/min')
Ki = Ci/(Km/MMconst-1)
print('Ki estimated by non-linear regression is', round(Ki,2), 'M')



def michaelis(S,t):
    dSdt = -(vmax*S)/(Km + S)
    return dSdt

S0 = Cs[0]
t = np.linspace(0,150,7)
S = odeint(michaelis, S0, t)

#Competitive inhibition
def competitive(S,t):
    dSdt = -(vmax*S)/(MMconst*(1 + Icomp/Ki) + S)
    return dSdt

#Competitive inhibition
plt.subplot(3,1,2)
# for i in range(1, 5):
Icomp = 1
Scomp = odeint(competitive, S0, t)
vcomp = (vmax*Scomp)/(MMconst*(1 + Icomp/Ki) + Scomp)
plt.rc('axes', prop_cycle=(cycler('color', ['r', 'g', 'b', 'c'])))
plt.plot(Scomp, vcomp, label = "$C_I$ = %i" %Icomp)
plt.plot(Cs, velfit_nl, "g", label = 'v from fit')
plt.xlabel("$C_S$")
plt.ylabel("v")
plt.title('Competitive inhibition')
plt.legend()


#Non-competitive inhibition
def noncompetitive(S,t):
    dSdt = -(vmax*S)/((MMconst + S)*(1 + Inc/Ki))
    return dSdt

#Non-competitive inhibition
plt.subplot(3,1,3)
# for i in range (1,5):
Inc =  1
Snc = odeint(noncompetitive, S0, t)
vnc = (vmax*Snc)/((MMconst + Snc)*(1 + Inc/Ki))
plt.rc('axes', prop_cycle=(cycler('color', ['r', 'g', 'b', 'c'])))
plt.plot(Snc, vnc, label = "$C_I$ = %i" %Inc)
plt.plot(Cs, velfit_nl, "g", label = 'v from fit')
plt.xlabel("$C_S$")
plt.ylabel("v")
plt.title('Non-competitive inhibition')
plt.legend()
plt.tight_layout()
plt.show()

# The inhibitor is non-competitive according to the graph
#vmax estimated by non-linear regression is 1.59 M/min
# Ki estimated by non-linear regression is 1.64 M