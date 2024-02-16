# import libraries
import numpy as np
from scipy.integrate import odeint #Using the simple ODE solver
import matplotlib.pyplot as plt

#parameter values
a = 1
b = 1
c = -1
d= -1


#Define System of ODEs
def odesystem (z, t):
    x = z[0]
    y = z[1]
    dxdt = a*x + b*y
    dydt = c*x + d*y
    dzdt = [dxdt, dydt]
    return dzdt

#solve ODE
t = np.linspace(0, 2, 200)
x0 = 1 #initial x value
y0 = 1 #initial y value
z0 = [x0, y0]

z = odeint(odesystem, z0, t)
x = z[:, 0]
y = z[:, 1]

#calculate x and y values at certain time points
print("x:", z[30, 0]) #time x number of increments from t value
print("y:", z[30, 1])

#calculate eigenvalues
arr = [[a, b], [c, d]] 
eigen = np.linalg.eigvals(arr)
print("eigenvalues:", eigen)

#Plot Results
plt.subplot(2, 1, 1)
plt.plot(t, x, "k", label = 'x')
plt.plot(t, y, "b", label = 'y')
plt.xlabel("time")
plt.ylabel("variables")
plt.legend()

plt.subplot(2, 1, 2)
plt.plot(x, y, "r")
plt.xlabel("x")
plt.ylabel("y")
plt.show()