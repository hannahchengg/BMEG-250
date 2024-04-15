#Importing the necessary libraries
import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import odeint

# #Let's define the parameters

#The basal expression level (after the repressor has bound to DNA)
#If we introduce the same number of gene copies in the cell, these values should be equal
#If the number of gene copies varies, they will be multiples of one another

k10 = 0.5
k20 = 0.5
k30 = 0.5
k40 = 0.5

#The activated expression level (no repressor has bound to DNA)
k11 = 50
k21 = 50
k31 = 50
k41 = 50


#Protein expression levels
k12 = 0.2
k22 = 0.2
k32 = 0.2
k42 = 0.3

#Let's assume similar rates of degradation for the proteins & mRNA
gammam = 1.5
gammap = 0.5
gammagp = 0.1

#Allosteric coefficients
n1 = 2
n2 = 2
n3 = 2
n4 = 2

#Dissociation constants
theta1 = 1
theta2 = 1
theta3 = 1
theta4 = 1


#Cell growth coefficients
umax = 0.1
Ks = 5
Ysx = 4

#Monod equation = model cell growth

#dX/dt = uX, u = specific growth rate, u = (umax*S)/(Ks + S)
#dS/dt = Ysx*dX/dt

#Repressilator math model

def repressilator(S,t):
    #[M1, M2, M3, MG, P1, P2, P3, G, X, C]
    #[0,  1,  2,  3,  4,  5,  6,  7, 8, 9]
    #M1, P1 - TetR mRNA and protein
    #M2, P2 - Lambda CL mRNA and protein
    #M3, P3 - LacI mRNA and protein
    #MG and G - GFP mRNA and protein
    #X - biomass
    #C -  substrate
    s1 = theta1**n1
    s2 = theta2**n2
    s3 = theta3**n3
    s4 = theta4**n4
    dM1dt = (k10 + ((k11*s3)/(s3+(S[6]**n3))) - gammam*S[0])
    dP1dt = (k12*S[0] - gammap*S[4])*S[8]
    dM2dt = (k20 + ((k21*s1)/(s1+(S[4]**n1))) - gammam*S[1])*S[8]
    dP2dt = (k22*S[1] - gammap*S[5])*S[8]
    dM3dt = (k30 + ((k31*s2)/(s2+(S[5]**n2))) - gammam*S[2])*S[8]
    dP3dt = (k32*S[2] - gammap*S[6])*S[8]
    dMGdt = (k40 + ((k41*s4)/(s4+(S[4]**n4))) - gammam*S[3])*S[8]
    dGdt = (k42*S[3] - gammagp*S[7])*S[8]
    dXdt = umax*S[9]*S[8]/(Ks + S[9])
    dCdt = -Ysx*umax*S[9]*S[8]/(Ks + S[9])
    dSdt = [dM1dt, dM2dt, dM3dt, dMGdt, dP1dt, dP2dt, dP3dt, dGdt, dXdt, dCdt]
    return dSdt

#Solving the system of ODEs
t = np.linspace(0, 35, 100)
S0 = [1,2,0.5,0,2.5,1.5,1.8,0,1,100] #experiment
S = odeint(repressilator, S0, t)

#Extracting the solutions
M1 = S[:,0] 
M2 = S[:,1]
M3 = S[:,2]
MG = S[:,3]
P1 = S[:,4]
P2 = S[:,5]
P3 = S[:,6]
G = S[:,7]
X = S[:,8]
C = S[:,9]

#Preparing the plots
plt.plot(t, M1, "k", label = "TetR")
plt.plot(t, M2, "b", label = r'$\lambda_{CL}$')
plt.plot(t, M3, "r", label = "LacI")
plt.plot(t, MG, "g", label = "GFP")
plt.xlabel("Time")
plt.ylabel("Transcript levels")
plt.title('Transcript data')
plt.legend()
plt.show()

plt.plot(t, P1, "k", label = "TetR")
plt.plot(t, P2, "b", label = r'$\lambda_{CL}$')
plt.plot(t, P3, "r", label = "LacI")
plt.plot(t, G, "g", label = "GFP")
plt.xlabel("Time")
plt.ylabel("Protein levels")
plt.title('Protein data')
plt.legend()
plt.show()

plt.plot(t, X, "k", label = 'Biomass')
plt.plot(t, C, "b", label = 'Substrate')
plt.plot(t, G, "g", label = 'GFP')
plt.xlabel("Time")
plt.ylabel("Concentration of biomass, substrate & GFP")
plt.title('Fermentation trends')
plt.legend()
plt.show()