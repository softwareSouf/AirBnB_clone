#!/usr/bin/python3
import uuid
from datetime import datetime

class BaseModel:
    """
    	BaseModel class defines common attributes/methods for other classes. """

    def __init__(self):
        """
        Initialize a new BaseModel instance.

        Public instance attributes:
            id: string - assigned with a UUID when an instance is created
            created_at: datetime - assigned with the current datetime when an instance is created
            updated_at: datetime - assigned with the current datetime when an instance is created and updated as needed
        """
        self.id = str(uuid.uuid4())
        self.created_at = datetime.now()
        self.updated_at = datetime.now()

    def __str__(self):
        """
        Return a string representation of the BaseModel instance.

        Format: "[<class name>] (<self.id>) <self.__dict__>"
        """
        return "[{}] ({}) {}".format(self.__class__.__name__, self.id, self.__dict__)

    def save(self):
        """
        Update the public instance attribute 'updated_at' with the current datetime.
        """
        self.updated_at = datetime.now()

    def to_dict(self):
        """
        Convert the BaseModel instance to a dictionary.

        Returns:
            dict: A dictionary containing keys/values of __dict__ of the instance
                  with the class name and formatted date strings.
        """
        obj_dict = self.__dict__.copy()
        obj_dict['__class__'] = self.__class__.__name__
        obj_dict['created_at'] = self.created_at.isoformat()
        obj_dict['updated_at'] = self.updated_at.isoformat()
        return obj_dict

