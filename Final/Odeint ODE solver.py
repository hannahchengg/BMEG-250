#Importing the requisite libraries
import numpy as np
from scipy.integrate import odeint #Using the simple ODE solver
import matplotlib.pyplot as plt

#Parameter values TO CHANGE
a = 2
b = 2
c = 1
d = 1

#Defining the system of ODEs

def system(z,t):
    #z is an array of [x,y] 
    #Indexing in python stats at 0
    # x = z[0], y = z[1]
    dxdt = a*z[0] - b*z[0]*z[1] #TO CHANGE BASED ON EQN
    dydt = c*z[0]*z[1] - d*z[1] #TO CHANGE BASED ON EQN
    dzdt = [dxdt, dydt]
    return dzdt

#Solving the system of ODEs

t = np.linspace(0, 20, 200)
z0 = [2,1] #INITIAL VALUES TO CHANGE
z = odeint(system, z0, t)

#Extracting the values for x and y from the solution array 
 
x = z[:,0] #[rows, columns]
y = z[:,1]

# calculate x and y values at certain time points
print("x:", z[-1, 0]) #REPLACE INDEX 0 WITH THE DESIRED TIME
print("y:", z[-1, 1]) #REPLACE INDEX 0 WITH THE DESIRED TIME

#Calculate partial derivatives for Jacobian matrix and eigenvalues
def eigencalc(e):
    x = e[0]
    y = e[1]
    f1dx = 1 - (2*x)/5 -y #manual derivative
    f1dy = -x #manual derivative
    f2dx = y #manual derivative
    f2dy = x-1 #manual derivative

    j = [[f1dx, f1dy], [f2dx, f2dy]]
    eigen =  np.linalg.eigvals(j)
    return eigen

#Find EQ points
#manual calculations; set dxdt to 0 and solve for values of x1, y1
#then set dydt to 0 and solve for values of x2, y2
#EQ = (x1, y2), (x2, y1)
#use these values for determining eigenvalues

e1 = [0, 0] #TO CHANGE ACCORDING TO CALCULATED EQ POINTS
e2 = [1, 1] #TO CHANGE ACCORDING TO CALCULATED EQ POINTS

#if real part eigenvalues are positive --> unstable; sys diverges
#if real part eigenvalues are negative --> stable; converges to EQ
#if real part eigenvalues are 0 --> continuous oscillation; circle
#if real part eignevalues mixed signs --> saddle point

print("e1:", eigencalc(e1))
print("e2:", eigencalc(e2))

#Plotting the solution
plt.subplot(2, 1, 1)
plt.plot(t, x, "k", label = 'x(t)')
plt.plot(t, y, "b", label = 'y(t)')
plt.xlabel("Time")
plt.ylabel("Number of individuals")
plt.legend()
#plt.show()

plt.subplot(2, 1, 2)
plt.plot(x, y, "r") #This is the implicit solution that we find analytically
plt.xlabel("x(t)")
plt.ylabel("y(t)")
plt.show()
