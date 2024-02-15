# import libraries
import numpy as np
from scipy.integrate import solve_ivp #Using the simple ODE solver
import matplotlib.pyplot as plt


#Define System of ODEs
def odesystem (t, z):
    
    # a is a matrix of values with first col being r values
    a = [[1, 1, 1.09, 1.52, 0], 
         [0.72, 0, 1, 0.44, 1.36], 
         [1.53, 2.33, 0, 1, 0.47], 
         [1.27, 1.21, 0.51, 0.35, 1]]
    
    r1 = a[0][0]
    r2 = a[1][0]
    r3 = a[2][0]
    r4 = a[3][0]

    x1 = z[0]
    x2 = z[1]
    x3 = z[2]
    x4 = z[3]

    dx1 = r1*x1*(1 - (a[0][1]*x1 + a[0][2]*x2 + a[0][3]*x3 + a[0][4]*x4))
    dx2 = r2*x2*(1 - (a[1][1]*x1 + a[1][2]*x2 + a[1][3]*x3 + a[1][4]*x4))
    dx3 = r3*x3*(1 - (a[2][1]*x1 + a[2][2]*x2 + a[2][3]*x3 + a[2][4]*x4))
    dx4 = r4*x4*(1 - (a[3][1]*x1 + a[3][2]*x2 + a[3][3]*x3 + a[3][4]*x4))
    
    dx = [dx1, dx2, dx3, dx4]

    return dx

#solve ODE
t = np.array([0, 200])
z0 = [0.1, 0.4, 0.2, 0.5]

sol = solve_ivp(odesystem, t, z0, method='RK23',dense_output=True)

for i in range(sol.y.shape[0]):
    plt.plot(sol.t, sol.y[i], label=f'$X_{i}(t)$')
plt.xlabel('$t$') # the horizontal axis represents the time 
plt.legend() # show how the colors correspond to the components of X
plt.show()


