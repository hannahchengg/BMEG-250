# import libraries
import numpy as np
from scipy.integrate import odeint #Using the simple ODE solver
import matplotlib.pyplot as plt

#parameter values
a = 1
b = 1
c = 1
d= 1


#Define System of ODEs
def odesystem (z, t):
    x = z[0]
    y = z[1]
    dxdt = 0
    dydt = b*x + a*y
    dzdt = [dxdt, dydt]
    return dzdt

#solve ODE
t = np.linspace(0, 20, 200)
x0 = 0 #initial x value
y0 = -1 #initial y value
z0 = [x0, y0]

z = odeint(odesystem, z0, t)
x = z[:, 0]
y = z[:, 1]

#calculate eigenvalues
arr = [[a, b], [c, d]]
eigen = np.linalg.eig(arr)
print(eigen[0])

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