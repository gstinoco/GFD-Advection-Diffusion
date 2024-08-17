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

import numpy as np
import Scripts.Gammas as Gammas
import Scripts.Neighbors as Neighbors

def Cloud(p, f, v, a, b, t, triangulation = False, tt = [], implicit = False, lam = 0.5):
    """
    2D Diffusion Equation implemented on Unstructured Clouds of Points.
    
    This function calculates an approximation to the solution of Diffusion equation in 2D using a Generalized Finite Differences scheme on unstructured clouds of points.
    
    The problem to solve is:
    
    \frac{\partial u}{\partial t}= v\nabla^2 u
    
    Input:
        p               ndarray         Array with the coordinates of the nodes and the flag for boundary or inner node.
        f               Function        Function declared with the boundary condition.
        v               Real            Diffusion coefficient.
        t               Integer         Number of time steps to be considered.
        triangulation   Logical         Select whether or not there is a triangulation available.
                                            True: Triangulation available.
                                            False: No triangulation available (Default)
        tt              ndarray         Array with the triangulation indexes.
        implicit        Logical         Select whether or not use an implicit scheme.
                                            True: Implicit scheme used.
                                            False: Explicit scheme used (Default).
        lam             Real            Lambda parameter for the implicit scheme.
                                            Must be between 0 and 1 (Default: 0.5).
    
    Output:
        u_ap        m x 1           Array           Array with the approximation computed by the routine.
        u_ex        m x 1           Array           Array with the theoretical solution.
        vec         m x nvec        Array           Array with the correspondence of the 'nvec' neighbors of each node.
    """

    # Variable initialization
    m    = len(p[:, 0])                                                             # The total number of nodes is calculated.
    nvec = 8                                                                        # Maximum number of neighbors for each node.
    T    = np.linspace(0, 1, t)                                                     # Time discretization.
    dt   = T[1] - T[0]                                                              # dt computation.
    u_ap = np.zeros([m, t])                                                         # u_ap initialization with zeros.
    u_ex = np.zeros([m, t])                                                         # u_ex initialization with zeros.
    boun_n = (p[:, 2] == 1) | (p[:, 2] == 2)                                        # Save the boundary nodes.
    inne_n = p[:, 2] == 0                                                           # Save the inner nodes.
    
    # Boundary conditions.
    for k in np.arange(t):                                                          # For each time step.
        u_ap[boun_n, k] = f(p[boun_n, 0], p[boun_n, 1], T[k], v, a, b)              # The boundary condition is assigned.
  
    # Initial condition
    u_ap[:, 0] = f(p[:, 0], p[:, 1], T[0], v, a, b)                                 # The initial condition is assigned.
    
    # Neighbor search for all the nodes.
    if triangulation == True:                                                       # If there are triangles available.
        vec = Neighbors.Triangulation(p, tt, nvec)                                  # Neighbor search with the proper routine.
    else:                                                                           # If there are no triangles available.
        vec = Neighbors.Cloud(p, nvec)                                              # Neighbor search with the proper routine.

    # Computation of Gamma values
    L = np.vstack([[-a], [-b], [2*v], [0], [2*v]])                                  # The values of the differential operator are assigned.
    K = dt*Gammas.Cloud(p, vec, L)                                                  # K computation with the required Gammas.
    
    # Generalized Finite Differences Method
    if implicit == False:                                                           # For the explicit scheme.
        K2 = np.identity(m) + K                                                     # Explicit formulation of K.
    else:                                                                           # For the implicit scheme.
        K2 = np.linalg.pinv(np.identity(m) - (1-lam)*K)@(np.identity(m) + lam*K)    # Implicit formulation of K.

    for k in np.arange(1, t):                                                       # For each of the time steps.
        un = K2@u_ap[:, k-1]                                                        # The new time-level is computed.
        u_ap[inne_n, k] = un[inne_n]                                                # Save the computed solution.
        
    # Theoretical Solution
    for k in np.arange(t):                                                          # For all the time steps.
        u_ex[:, k] = f(p[:, 0], p[:, 1], T[k], v, a, b)                             # The theoretical solution is computed.

    return u_ap, u_ex, vec