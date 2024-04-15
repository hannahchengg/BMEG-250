# import libraries
import numpy as np
from scipy.integrate import odeint #Using the simple ODE solver
import matplotlib.pyplot as plt


#Define System of ODEs
def system (y, x):
    dydx = x + y #TO CHANGE
    return dydx

#solve ODE
x = np.linspace(0, 20, 200)
x0 = 0 #TO CHANGE
y0 = 0 #TO CHANGE

y = odeint(system, y0, x)

#plot results
plt.plot(x,y)
plt.xlabel("x")
plt.ylabel("y")
plt.title("Question 1b")
plt.show()