#!/usr/bin/python3
""" Create, Base, the base of all other classes """

import os.path
import json


class Base:
    """ base” of all other classes """
    __nb_objects = 0

    def __init__(self, id=None):
        self.id = id

    @property
    def id(self):
        """ Method that returns the id of the Base """
        return self.__id

    @id.setter
    def id(self, value):
        if value is None:
            Base.__nb_objects += 1
            self.__id = Base.__nb_objects
        else:
            self.__id = value

    @staticmethod
    def to_json_string(list_dictionaries):
        new_list = []
        if list_dictionaries:
            for atribu in list_dictionaries:
                new_list. append(atribu)
        return (json.dumps(new_list))

    @classmethod
    def save_to_file(cls, list_objs):
        list_from = []
        with open("{}.json".format(cls.__name__), "w") as file:
            if (list_objs):
                for obj in list_objs:
                    obj_dict = obj.to_dictionary()
                    list_from.append(obj_dict)
            file.write(cls.to_json_string(list_from))

    @staticmethod
    def from_json_string(json_string):
        if (json_string):
            return (json.loads(json_string))
        return ([])

    @classmethod
    def create(cls, **dictionary):
        if cls.__name__ == "Rectangle":
            new = cls(1, 1)
        elif cls.__name__ == "Square":
            new = cls(1)
        new.update(**dictionary)
        return (new)

    @classmethod
    def load_from_file(cls):
        """load_from_file"""
        a = []
        if os.path.exists('./{}.json'.format(cls.__name__)):
            with open('{}.json'.format(cls.__name__), 'r') as f:
                return [cls.create(**i) for i in
                        cls.from_json_string(f.read())]
        else:
            return a

    @classmethod
    def save_to_file_csv(cls, list_objs):
        """ Writes a CVS representation of list_objs
        """
        filename = "{}.csv".format(cls.__name__)
        new_list = []

        if list_objs is not None:
            for instance in list_objs:
                new_list.append(cls.to_dictionary(instance))

        with open(filename, 'w', encoding='utf-8') as f:
            f.write(cls.to_json_string(new_list))

    @classmethod
    def load_from_file_csv(cls):
        """ Returns a list of instances
        """
        filename = "{}.csv".format(cls.__name__)
        instance_list = []

        try:
            with open(filename, 'r', encoding='utf-8') as f:
                file_strs = cls.from_json_string(f.read())

            for instance in file_strs:
                instance_list.append(cls.create(**instance))

        except FileNotFoundError:
            pass

        return 
