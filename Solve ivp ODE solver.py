# import libraries
import numpy as np
from scipy.integrate import solve_ivp #Using the simple ODE solver
import matplotlib.pyplot as plt

#parameters:
a = 2/3
b = 0.04
c = 0.008
d = 0

#Define System of ODEs
def odesystem (t, z):

    x = z[0]
    y = z[1]

    dxdt = 1/b* (x*(1-x) + (a*(c-x)*y)/(c+x))
    dydt = x - y
    dz = [dxdt, dydt]
    return dz

#solve ODE
t = np.array([0, 20])
z0 = [2, 2]

sol = solve_ivp(odesystem, t, z0, method='RK23',dense_output=True)

plt.subplot(2, 1, 1)
for i in range(sol.y.shape[0]):
    plt.plot(sol.t, sol.y[i], label=f'$X_{i}(t)$')
plt.xlabel('$t$') # the horizontal axis represents the time 
plt.legend() # show how the colors correspond to the components of X

plt.subplot(2, 1, 2)
plt.plot(sol.y[1], sol.y[0], "r")
plt.xlabel("x")
plt.ylabel("y")
plt.show()