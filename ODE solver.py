# import libraries
import numpy as np
from scipy.integrate import odeint #Using the simple ODE solver
import matplotlib.pyplot as plt

#parameter values

#Define System of ODEs
def odesystem (y, x):
    dydx = x*(y**3)-x*y
    return dydx

#solve ODE
x = np.linspace(0, 20, 200)
x0 = 0
y0 = 0

y = odeint(odesystem, y0, x)

#plot results
plt.plot(x,y)
plt.show()