# import libraries
import numpy as np
from scipy.integrate import odeint #Using the simple ODE solver
import matplotlib.pyplot as plt

#parameter values


#Define System of ODEs
def odesystem (z, t):
    x = z[0]
    y = z[1]
    dxdt = 4*x - 3*y
    dydt = 8*x - 6*y
    dzdt = [dxdt, dydt]
    return dzdt

#solve ODE
t = np.linspace(0, 20, 200)
x0 = 1 #initial x value
y0 = 1 #initial y value
z0 = [x0, y0]

z = odeint(odesystem, z0, t)
x = z[:, 0]
y = z[:, 1]

#plot results
plt.plot(x, y)
plt.show()