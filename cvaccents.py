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


import json  # used for exporting data
import os  # used for file handling


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

    def __init__(
        self,
        id=0,
        name="Accent Name",
        count=0,
        locale=None,
        descriptors=None,
        predetermined=False,
    ):
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
        # TODO put a check in here to make sure it is an integer
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
            print("Something went wrong in updateStatus")
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
        # TODO put a check in here to make sure it is an string
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

        string = " ".join(str_list)

        return string

    def total(self):
        return len(self.AccentDict)

    def sortByCount(self, reverse=True):
        return dict(
            sorted(
                self.AccentDict.items(),
                key=lambda t: (t[1].count, t[1].name),
                reverse=reverse,
            )
        )

    def items(self):
        """
        Allows the Collection to be iterated like a Dict
        """
        return self.AccentDict.items()

    def updatePredeterminedStatus(self, predetermined_accents_list, status=True):

        try:
            for accent in self.AccentDict.items():
                print(accent)
                print(accent[0])

                for predetermined_accent in predetermined_accents_list:

                    if predetermined_accent == accent[1].name:
                        accent[1].updateStatus(status)
                        print("changed ", accent[1], "status to ", status)
                        # else do nothing - we don't want to update the predetermined_status of any other accents

            return True

        except Exception as e:
            print(e)
            print("Something went wrong in updatePredeterminedStatus")
            return False

    def reportNoneAccentDescriptors(self):
        """
        Used as a cross-check for Accents missing AccentDescriptors
        """
        try:
            missing_descriptors = []
            for accent in self.AccentDict.items():

                if not (accent[1]._descriptors):
                    missing_descriptors.append(accent)

            return missing_descriptors

        except Exception as e:
            print(e)
            print("Something went wrong in reportNoneAccentDescriptors")
            return False

    def reportPredeterminedAccents(self):
        """
        returns a list of predetermined Accents and their count of Accents in the AccentCollection
        TODO: I feel like there must be a simpler way to get this information from the AccentCollection class
        """

        try:
            predetermined_accents = []

            for idx, accent in enumerate(self.AccentDict.items()):
                if accent[1]._predetermined:
                    predetermined_accents.append([accent[1]._name, accent[1]._count])

            # order list by count
            predetermined_accents.sort(key=lambda a: a[1], reverse=True)
            return predetermined_accents

        except Exception as e:
            print(e)
            print("Something went wrong in reportPredeterminedAccents")
            return False

    def reportMultipleAccentDescriptors(self):
        """
        returns a list of Accent objects where the Accent object has > 1 Accent Descriptors
        This is to identify Accents that are described in multiple ways, e.g. "Kiwi" or "Received Pronunciation"
        TODO: I feel like there must be a simpler way to get this information from the AccentCollection class
        """

        try:
            multipleAccentDescriptors = []

            for idx, accent in enumerate(self.AccentDict.items()):
                if (len(accent[1]._descriptors) > 1):
                    print("more than two descriptors for: ", accent[1]._name)
                    multipleAccentDescriptors.append(accent)

            # no need to order the Dict
            return multipleAccentDescriptors

        except Exception as e:
            print(e)
            print("Something went wrong in reportMultipleAccentDescriptors")
            return False

    def reportAccentDescriptorCategories(self):
        """
        returns a list of AccentDescriptor categories and their count of Accents in the AccentCollection

        TODO: I think there's probably an easier way to do this too
        """

        try:
            accent_category_counts = []

            for idx, accent in enumerate(self.AccentDict.items()):
                for idxd, descriptor in enumerate(accent[1]._descriptors):

                    # check if this Accent Descriptor is already in accent_category_counts
                    # if not, add it, if so, increment the count
                    match = False
                    index = None

                    for idxc, accent_category in enumerate(accent_category_counts):
                        if accent_category[0] == descriptor._name:
                            match = True
                            index = idxc

                    if match:
                        accent_category_counts[index][1] += 1
                    else:
                        accent_category_counts.append([descriptor._name, 1])

            # order list by count
            accent_category_counts.sort(key=lambda a: a[1], reverse=True)

            return accent_category_counts

        except Exception as e:
            print(e)
            print("Something went wrong in reportAccentDescriptorCategories")
            return False

    def exportJSON(self, filePath):
        """
        Dump the AccentDict to JSON
        """

        # check that the given filePath is valid
        try:
            os.path.exists(filePath)
        except Exception as e:
            print(e)
            print("Something went wrong in exportJSON")
            return False
        else:
            with open(filePath, "w") as outfile:
                json.dump(self.AccentDict, outfile, cls=AccentEncoder)
            return True


class AccentEncoder(json.JSONEncoder):
    def default(self, obj):
        if isinstance(obj, Accent):

            # call out to a private method
            # otherwise the encoder doesn't know how to handle the AccentDescripor object
            accentDescriptors = AccentEncoder._encodeAccentDescriptor(obj._descriptors)

            data = {
                "id": obj._id,
                "name": obj._name,
                "count": obj._count,
                "locale": obj._locale,
                "descriptors": accentDescriptors,
                "predetermined": obj._predetermined,
            }
            return data
        else:
            type_name = obj.__class__.__name__
            raise TypeError(f"Unexpected type {type_name}")

        return json.JSONEncoder.default(self, obj)

    def _encodeAccentDescriptor(descriptors):
        # descriptors should be a list of AccentDescriptor objects
        for descriptor in descriptors:
            data = {}
            if isinstance(descriptor, AccentDescriptor):
                data[descriptor._id] = {
                    "id": descriptor._id,
                    "name": descriptor._name,
                    "definition": descriptor._definition,
                    "parent": descriptor._parent,
                }
            else:
                type_name = descriptors.__class__.__name__
                raise TypeError(f"Unexpected type {type_name}")
        return data
