import math

from gvlib.crosssection.section import section 

def test_heb_sample():
    assert section("HEB", "200B").web == 9
