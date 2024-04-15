#This code allows you to solve a second-order ODE

#The guiding principle is to re-cast the BVP as a system of IVPs

#Let's first plot the analytical solutions

#Importing the requisite libraries
import numpy as np
import matplotlib.pyplot as plt

#Let us first consider the analytical solutions

CAo = 50 #picking an arbitrary value for CAo
L = 0.5 # millimeter

def analytical(x,phi):
    s = (phi*x)/L
    C = CAo*(((-np.exp(-phi)*np.sinh(s))/np.sinh(phi)) + np.exp(-s))
    return C

#Plotting analytical solutions as a series of solutions to infer influence of the Thiele modulus

x = np.linspace(0,L,100)
phiarray = np.linspace(0.01, 10,10) #creating a series of phi values to see how the Thiele modulus impacts performance
m = np.size(x)
n = np.size(phiarray)
Canalytical = np.zeros((m,n))

i = 0 #counter

while i < n:
    p = phiarray[i]
    Canalytical[:,i] = analytical(x,p)
    if i == 0:
        plt.plot(x, Canalytical[:,i], "b", label = r'$\phi$' " = 0.01")
    elif i == 3:
        plt.plot(x, Canalytical[:,i], "g")#, label = r'$\phi$' " = 3")
    elif i == n-1:
        plt.plot(x, Canalytical[:,i], "r", label = r'$\phi$' " = 10")
    else:
        plt.plot(x, Canalytical[:,i], "k")
    i += 1

plt.xlabel("x")
plt.ylabel('$C_A$')
plt.title('Analytical solutions for $C_A$ (x = 0) = $C_{Ao}$ and $C_A$ (x = L) = 0')
plt.legend()
plt.show()

#Now let's solve this problem using Python

from scipy.integrate import odeint
from scipy.optimize import fmin

#odeint only solves IVPs
#This means we need to use the shooting method to solve the BVP
#The shooting method is simply an optimization problem
#We will solve the problem for a single value of phi to demonstrate the method

P = 0.01 #value for phi that we will use to solve the BVP numerically
x = np.linspace(0,L,25) #Re-defining x so that we have a clearer plot

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
    S0 = Q_guess
    S = odeint(bvp, S0, x)
    Q_numerical = S[:,1]
    size = np.size(Q_numerical)-1 
    sol = abs(Q_numerical[size]) #dCA/dx @ x = L is 0
    return sol

#Running the optimization
guess = -20
guess_array = [CAo, guess]
Q_ini_correct = fmin(shooting, guess_array, xtol=1e-8) #some random guess

#Resolving the ODE with the correct initial value of Q
S_ini = [CAo,Q_ini_correct[1]]
S_correct = odeint(bvp, S_ini, x)
C_correct = S_correct[:,0]
C_analytical = analytical(x,P)

#Plotting the result
plt.plot(x, C_analytical, "ko", label = 'Analytical solution')
plt.plot(x, C_correct, "k--", label = 'Numerical solution')
plt.xlabel("x")
plt.ylabel('$C_A$')
plt.title('Solutions for $C_A$ (x = 0) = $C_{Ao}$ and $C_A$ (x = L) = 0 for ' r'$\phi$' " = 3")
plt.legend()
plt.show()