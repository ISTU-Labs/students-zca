from zope.interface import Interface

class IStorage(Interface):
    """This interface defines database (storage) functions
    to persistently store component data.
    """
    def store(obj):
        """Stores the object in a storage."""

    def get(id):
        """Retrive the object by its id from
        a storage."""

class ISQLiteStorage(IStorage):
    pass

class ISQLiteStorageAdapter:
    def store(storage):
        """Stores self in the storage.
        Return an indentifier of the stored object.
        """
    def get(storage, id):
        """Constructs object from stored data identified
        by id"""
