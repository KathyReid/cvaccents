"""

Classes which help describe Accents and AccentDescriptors in Mozilla Common Voice speech data. 

Classes:

    Accent: used to describe an accent
    AccentDescriptor: used to describe an accent in granular qualitative terms, that are developer-defined. 

Functions:

    str(object) -> string

Misc variables:

    __version__



"""

"""
Accent represents an accent

This allows the Accent class to have as an attribute an list of AccentDescriptor objects which describe the Accent, facilitating one-to-many cardinality between Accents and AccentDescriptors, providing rich description of accents. 
"""


class Accent:

    # class attributes
    source = "Mozilla Common Voice"
    __version__ = 0.1

    def __init__(self, id, name, count, locale, descriptors):
        self.id = id
        self.name = name
        self.count = count
        self.locale = locale
        self.descriptors = descriptors
        self.predetermined = predetermined

    """
    Define a __str__ function to aid with debugging
    """

    def __str__(self):
        return f"id is {self.id}, name is {self.name}, count is {self.count}, locale is {self.locale}, descriptors are {self.descriptors}, predetermined is {self.predetermined}."


"""
Accent Descriptor is a class to represent the different ways in which an accent can be described. 
This allows the Accent class to have as an attribute an list of AccentDescriptor objects which describe the Accent.
This allows a one-to-many cardinality between Accents and AccentDescriptors.
"""


class AccentDescriptor:

    # class attributes

    def __init__(self, id, name, definition):
        self.id = id
        self.name = name
        self.definition = definition

    """
    Define a __str__ function to aid with debugging
    """

    def __str__(self):
        return f"id is {self.id}, name is {self.name}, definition is {self.definition}"
