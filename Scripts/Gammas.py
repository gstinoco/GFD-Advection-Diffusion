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

import numpy as np
from joblib import Parallel, delayed

def compute_gamma_for_node(i, p, vec, L):
    """
    Compute the gamma values for a single node and update the corresponding row in K matrix.
    """
    nvec = len(vec[0, :])                                                           # The maximum number of neighbors.
    m = len(p[:, 0])                                                                # The number of nodes in x.
    K_row = np.zeros(m)                                                             # K initialization with zeros.

    if p[i, 2] == 0:                                                                # If the node is an inner node.
        nvec = sum(vec[i, :] != -1)                                                 # The total number of neighbors of the node.
        dx = np.zeros([nvec])                                                       # dx initialization with zeros.
        dy = np.zeros([nvec])                                                       # dy initialization with zeros.
        for j in np.arange(nvec):                                                   # For each of the neighbor nodes.
            vec1 = int(vec[i, j])                                                   # The neighbor index is found.
            dx[j] = p[vec1, 0] - p[i, 0]                                            # dx is computed.
            dy[j] = p[vec1, 1] - p[i, 1]                                            # dy is computed.
        M = np.vstack([[dx], [dy], [dx**2], [dx*dy], [dy**2]])                      # M matrix is assembled.
        M = np.linalg.pinv(M)                                                       # The pseudoinverse of matrix M.
        YY = M@L                                                                    # M*L computation.
        Gamma = np.vstack([-sum(YY), YY]).transpose()                               # Gamma values are found.
        K_row[i] = Gamma[0, 0]                                                      # The corresponding Gamma for the central node.
        for j in np.arange(nvec):                                                   # For each of the neighbor nodes.
            K_row[vec[i, j]] = Gamma[0, j + 1]                                      # The corresponding Gamma for the neighbor node.
    
    elif p[i, 2] == 1 or p[i, 2] == 2:                                              # If the node is in the boundary.
        K_row[i] = 1                                                                # Central node weight is equal to 1.
        for j in np.arange(nvec):                                                   # For each of the neighbor nodes.
            K_row[vec[i, j]] = 0                                                    # Neighbor node weight is equal to 0.

    return K_row

def Cloud(p, vec, L, n_jobs=-1):
    """
    2D Clouds of Points Gammas Computation with parallelization using Joblib.
    
    This function computes the Gamma values for clouds of points and assembles the K matrix using parallel computation.
    
    Input:
        p           Array           Array with the coordinates of the nodes and a flag for the boundary.
        vec         Array           Array with the correspondence of the 'nvec' neighbors of each node.
        L           Array           Array with the values of the differential operator.
        n_jobs      int             Number of jobs to run in parallel (-1 uses all processors).
    
    Output:
        K           Array           K Matrix with the computed Gammas.
    """

    m = len(p[:, 0])                                                                # The total number of nodes.
    
    # Parallel computation of each row of K using Joblib
    K_rows = Parallel(n_jobs=n_jobs)(delayed(compute_gamma_for_node)(i, p, vec, L) for i in range(m))
    
    # Combine the rows to form the full matrix K
    K = np.vstack(K_rows)
    
    return K