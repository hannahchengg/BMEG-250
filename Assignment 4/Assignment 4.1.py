import numpy as np
from scipy.integrate import solve_bvp
import matplotlib.pyplot as plt

 # Constants and initial conditions
D_water = 0.5e-4  # m^2/s, diffusivity in water
D_organic = 6e-3  # m^2/s, diffusivity in organic
k = 2e-2  # 1/s, reaction rate constant
J = 0.001  # mol/m^2/s, flux through membrane
c_wall = 2  # mol/m^3, concentration at water wall
x_mid = 0.25  # m, midway point

# Function to solve for concentration profile in organic compartment
def organic_profile(c0):
    lambda_ = np.sqrt(k / D_organic)
    
    def ode_system(x, y):
        return [y[1], k / D_organic * y[0]]
    
    def bc(ya, yb):
        return [ya[0] - c0, yb[0]]
    
    x_span = [0, 0.5]  # From x=0 to x=0.5 m (end of organic compartment)
    y_init = [c0, -J / D_organic]  # Starting with c0 and derivative from flux condition
    
    sol = solve_bvp(ode_system, bc, np.linspace(*x_span, 100), np.zeros((2, 100)))
    
    if sol.success:
        c_mid = sol.sol(x_mid)[0]
        return c_mid
    else:
        raise RuntimeError("Failed to solve BVP for organic compartment.")

# Midway concentration in water compartment
c_water_mid = c_wall - (J * x_mid / D_water)

# Finding c0 for the organic compartment using iterative approach to match flux
c0_guess = J * x_mid / D_organic  # Initial guess for c0 at x=0 in organic compartment

# Solve for organic profile with guessed c0
c_organic_mid = organic_profile(c0_guess)

# Display the results
difference = c_water_mid - c_organic_mid
print(difference)