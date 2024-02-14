# import libraries
import numpy as np
from scipy.integrate import odeint #Using the simple ODE solver
import matplotlib.pyplot as plt

#parameter values
a = 4
b = -3
c = 8
d = -6


#Define System of ODEs
def odesystem (z, t):
    x = z[0]
    y = z[1]
    dxdt = a*x + b*y
    dydt = c*x + d*y
    dzdt = [dxdt, dydt]
    return dzdt

#solve ODE
t = np.linspace(0, 2.5, 200)
x0 = 1 #initial x value
y0 = 1 #initial y value
z0 = [x0, y0]

z = odeint(odesystem, z0, t)
x = z[:, 0]
y = z[:, 1]

#calculate eigenvalues
arr = [[a, b], [c, d]]
eigen = np.linalg.eig(arr)
print(eigen[0])

#plot results
plt.plot(x,y)
plt.xlabel("x")
plt.ylabel("y")
plt.title("Question 2d")
plt.show()

