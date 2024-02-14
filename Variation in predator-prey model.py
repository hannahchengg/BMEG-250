#Importing the requisite libraries
import numpy as np
from scipy.integrate import odeint #Using the Runge-Kutta ODE solvers
import matplotlib.pyplot as plt

#Parameter values

a = 1 
b = 1 
c = 1
d = 1
e = 5

#Defining the system of ODEs

def predprey(z,t):
    #z is an array of [x,y]
    #Iindexing in python stats at 0
    # x = z[0], y = z[1]
    dxdt = a*z[0] - b*z[0]*z[1] - (a/e)*(z[0]**2)
    dydt = c*z[0]*z[1] - d*z[1] 
    dzdt = [dxdt, dydt]
    return dzdt

#Solving the system of ODEs

t = np.linspace(0, 40, 400)
z0 = [2,1]
z = odeint(predprey, z0, t)

#Extracting the values for x and y from the solution array 
 
x = z[:,0]
y = z[:,1]



#Plotting the solution

plt.subplot(2, 1, 1)
plt.plot(t, x, "k", label = 'Prey')
plt.plot(t, y, "b", label = 'Predator')
plt.xlabel("Time")
plt.ylabel("Number of individuals")
plt.legend()

plt.subplot(2, 1, 2)
plt.plot(x, y, "r")
plt.xlabel("Prey")
plt.ylabel("Predators")
plt.show()