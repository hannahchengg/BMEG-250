# import libraries
import numpy as np
from scipy.integrate import solve_ivp #Using the simple ODE solver
import matplotlib.pyplot as plt

#parameters TO CHANGE
a = 2/3
b = 0.04
c = 0.008
d = 0

#Define System of ODEs
def system (t, z):
    x = z[0]
    y = z[1]
    dxdt = 1/b* (x*(1-x) + (a*(c-x)*y)/(c+x)) #TO CHANGE
    dydt = x - y #TO CHANGE
    dz = [dxdt, dydt]
    return dz

#solve ODE
t = np.array([0, 20])
z0 = [2, 2] #TO CHANGE

sol = solve_ivp(system, t, z0)

#plots x and y against time
plt.subplot(2, 1, 1)
plt.plot(sol.t, sol.y[0], label= 'y(t)')
plt.plot(sol.t, sol.y[1], label= 'x(t)')
plt.xlabel('Time') 
plt.legend()

#plots x against y
plt.subplot(2, 1, 2)
plt.plot(sol.y[1], sol.y[0], "r")
plt.xlabel("x")
plt.ylabel("y")
plt.show()