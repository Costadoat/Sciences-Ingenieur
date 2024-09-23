from skspatial.objects import Plane
from skspatial.objects import Points
from skspatial.plotting import plot_3d
from mpl_toolkits.mplot3d.axes3d import Axes3D
from random import random
import matplotlib.pyplot as plt
import numpy as np
from numpy.linalg import norm
from scipy.optimize import leastsq

# Paramètre pour générer des défauts sur le cylindre
aleac=30

# Paramètre pour générer des défauts sur le plan
aleap=30

##################################################
####Générer le nuage de points####################

# Fonction permettant de générer un défaut sur le nuage de points
def alea(vect,percent):
    return [i*(1+((2*random()-1)*percent/100)) for i in vect]

# Génération du cylindre avec défaut

r=10
cyl_pt=[]
center=np.array([10,10,1])
for z in np.linspace(0,10,10):
    for theta in np.linspace(0,2*np.pi,20):
        cyl_pt.append(alea([r*np.cos(theta),r*np.sin(theta),z],aleac)+center)
cyl_pt=np.array(cyl_pt)

###################################################

plan_pt = [[0, 0, -5], [5, 15, -5], [-30, 30, -5], [15, -30, -5], [-10, 30, -5], [30, 30, -5]]

plan_pt = np.array([alea(pt,aleap) for pt in plan_pt])

#Fonction pour générer un cylindre à tracer à partir

def rotation_matrix(axis, theta):
    """
    Return the rotation matrix associated with counterclockwise rotation about
    the given axis by theta radians.
    """
    axis = np.asarray(axis)
    axis = axis / np.sqrt(np.dot(axis, axis))
    a = np.cos(theta / 2.0)
    b, c, d = -axis * np.sin(theta / 2.0)
    aa, bb, cc, dd = a * a, b * b, c * c, d * d
    bc, ad, ac, ab, bd, cd = b * c, a * d, a * c, a * b, b * d, c * d
    return np.array([[aa + bb - cc - dd, 2 * (bc + ad), 2 * (bd - ac)],
                     [2 * (bc - ad), aa + cc - bb - dd, 2 * (cd + ab)],
                     [2 * (bd + ac), 2 * (cd - ab), aa + dd - bb - cc]])


def cylindre_axe_z(center_x,center_y,alpha,beta,radius,height_z):
    """
    center_x, coordonnée en x du centre du cylindre
    center_y, coordonnée en y du centre du cylindre
    alpha, rotation (radian) autour de l'axe x (non implémenté)
    beta, rotation (radian) autour de l'axe y (non implémenté)
    radius, rayon du cylindre
    height_z, hauteur du cylindre
    """

    z = np.linspace(0, height_z, 50)
    theta = np.linspace(0, 2*np.pi, 50)
    theta_grid, z_grid=np.meshgrid(theta, z)
    x_grid = radius*np.cos(theta_grid)  + center_x
    y_grid = radius*np.sin(theta_grid) + center_y

    for i in range(len(x_grid)):
        for axis,theta in [[[1, 0, 0],alpha],[[0, 1, 0],beta]]:
            (x_grid[i],y_grid[i],z_grid[i])=np.dot(rotation_matrix(axis, theta), (x_grid[i],y_grid[i],z_grid[i]))
    return x_grid,y_grid,z_grid

#Fonction pour associer un cylindre idéal à un nuage de points

def cylinderFitting(xyz):

    """
    This is a fitting for a vertical cylinder fitting
    Reference:
    http://www.int-arch-photogramm-remote-sens-spatial-inf-sci.net/XXXIX-B5/169/2012/isprsarchives-XXXIX-B5-169-2012.pdf

    xyz is a matrix contain at least 5 rows, and each row stores x y z of a cylindrical surface
    p is initial values of the parameter;
    p[0] = Xc, x coordinate of the cylinder centre
    P[1] = Yc, y coordinate of the cylinder centre
    P[2] = alpha, rotation angle (radian) about the x-axis
    P[3] = beta, rotation angle (radian) about the y-axis
    P[4] = r, radius of the cylinder

    th, threshold for the convergence of the least squares

    """   
    x = xyz[:,0]
    y = xyz[:,1]
    z = xyz[:,2]


    p = np.array([x.mean(), y.mean(), 0,0, 10])

    fitfunc = lambda p, x, y, z: (- np.cos(p[3])*(p[0] - x) - z*np.cos(p[2])*np.sin(p[3]) - np.sin(p[2])*np.sin(p[3])*(p[1] - y))**2 + (z*np.sin(p[2]) - np.cos(p[2])*(p[1] - y))**2 #fit function
    errfunc = lambda p, x, y, z: fitfunc(p, x, y, z) - p[4]**2 #error function 
    try:
        est_p , success = leastsq(errfunc, p, args=(x, y, z), maxfev=1000000)
        
        return est_p
        
    except TypeError:
        return 0
        pass

