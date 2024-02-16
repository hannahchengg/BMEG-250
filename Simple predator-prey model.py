#Importing the requisite libraries
import numpy as np
from scipy.integrate import odeint #Using the simple ODE solver
import matplotlib.pyplot as plt

#Parameter values


#Defining the system of ODEs

def predprey(z,t):
    #z is an array of [x,y] 
    #Iindexing in python stats at 0
    # x = z[0], y = z[1]
    

    dx = []

    return dx

#Solving the system of ODEs

t = np.linspace(0, 20, 200)
z0 = [2,1]
z = odeint(predprey, z0, t)

#Extracting the values for x and y from the solution array 
 
x = z[:,0] #[rows, columns]
y = z[:,1]

#Plotting the solution

plt.subplot(2, 1, 1)
plt.plot(t, x, "k", label = 'Prey')
plt.plot(t, y, "b", label = 'Predator')
plt.xlabel("Time")
plt.ylabel("Number of individuals")
plt.legend()
#plt.show()

plt.subplot(2, 1, 2)
plt.plot(x, y, "r") #This is the implicit solution that we find analytically
plt.xlabel("Prey")
plt.ylabel("Predators")
plt.show()
