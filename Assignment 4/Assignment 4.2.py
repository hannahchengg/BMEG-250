#Question 2a
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import linregress
from scipy.integrate import odeint
from scipy.optimize import least_squares 

abs_data = pd.read_excel('Assignment 4/Absorbance data.xlsx')
enzyme_data = pd.read_excel('Assignment 4/Enzyme assay data.xlsx')

abs = abs_data["Absorbance (AU)"].values
abs_ca = abs_data["CA (mol/m3)"].values

slope, intercept, r, p, error = linregress(abs_ca, abs)
k = slope
rsquared = r**2

print("k is", k, "and r^2 is", r)

#Question 2b
time = enzyme_data['Time (min)']
enz_ca = enzyme_data['CA (mol/m3)']

def derivative(S,t):
    j = len(S)
    D = np.zeros(j)
    for i in range(0,j-1):
        D[i] = (S[i+1] - S[i])/(t[i+1] - t[i]); #Forward difference formula
    return D

v = -derivative(enz_ca,time)

#estimate the velocity using michaelis
def michaelis(substrate,params):
    #params = [vmax, Km]
    velocity = (params[0]*substrate)/(params[1]+substrate)
    return velocity

#calculate the residual
def residual(params):
    #velocity from michaelis - actual velocity
    return michaelis(enz_ca,params) - v

#find the best fit from residual
fit_nl = least_squares(residual, [1,1000000]) #Fitting, [1,5] is the initial guess for params
velfit_nl = michaelis(enz_ca, fit_nl.x) #Data for trendline, parameters stored in the x-array of fit2

vmax = fit_nl.x[0]
Km = fit_nl.x[1]

print('vmax is ', vmax, 'Km is ', Km)

plt.plot(enz_ca, v, "ko", label = 'v from experimental data')
plt.plot(enz_ca, velfit_nl, "g", label = 'v from fit')
plt.xlabel("$C_S$ (M)")
plt.ylabel('Reaction velocity (M/min)')
plt.legend()
plt.show()


#Question 2d
import matplotlib.pyplot as plt
import numpy as np

# Layer thicknesses in cm
blood_thickness = 0.22  # Approximated from 220 μL in a cylindrical well with a diameter of 0.75 cm
buffer_thickness = 0.22  # Same volume as blood
hydrogel_thickness = 0.1
total_thickness = blood_thickness + buffer_thickness + hydrogel_thickness

# Concentration of citrulline in mol/m^3 (or equivalently mmol/L here)
blood_concentration = 10  # Given for the blood layer
# Assuming a linear decrease, just for visualization
buffer_concentration_start = blood_concentration  # Assuming perfect mixing didn't occur
buffer_concentration_end = 5  # Arbitrary value for demonstration
hydrogel_concentration = 2  # Assuming significant conversion by enzyme

# Depth (y-axis) from top to bottom of the well in cm
depths = [0, blood_thickness, blood_thickness + buffer_thickness, total_thickness]

# Corresponding concentrations at each depth boundary
concentrations = [blood_concentration, buffer_concentration_start, buffer_concentration_end, hydrogel_concentration]

# Creating the plot
plt.figure(figsize=(8, 6))
plt.step(concentrations, depths, where='pre', label='Citrulline Concentration Profile')

# Customizing the plot
plt.gca().invert_yaxis()  # Invert y-axis to match the physical layout (blood at the top)
plt.title('Expected Citrulline Concentration Profile in the Well')
plt.xlabel('Citrulline Concentration (mmol/L)')
plt.ylabel('Depth in the Well (cm)')
plt.legend()
plt.grid(True)

# Display the plot
plt.show()
