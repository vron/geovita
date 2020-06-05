""" Calculates area moment of inertia of standard shapes. """

import math

def cylinder(D):
    """ Calculate the area moment of inertia of a cylinder.

    Args:
        D (float): diameter of the cylinder.

    Returns:
        float: the area moment of inertia.
    """

    return pipe(D, D/2.0)
    
def pipe(outer_D, t):
    """ Calculate the area moment of inertia of a pipe.

    Args:
        outer_S (float): outer diameter of the pipe.
        t (float): thickness of the pipe wall.

    Returns:
        float: the area moment of inertia.
    """

    if t < 0.0 or t*2>outer_D:
        raise ValueError("wall thickness must be in range [0,D/2]")
    r = outer_D / 2.0
    rh = r - t
    return math.pi / 4.0 * (math.pow(r, 4) - math.pow(rh, 4))