def fitPlaneLTSQ(XYZ):
    (rows, cols) = XYZ.shape
    G = np.ones((rows, 3))
    G[:, 0] = XYZ[:, 0]  #X
    G[:, 1] = XYZ[:, 1]  #Y
    Z = XYZ[:, 2]
    (a, b, c),resid,rank,s = np.linalg.lstsq(G, Z,rcond=None)
    normal = (a, b, -1)
    nn = np.linalg.norm(normal)
    normal = normal / nn
    return (c, normal)


# Programme principal
if __name__=="__main__":

    fig = plt.figure()
    ax = Axes3D(fig)

    # Tracé du nuage de points (cylindre)
    ax = fig.add_subplot(111, projection='3d')
    ax.scatter(cyl_pt[:,0], cyl_pt[:,1], cyl_pt[:,2])
    
   
    print("Performing Cylinder Fitting ... ")
    est_p =  cylinderFitting(cyl_pt)
    print("Fitting Done!")
    print(" ")
    print("Estimated Parameters: ")
    print(est_p)

    # Tracé du cylindre des moindres carrés
    Xc,Yc,Zc = cylindre_axe_z(est_p[0],est_p[1],est_p[2],est_p[3],est_p[4],10)
    ax.plot_surface(Xc, Yc, Zc, alpha=0.5)

    # Calcul axe du cylindre des moindres carrés
    p1=center
    p2=center+np.array([0,0,15])
    alpha=est_p[2]
    p2=np.dot(np.array([[1,0,0],[0,np.cos(alpha),-np.sin(alpha)],[0,np.cos(alpha),-np.cos(alpha)]]),p2)
    alpha=est_p[3]
    p2=np.dot(np.array([[np.cos(alpha),0,-np.sin(alpha)],[0,1,0],[np.cos(alpha),0,-np.cos(alpha)]]),p2)
    print(p1,p2)


    # Tracé axe du cylindre des moindres carrés
    ax.plot([p1[0],p2[0]],[p1[1],p2[1]],[p1[2],p2[2]])

    # Recherche distance min max nuage de points, axe moindre carrés
    max=0
    min=est_p[4]
    for pt in cyl_pt:
        dist=norm(np.cross(p2-p1, p1-pt)) / norm(p2-p1)
        if dist>max:
            max=dist
        if dist<min:
            min=dist
    print('Défaut de forme:', max-min)

    # Tracé des cylindres tangents au nuage de points extérieurs et intérieurs des moindres carrés
    Xc,Yc,Zc = cylindre_axe_z(est_p[0],est_p[1],est_p[2],est_p[3],max,10)
    ax.plot_surface(Xc, Yc, Zc, alpha=0.5)
    Xc,Yc,Zc = cylindre_axe_z(est_p[0],est_p[1],est_p[2],est_p[3],min,10)
    ax.plot_surface(Xc, Yc, Zc, alpha=0.5)

    c,normal=fitPlaneLTSQ(plan_pt)
    point = np.array([0.0, 0.0, c])
    d = -point.dot(normal)

    # Tracé axe du cylindre des moindres carrés
    m=(p1+p2)/2
    p3=m+10*normal
    p4=m-10*normal
    ax.plot([p3[0],p4[0]],[p3[1],p4[1]],[p3[2],p4[2]])

    ax.scatter(plan_pt[:, 0], plan_pt[:, 1], plan_pt[:, 2])

    maxx = np.max(plan_pt[:,0])
    maxy = np.max(plan_pt[:,1])
    minx = np.min(plan_pt[:,0])
    miny = np.min(plan_pt[:,1])
    xx, yy = np.meshgrid([minx, maxx], [miny, maxy])
    z = (-normal[0]*xx - normal[1]*yy - d)*1. / normal[2]
    ax.plot_surface(xx, yy, z, alpha=0.2)

    # Recherche distance min max nuage de points, axe moindre carrés
    for pt in [p1,p2]:
        dist=norm(np.cross(p4-p3, p3-pt)) / norm(p4-p3)
        print(dist)
    


    ax.set_xlabel('x')
    ax.set_ylabel('y')
    ax.set_zlabel('z')
    plt.show()
