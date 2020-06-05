import math

from gvlib.crosssection import inertia 

def test_pipe():
    assert abs(inertia.pipe(0.25, 0.01) - 0.000054381) < 1e-5

def test_cylinder():
    assert abs(inertia.cylinder(0.5) - math.pow(0.25,4)*math.pi/4) < 1e-5
