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

## Library importation.
import numpy as np
import matplotlib.pyplot as plt
from matplotlib import cm
from matplotlib.animation import FuncAnimation

def Cloud_Transient(p, tt, u_ap, u_ex, save = False, nom = ''):
    """
    Cloud

    This function graphs and saves the approximated and theoretical solutions of the problem being solved at several time levels.
    Both solutions are presented side by side to help perform graphical comparisons between both solutions.

    Input:
        p               ndarray         Array with the coordinates of the nodes.
        tt              ndarray         Array with the correspondence of the n triangles.
        u_ap            ndarray         Array with the computed solution.
        u_ex            ndarray         Array with the theoretical solution.
        save            bool            Save the graphic.
                                        True: Save the created graphs.
                                        False: Don't save the created graphs (Default).
        nom             string          Name of the files to be saved to drive.
        
    Output:
        None
    """

    ## Variable initialization.
    t       = u_ex.shape[1]
    step    = max(1, t // 50)
    T       = np.linspace(0, 1, t)
    min_val = u_ex.min()
    max_val = u_ex.max()

    fig, (ax1, ax2) = plt.subplots(1, 2, subplot_kw = {"projection": "3d"}, figsize = (10, 5))
    
    if save:
        def update_plot(k):
            k = min(k, t - 1)
            ax1.clear()
            ax2.clear()
            tin = float(T[k])
            fig.suptitle('Solution at t = %1.3f s.' % tin)
            
            ax1.plot_trisurf(p[:, 0], p[:, 1], u_ap[:, k], triangles = tt, cmap = cm.coolwarm, linewidth = 0, antialiased = False)
            ax1.set_zlim([min_val, max_val])
            ax1.set_title('Approximation')
            
            ax2.plot_trisurf(p[:, 0], p[:, 1], u_ex[:, k], triangles = tt, cmap = cm.coolwarm, linewidth = 0, antialiased = False)
            ax2.set_zlim([min_val, max_val])
            ax2.set_title('Theoretical Solution')
            
            return fig, 
    
        ani = FuncAnimation(fig, update_plot, frames = np.arange(0, t+1, step), blit = True)
        ani.save(nom, writer = 'ffmpeg', fps = 10)
        plt.close()

    else:
        for k in np.arange(0, t, step):
            tin = float(T[k])
            fig.suptitle('Solution at t = %1.3f s.' %tin)

            ax1.plot_trisurf(p[:, 0], p[:, 1], u_ap[:, k], triangles = tt, cmap = cm.coolwarm, linewidth = 0, antialiased = False)
            ax1.set_zlim([min_val, max_val])
            ax1.set_title('Approximation')
            
            ax2.plot_trisurf(p[:, 0], p[:, 1], u_ex[:, k], triangles = tt, cmap = cm.coolwarm, linewidth = 0, antialiased = False)
            ax2.set_zlim([min_val, max_val])
            ax2.set_title('Theoretical Solution')

            plt.pause(0.01)
            ax1.clear()
            ax2.clear()

        tin = float(T[-1])
        fig.suptitle('Solution at t = %1.3f s.' %tin)

        ax1.plot_trisurf(p[:, 0], p[:, 1], u_ap[:, -1], triangles = tt, cmap = cm.coolwarm, linewidth = 0, antialiased = False)
        ax1.set_zlim([min_val, max_val])
        ax1.set_title('Approximation')
        
        ax2.plot_trisurf(p[:, 0], p[:, 1], u_ex[:, -1], triangles = tt, cmap = cm.coolwarm, linewidth = 0, antialiased = False)
        ax2.set_zlim([min_val, max_val])
        ax2.set_title('Theoretical Solution')

        plt.pause(0.1)
        plt.close()


def Cloud_Transient_Steps(p, tt, u_ap, u_ex, nom):
    """
    Cloud_Steps

    This function graphs and saves the approximated and theoretical solutions of the problem being solved at three different time levels.
    Both solutions are presented side by side to help perform graphical comparisons between both solutions.

    Input:
        p               ndarray         Array with the coordinates of the nodes.
        tt              ndarray         Array with the correspondence of the n triangles.
        u_ap            ndarray         Array with the computed solution.
        u_ex            ndarray         Array with the theoretical solution.
        nom             string          Name of the files to be saved to drive.
    
    Output:
        None
    """

    ## Variable initialization.
    t       = u_ex.shape[1]
    step    = max(1, t // 3)
    min_val = u_ex.min()
    max_val = u_ex.max()
    T       = np.linspace(0, 1, t)

    ## Create the graphs.
    for k in np.arange(0, t+1, step):
        if k >= t:
            k = t - 1
        fig, (ax1, ax2) = plt.subplots(1, 2, subplot_kw = {"projection": "3d"}, figsize = (10, 5))
        tin = float(T[k])
        plt.suptitle('Solution at t = %1.3f s.' %tin)
        ax1.plot_trisurf(p[:, 0], p[:, 1], u_ap[:, k], triangles = tt, cmap = cm.coolwarm, linewidth = 0, antialiased = False)
        ax1.set_zlim([min_val, max_val])
        ax1.set_title('Approximation')
        ax2.plot_trisurf(p[:, 0], p[:, 1], u_ex[:, k], triangles = tt, cmap = cm.coolwarm, linewidth = 0, antialiased = False)
        ax2.set_zlim([min_val, max_val])
        ax2.set_title('Theoretical Solution')
        nok = nom + '_' + str(format(T[k], '.2f'))
        plt.savefig(nok + 's.png')
        plt.savefig(nok + 's.svg', format = 'svg')
        plt.close()

def Cloud_Transient_1(p, tt, u_ap, save = False, nom = ''):
    """
    Cloud_Transient_1

    This function graphs and saves the approximated and theoretical solutions of the problem being solved at several time levels.
    Both solutions are presented side by side to help perform graphical comparisons between both solutions.

    Input:
        p               ndarray         Array with the coordinates of the nodes.
        tt              ndarray         Array with the correspondence of the n triangles.
        u_ap            ndarray         Array with the computed solution.
        save            bool            Save the graphic.
                                        True: Save the created graphs.
                                        False: Don't save the created graphs (Default).
        nom             string          Name of the files to be saved to drive.
        
    Output:
        None
    """

    ## Variable initialization.
    t       = u_ap.shape[1]
    step    = max(1, t // 50)
    T       = np.linspace(0, 1, t)
    min_val = u_ap.min()
    max_val = u_ap.max()

    fig = plt.figure(figsize=(5, 5))
    ax1 = fig.add_subplot(111, projection='3d')
    
    if save:
        def update_plot(k):
            k = min(k, t - 1)
            ax1.clear()
            tin = float(T[k])
            fig.suptitle('Approximation at t = %1.3f s.' % tin)
            
            ax1.plot_trisurf(p[:, 0], p[:, 1], u_ap[:, k], triangles = tt, cmap = cm.coolwarm, linewidth = 0, antialiased = False)
            ax1.set_zlim([min_val, max_val])

            return fig, 
    
        ani = FuncAnimation(fig, update_plot, frames = np.arange(0, t+1, step), blit = True)
        ani.save(nom, writer = 'ffmpeg', fps = 10)
        plt.close()

    else:
        for k in np.arange(0, t, step):
            tin = float(T[k])
            fig.suptitle('Approximation at t = %1.3f s.' %tin)

            ax1.plot_trisurf(p[:, 0], p[:, 1], u_ap[:, k], triangles = tt, cmap = cm.coolwarm, linewidth = 0, antialiased = False)
            ax1.set_zlim([min_val, max_val])
            
            plt.pause(0.01)
            ax1.clear()
            
        tin = float(T[-1])
        fig.suptitle('Approximation at t = %1.3f s.' %tin)

        ax1.plot_trisurf(p[:, 0], p[:, 1], u_ap[:, -1], triangles = tt, cmap = cm.coolwarm, linewidth = 0, antialiased = False)
        ax1.set_zlim([min_val, max_val])
        
        plt.pause(0.1)
        plt.close()


def Cloud_Transient_Steps_1(p, tt, u_ap, nom):
    """
    Cloud_Transient_Steps_1

    This function graphs and saves the approximated solution of the problem being solved at three different time levels.

    Input:
        p               ndarray         Array with the coordinates of the nodes.
        tt              ndarray         Array with the correspondence of the n triangles.
        u_ap            ndarray         Array with the computed solution.
        nom             string          Name of the files to be saved to drive.
    
    Output:
        None
    """

    ## Variable initialization.
    t       = u_ap.shape[1]
    step    = max(1, t // 3)
    min_val = u_ap.min()
    max_val = u_ap.max()
    T       = np.linspace(0, 1, t)

    ## Create the graphs.
    for k in np.arange(0, t+1, step):
        if k >= t:
            k = t - 1
        fig = plt.figure(figsize=(5, 5))
        ax1 = fig.add_subplot(111, projection='3d')
        tin = float(T[k])
        plt.suptitle('Approximation at t = %1.3f s.' %tin)
        ax1.plot_trisurf(p[:, 0], p[:, 1], u_ap[:, k], triangles = tt, cmap = cm.coolwarm, linewidth = 0, antialiased = False)
        ax1.set_zlim([min_val, max_val])
        nok = nom + '_' + str(format(T[k], '.2f'))
        plt.savefig(nok + 's.png')
        plt.savefig(nok + 's.svg', format = 'svg')
        plt.close()


def Error(er):
    """
    Error

    This function graphs all the Quadratic Mean Errors computed between the approximated and theoretical solutions of the problem being solved.
    
    Input:
        er              ndarray         Array with the Quadratic Mean Error on each time step.
    
    Output:
        None
    """
    t = len(er)
    T = np.linspace(0,1,t)
    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(10, 4))

    ax1.plot(T, er)
    ax1.set_title('Linear')
    ax1.set(xlabel='Time Step', ylabel='Error')

    ax2.semilogy(T, er)
    ax2.set_title('Logarithmic')
    ax2.set(xlabel='Time Step', ylabel='Error')

    plt.suptitle('Quadratic Mean Error')
    plt.show()


def Error_sav(er,nom):
    """
    Error_sav

    This function graphs and saves all the Quadratic Mean Errors computed between the approximated and theoretical solutions of the problem being solved.
    The graphic is stored, as an image, on drive on the current path, or whatever path were provided on "nom".

    Input:
        er              ndarray         Array with the Quadratic Mean Error on each time step.
        nom             string          Name of the file to be saved to drive.
    
    Output:
        None
    """
    t = len(er)
    T = np.linspace(0,1,t)
    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(10, 4))
    
    ax1.plot(T, er)
    ax1.set_title('Linear')
    ax1.set(xlabel='Time Step', ylabel='Error')

    ax2.semilogy(T, er)
    ax2.set_title('Logarithmic')
    ax2.set(xlabel='Time Step', ylabel='Error')

    plt.suptitle('Quadratic Mean Error')

    plt.savefig(nom)
    plt.close()