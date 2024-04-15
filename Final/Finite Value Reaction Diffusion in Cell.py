#Metabolite A diffuses within a cell and undergoes an enzymatic transformation
#We are assuming cartesian coordinates for this problem

#Importing the requisite libraries
import numpy as np
from scipy.integrate import odeint
from scipy.optimize import fminbound
import matplotlib.pyplot as plt

#Parameter values (these have been arbitrarily selected)
#TO CHANGE

# DA = 6e-3 #mm2/hr
# vmax = 6 #uM/hr
# KM = 45 #uM
L = 0.5 #mm
CAo = 50 #uM

#Let's define the system of ODEs
#The solution array is S = [C, Q] where dCdx = Q

def bvp(S, x):
    dCdx = S[1]
    dQdx = 0.02
    dSdx = [dCdx, dQdx]
    return dSdx

x = np.linspace(0,L,1000)

#Let's code the shooting method
#We know the value of CA at x = 0 
#We also know the value of Q at x = L (finite condition)
#We do not know anything about CA at x = L or Q at x = 0
#We will guess a value for Q at x = 0, solve the ODEs 
#We will then gauge the accuracy of the solution by comparing the value of Q at x = L

def shooting(Q_guess):
    S0 = [CAo, Q_guess]
    S = odeint(bvp, S0, x)
    Q_numerical = S[:,1]
    size = np.size(Q_numerical)-1 
    sol = abs(Q_numerical[size]) #dCA/dx @ x = L is 0
    return sol

#Running the optimization
Q_ini_correct = fminbound(shooting, -10000, 10000, xtol=1e-8) #some random guess

#Resolving the ODE with the correct initial value of Q
S_ini = [CAo,Q_ini_correct]
S_correct = odeint(bvp, S_ini, x)
C_correct = S_correct[:,0]

#Plotting the result
plt.plot(x, C_correct, "b")
plt.xlabel("Length (mm)")
plt.ylabel('$C_A$ (uM)')
plt.title('Homogeneous: $C_A$ (x = 0) = $C_{Ao}$ and ' r'$\frac{dC_A}{dx}$ ' '(x = L) = 0')
plt.show()

