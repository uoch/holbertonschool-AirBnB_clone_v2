#!/usr/bin/python3
"""This module defines a class to manage file storage for hbnb clone"""
import json


class FileStorage:
    """This class manages storage of hbnb models in JSON format"""
    __file_path = 'file.json'
    __objects = {}
    
    def all(self, cls=None):
        """Returns a dictionary of models currently in storage"""
        if cls is not None:
            """return {k: v for k, v in self.__objects.items() if isinstance(v, cls)}"""
            lis = {}
            for k, v in self.__objects.items():
                if isinstance(v, cls):
                    lis[k] = v
            return lis
        else:
            return self.__objects
    def new(self, obj):
        """Adds new object to storage dictionary"""
        self.all().update({obj.to_dict()['__class__'] + '.' + obj.id: obj})

    def save(self):
        """ serializes __objects to the JSON file"""
        with open(self.__file_path, 'w', encoding='utf-8') as f:
            temp = {}
            temp.update(FileStorage.__objects)
            for key, val in temp.items():
                temp[key] = val.to_dict()
            json.dump(temp, f)
    def reload(self):
        """Loads storage dictionary from file"""
        from models.base_model import BaseModel
        from models.user import User
        from models.place import Place
        from models.state import State
        from models.city import City
        from models.amenity import Amenity
        from models.review import Review

        classes = {
                    'BaseModel': BaseModel, 'User': User, 'Place': Place,
                    'State': State, 'City': City, 'Amenity': Amenity,
                    'Review': Review
                  }
        try:
            temp = {}
            with open(FileStorage.__file_path, 'r') as f:
                temp = json.load(f)
                for key, val in temp.items():
                    self.all()[key] = classes[val['__class__']](**val)
        except FileNotFoundError:
            pass
    def delete(self, obj=None):
        """Deletes an object from the storage"""
        if obj is None:
            return
        else:
            delme = None
            for key, value in self.__objects.items():
                if value == obj:
                    delme = key
                    break
            if delme is not None:
                del self.__objects[delme]
                self.save()