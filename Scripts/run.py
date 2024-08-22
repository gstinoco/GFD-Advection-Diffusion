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
import os
import re
import numpy as np
import Scripts.Graph as Graph
import Scripts.Errors as Errors
import AdvectionDiffusion

## Create a dictionary to get all the regions in da Data folder.
def group_files_by_region(files):
    pattern = re.compile(r'^(.*?)(_p\.csv|_tt\.csv)$')                                      # Look for the files ending in "_p.csv" and "_tt.csv"
    regions = {}                                                                            # Dictionary for the regions.
    for file in files:                                                                      # For each of the files in clouds.
        match = pattern.match(file)                                                         # Check for the match of the pattern with the file.
        if match:                                                                           # If is a match.
            region, suffix = match.groups()                                                 # Get the name of the region.
            if region not in regions:                                                       # If the file haven't been added.
                regions[region] = {}                                                        # Create an empty entry.
            regions[region][suffix] = file                                                  # Add the file to the regions.
    return regions                                                                          # Return the regions dictionary.

## Process the regions and compute the solutions.
def process_region(f, v, a, b, t, region, files, data_path, results_path, save):
    print(f'Working on region: {region}')
    if '_p.csv' in files and '_tt.csv' in files:                                            # Check the existence of points and triangles.
        p_file_path  = os.path.join(data_path, files['_p.csv'])                             # Get the file path for the points.
        tt_file_path = os.path.join(data_path, files['_tt.csv'])                            # Get the file path fot the triangles.

        p  = np.genfromtxt(p_file_path,  delimiter = ',', skip_header = 0)                  # Load the coordinates of the points.
        tt = np.genfromtxt(tt_file_path, delimiter = ',', skip_header = 0)                  # Load the triangles correspondence.

        u_ap, u_ex, vec = AdvectionDiffusion.Cloud(p, f, v, a, b, t, triangulation = triangulation, tt = tt, implicit = Implicit, lam = 0.1)
                                                                                            # Compute the numerical solution.

        er = Errors.Cloud(p, vec, u_ap, u_ex)                                               # Compute the error.
        print(f'\tError: {np.mean(er)}')                                                    # Print the mean of the error.

        if save:                                                                            # If we are going to save.
            os.makedirs(os.path.join(results_path, region), exist_ok = True)
                                                                                            # Ensure the directory exists.
            error_path = os.path.join(results_path, region, 'Error.txt')
                                                                                            # Set the name of the file for the error.
            with open(error_path, 'w') as file:                                             # Create the file.
                file.write(str(np.mean(er)))                                                # Save the error.

            computed_solution_path = os.path.join(results_path, region, 'Computed Solution.csv')
                                                                                            # Set the name of the file for the computed solution.
            np.savetxt(computed_solution_path, u_ap, delimiter = ',', fmt = '%.8f')         # Save the computed solution.

            theoretical_solution_path = os.path.join(results_path, region, 'Theoretical Solution.csv')
                                                                                            # Set the name of the file for the theoretical solution.
            np.savetxt(theoretical_solution_path, u_ex, delimiter = ',', fmt = '%.8f')      # Save the theoretical solution.

            plot_path = os.path.join(results_path, region, 'Solution')
                                                                                            # Set the name for the resulting graphs.
            Graph.Cloud_Transient_Steps_1(p, tt, u_ap, nom = plot_path)                     # Save the resulting graphs.

        plot_path = os.path.join(results_path, region, 'Solution.mp4')
                                                                                            # Set the name for the resulting video.
        Graph.Cloud_Transient_1(p, tt, u_ap, save = Save, nom = plot_path)                  # Save the resulting video.

def run_simulation(f, v, a, b, t, implicit, data, exam = 'test', holes = False, save = True):
    global Implicit, triangulation, Save
    Implicit      = implicit
    Save          = save                                                                    # Choose wether the results must be saved.
    triangulation = False                                                                   # Neighbors like in a triangulation?

    if holes:
        results_clouds = 'Results/'+ exam + '/Holes/'                                       # Folder to save the results (explicit).
    else:
        results_clouds = 'Results/'+ exam + '/Clouds/'                                      # Folder to save the results (explicit).
    
    clouds = os.listdir(data)                                                               # List for the clouds.

    regions_c = group_files_by_region(clouds)                                               # Create a dictionary for all the regions in Clouds.

    for region, files in regions_c.items():                                                 # For each of the regions.
        process_region(f, v, a, b, t, region, files, data, results_clouds, Save)            # Process the region.