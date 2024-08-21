"""
All the codes presented below were developed by:
    Dr. Gerardo Tinoco Guerrero
    Universidad Michoacana de San Nicolás de Hidalgo
    gerardo.tinoco@umich.mx

With the funding of:
    National Council of Humanities, Sciences and Technologies, CONAHCyT (Consejo Nacional de Humanidades, Ciencias y Tecnologías, CONAHCyT). México.
    Coordination of Scientific Research, CIC-UMSNH (Coordinación de la Investigación Científica de la Universidad Michoacana de San Nicolás de Hidalgo, CIC-UMSNH). México
    Aula CIMNE-Morelia. México

Date:
    July, 2023.

Last Modification:
    October, 2023.
"""

# Library importation
import numpy as np
from Scripts.run import run_simulation

# State the conditions for the problem.
## Problem Parameters
v = 0.02                                                                                    # Diffusion coefficient.
a = 0.5                                                                                     # Transport velocity on the x direction.
b = 0.5                                                                                     # Transport velocity on the y direction.
t = 2000                                                                                    # Number of time-steps.

## Function for the problem.
f = lambda x, y, t, v, a, b:  np.sin(np.pi*(x - a*t))*np.sin(np.pi*(y - b*t))*np.exp(-v*t)

# Should I save the results?
save = True

# Environment Variables for the functions
exam = 'Example 3'

# Run simulation with clouds.
data = 'Data/Clouds/'
print('Simulations for Simply Connected domains.')
run_simulation(f, v, a, b, t, implicit = False, data = data, exam = exam, holes = False, save = save)

# Run simulations with clouds with holes.
data = 'Data/Holes/'
print('Simulations for non-Simply Connected.')
run_simulation(f, v, a, b, t, implicit = False, data = data, exam = exam, holes = True, save = save)