import numpy as np
from humpday.coordinates import coords
from humpday.coordinates import rotate
from deap.benchmarks import h1
import math
from humpday.plotting import mesh2d_


def hump(xs,j):
    """ Loosely based on h1 function """
    origin = 0,0
    xs_rotated = rotate(origin=origin,point=xs,angle=j*math.pi/2)
    xs_dilated = [ (x*100) for i,x in enumerate(xs_rotated)]
    return -h1(individual=xs_dilated)[0]+0.0005*np.linalg.norm(xs_dilated)


def dilated_hump(xs,j):
    """ Loosely based on h1 function """
    origin = 0,0
    xs_rotated = rotate(origin=origin,point=xs,angle=j*math.pi/2)
    xs_dilated = [ (x*100)*(i+1) for i,x in enumerate(xs_rotated)]
    return -h1(individual=xs_dilated)[0]+0.0005*np.linalg.norm(xs_dilated)

def hump_selector(xs,zs,ws,offset):
    """ Finds nearest center and returns hump function
       xs position in plane
       zs listing of centers of humps
       ws weights of humps
       offset
    """
    centers = coords( zs, 2)
    ys = [ xs-c+offset for c in centers ]
    distances = [ (np.linalg.norm(ys_),i) for i, ys_ in enumerate(ys) ]
    sort_dist = sorted(distances,reverse=False)
    i_close = sort_dist[0][1]
    y = ys[i_close]
    w = ws[i_close]
    return w*hump(y,j=i_close)




if __name__=='__main__':
    ws = np.array([1.0,2.0,1.3])
    zs = np.array([0.25, 0.25, -0.25, -0.25, 0.15, -0.11])
    offset = (0,0)
    mesh2d_(hump_selector,zs,ws,offset)