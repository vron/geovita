""" Tabular data of standard beam sections """

from collections import namedtuple

Section = namedtuple('Section', ['name','height', 'width', 'web', 'area', 'mass', 'Ix', 'Iy'])
""" A Section represents the data that can be queried for a given section """

_sections = {}

def _add(c, *args):
    c = c.strip()
    if _sections.get(c, None) is None:
        _sections[c] = {}
    _sections[c][args[0]] = Section(*args)

# Add HEA sections
_add("HEA", "100A",96,100,5,21.2,16.7,349,134)
_add("HEA", "120A",114,120,5,25.3,19.9,606,231)
_add("HEA", "140A",133,140,5.5,31.4,24.7,1030,389)
_add("HEA", "160A",152,160,6,38.8,30.4,1670,616)
_add("HEA", "180A",171,180,6,45.3,35.5,2410,925)
_add("HEA", "200A",190,200,6.5,53.8,42.3,3690,1340)
_add("HEA", "220A",210,220,7,64.3,50.5,5410,1950)
_add("HEA", "240A",230,240,7.5,76.8,60.3,7760,2770)
_add("HEA", "260A",250,260,7.5,86.8,68.2,10450,3670)
_add("HEA", "280A",270,280,8,97.3,76.4,13670,4760)
_add("HEA", "300A",290,300,8.5,112,88.3,18260,6310)
_add("HEA", "320A",310,300,9,124,97.6,22930,6990)
_add("HEA", "340A",330,300,9.5,133,105,27690,7440)

# Add HEB sections
_add("HEB", "100B",100,100,6,26,20.4,450,167)
_add("HEB", "120B",120,120,6.5,34,26.7,864,318)
_add("HEB", "140B",140,140,7,43,33.7,1510,550)
_add("HEB", "160B",160,160,8,54.3,42.6,2490,889)
_add("HEB", "180B",180,180,8.5,65.3,51.2,3830,1360)
_add("HEB", "200B",200,200,9,78.1,61.3,5700,2000)
_add("HEB", "220B",220,220,9.5,91,71.5,8090,2840)
_add("HEB", "240B",240,240,10,106,83.2,11260,3920)
_add("HEB", "260B",260,260,10,118,93,14920,5130)
_add("HEB", "280B",280,280,10.5,131,103,19270,6590)
_add("HEB", "300B",300,300,11,149,117,25170,860)
_add("HEB", "320B",320,300,11.5,161,127,30820,9240)
_add("HEB", "340B",340,300,12,171,134,36660,9690)


def section(section_class, section_name=None):
    """ Return section data about a given section in a given section_class.

    Args:
        section_class (str): The section class.
        section_name (str): Name of the section in the class.

    Returns:
        Section: the Section data or None if no such section is stored.
    """
    if _sections.get(section_class, None) is None:
        return None
    return _sections.get(section_class, None).get(section_name, None)

def list_classes():
    """ List all section classes for which there is data stored.

    Returns:
        list[str]: The list of section classes.
    """
    return list(_sections.keys())

def list_sections(section_class):
    """ List all sections available in a given section class

    Args:
        section_class (str): The section class.
        
    Returns:
        list[str]: the list of sections available in the section_class or None.
    """
    if _sections.get(section_class, None) is None:
        return []
    return list(_sections.get(section_class, None).keys())

if __name__ == "__main__":
    pass