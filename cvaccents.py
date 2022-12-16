"""
Classes which help describe Accents and AccentDescriptors in Mozilla Common Voice speech data. 

Classes:
    Accent: used to describe an accent
    AccentDescriptor: used to describe an accent in granular qualitative terms, that are developer-defined. 

Functions:
    __str__(object) -> string

Misc variables:
    __version__

"""


class Accent:
    """
    Accent represents an accent of a language.
    This allows the Accent class to have as an attribute an list of AccentDescriptor objects,
    which describe the Accent,facilitating one-to-many cardinality between Accents and AccentDescriptors,
    providing rich description of accents.


    Parameters
    ----------
    id: integer
        A unique identifier of the Accent, suitable for using as a hashable index
    name: string
        A text description of the Accent, which is user-defined, such as from Mozilla CV data
    count: integer
        A count of the occurrences of the Accent, which is user-defined, such as from Mozilla CV data
    locale: string
        A descriptor of the language or locale of the Accent.
        The format of the descriptor is not defined, as it may be a language with many accents and locales,
        such as 'en', or may be a locale-specific variant of a language with its own accents - 'pt-BR'.
        This is user-defined based on context.
    descriptors: list of AccentDescriptor objects
        A list of AccentDescriptor objects describing the accent.


    Attributes
    ----------
    source: string
        The source of the Accent data, aimed with re-usability in mind.
    __version__: float
        Representation of the version number of the Class.

    """

    # class attributes
    source = "Mozilla Common Voice"
    __version__ = 0.1

    def __init__(self, id=0, name="Accent Name", count=0, locale=None, descriptors=None, predetermined=False):
        self.id = id
        self.name = name
        self.count = count
        self.locale = locale
        self.descriptors = descriptors
        self.predetermined = predetermined

    """
    Return a human-readable string representation of the object's values. 

        Parameters
        ----------

        Raises
        ------


        Returns
        -------
        string
    """

    def __str__(self):
        return f"id is {self.id}, name is {self.name}, count is {self.count}, locale is {self.locale}, descriptors are {self.descriptors}, predetermined is {self.predetermined}."


class AccentDescriptor:
    """
    Accent represents an accent of a language.
    This allows the Accent class to have as an attribute an list of AccentDescriptor objects,
    which describe the Accent,facilitating one-to-many cardinality between Accents and AccentDescriptors,
    providing rich description of accents.


    Parameters
    ----------
    id: integer
        A unique identifier of the AccentDescriptor, suitable for using as a hashable index
    name: string
        A text description of the AccentDescriptor, which is user-defined, such as from Mozilla CV data
    definition: string
        A text definition of the AccentDescriptor and how it should be applied,
        which is user-defined, such as from Mozilla CV data
    category: string
        A text category of the AccentDescriptor, which is user-defined,
        and may be, for example, a linguistic category such as 'Rhoticity'.


    Attributes
    ----------

    """

    # class attributes

    def __init__(self, id, name, definition, category):
        self.id = id
        self.name = name
        self.definition = definition
        self.category = category

    """
    Define a __str__ function to aid with debugging
    """

    def __str__(self):
        return f"id is {self.id}, name is {self.name}, definition is {self.definition}, category is {self.category}"
    
class AccentCollection: 
    """
    Accent represents a collection of Accent objects. 
    This allows for the definition of methods and attributes at a collection level. 
    For example, you may wish to store each language's Accents in a different Accent Collection. 


    Parameters
    ----------
    AccentDict: dict
        A dict of Accent objects


    Attributes
    ----------

    """
    
    def __init__(self, AccentDict):
        self.AccentDict = AccentDict
        
    def __str__(self): 
        for accent in self.AccentDict.items(): 
            print(accent[1].__str__()) # this leverages the __str__ method of Accent class
    
    def total(self): 
        return len(self.AccentDict)
    
    def sortByCount(self, reverse=True): 
        return dict(sorted(self.AccentDict.items(), key=lambda t:(t[1].count, t[1].name), reverse=reverse))
    
    def dummy(self):
        return "dummy function"

  