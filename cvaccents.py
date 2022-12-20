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
    predetermined: Boolean
        Whether the accent was predetermined in the data contributor's Common Voice profile. 
        False indicates the accent is self-specified. 


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
        self._id = id
        self._name = name
        self._count = count 
        self._locale = locale 
        self._descriptors = descriptors 
        self._predetermined = predetermined
        
        
    @property
    def id(self):
        return self._id
    
    @property
    def name(self):
        return self._name
    
    @property
    def count(self):
        return self._count
    
    @property
    def locale(self):
        return self._locale
    
    @property
    def descriptors(self):
        return self._descriptors
    
    @property
    def predetermined(self):
        return self.predetermined
    
    @id.setter
    def id(self, value):
        # TODO put a check in here to make sure it is an integer
        self._id = value
        
    @name.setter
    def name(self, value):
        # TODO put a check in here to make sure it is a string
        self._name = value
        
    @count.setter
    def count(self, value):
        #TODO put a check in here to make sure it is an integer
        self._count = value
        
    @count.setter
    def locale(self, value):
        # TODO put a check in here to make sure it is a string
        # I don't want to restrict it to say ISO-639 values
        # because the user may want to implement locale as say BCP-47
        self._locale = value
        
    @count.setter
    def descriptors(self, value):
        # TODO put a check in here to make sure it is a list of AccentDescriptor objects
        self._descriptors = value
        
    @count.setter
    def predetermined(self, value):
        # TODO put a check in here to make sure it is a Boolean value 
        self._predetermined = value
        
        
        
        

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
        string = f"id is {self._id}, name is {self._name}, count is {self._count}, locale is {self._locale}, descriptors are {self._descriptors}, predetermined is {self._predetermined}."
        return string
    
    def updateStatus(self, status): 
        """
        Update predetermined_status
        """
    
        try: 
            self._predetermined = status
        except Exception as e:
            print(e) 
            print('Something went wrong in updateStatus')
            return False
        else: 
            return True
          

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
    parent: integer 
        An id of another category that allows for parent-child relationships. 
        None if the Category is itself a parent. 


    Attributes
    ----------

    """

    # class attributes
    # None

    def __init__(self, id, name, definition, parent):
        self._id = id
        self._name = name
        self._definition = definition
        self._parent = parent 
        
        
    @property
    def id(self):
        return self._id
    
    @property
    def name(self):
        return self._name
    
    @property
    def definition(self):
        return self._definition
    
    @property
    def parent(self):
        return self._parent
    
    @id.setter
    def id(self, value):
        # TODO put a check in here to make sure it is an integer
        self._id = value
        
    @name.setter
    def name(self, value):
        # TODO put a check in here to make sure it is a string
        self._name = value
        
    @definition.setter
    def definition(self, value):
        #TODO put a check in here to make sure it is an string
        self._definition = value
        
    @parent.setter
    def parent(self, value):
        # TODO put a check in here to make sure it is an integer
        self._parent = value
        
    """
    Define a __str__ function to aid with debugging
    """

    def __str__(self):
        return f"id is {self._id}, name is {self._name}, definition is {self._definition}, parent is {self._parent}" 

    
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
        
        str_list = []
        
        for accent in self.AccentDict.items(): 
            str_list.append(accent[1].__str__())
            
        string = (' '.join(str_list))

        return (string)
    
    def total(self): 
        return len(self.AccentDict)
    
    def sortByCount(self, reverse=True): 
        return dict(sorted(self.AccentDict.items(), key=lambda t:(t[1].count, t[1].name), reverse=reverse))
    
    def items(self): 
        """
        Allows the Collection to be iterated like a Dict
        """ 
        return self.AccentDict.items()
        
    
    
    """
    Return a human-readable string representation of the object's values. 

    Parameters
    ----------
    
    predetermined_accents_list: list
        A list of strings representing the accents that should be marked as predetermined

    Raises
    ------


    Returns
    -------
    Boolean
        True on success
        False on failure
    """
    def updatePredeterminedStatus(self, predetermined_accents_list, status=True): 
        
        try: 
            for accent in self.AccentDict.items(): 
                print(accent)
                print(accent[0])
    
                for predetermined_accent in predetermined_accents_list: 
        
                    if (predetermined_accent == accent[1].name) :
                        accent[1].updateStatus(status)
                        print ('changed ', accent[1], 'status to ', status)
                        # else do nothing - we don't want to update the predetermined_status of any other accents 
                        
            return True
        
        except Exception as e:
            print(e) 
            print('Something went wrong in updatePredeterminedStatus')
            return False
    
  