import numpy as np
from scipy.integrate import odeint
import matplotlib.pyplot as plt

# Constants
YS1 = 0.5
YS2 = 0.3
YP = 0.4
umax = 0.5  # h^-1
k1 = 2      # g/L
k2 = 3      # g/L

# Initial concentrations
X0 = 0.1    # g/L
S1_0 = 10   # g/L
S2_0 = 10   # g/L
P0 = 0      # g/L

# Time points
t = np.linspace(0, 10, 100)  # 10 hours

# Differential equations
def model(y, t):
    X, S1, S2, P = y

    mu = umax * (S1 / (k1 + S1) + S2 / (k2 + S2))
    dXdt = mu * X
    dS1dt = -YS1 * mu * X
    dS2dt = -YS2 * mu * X
    dPdt = YP * mu * X

    return [dXdt, dS1dt, dS2dt, dPdt]

# Initial conditions
y0 = [X0, S1_0, S2_0, P0]

# Solve the differential equations
y = odeint(model, y0, t)

# Results
X_final, S1_final, S2_final, P_final = y[-1]

S1_final = y[70, 1]
print(S1_final)

print(f"Final concentration of cells (X): {X_final:.4f} g/L")
print(f"Final concentration of substrate 1 (S1): {S1_final:.4f} g/L")
print(f"Final concentration of substrate 2 (S2): {S2_final:.4f} g/L")
print(f"Final concentration of product (P): {P_final:.4f} g/L")
