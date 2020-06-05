""" Example script that prints some data about a particular HEB beam, illustrating 
how to import functions from the geovita library """

from gvlib.crosssection.section import section

if __name__ == "__main__":
    print("HEB:", section("HEB", "200B"))
    pass