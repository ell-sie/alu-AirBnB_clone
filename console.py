#!/usr/bin/python3
""" console of the base unit """

import cmd
import models
import json
import shlex
from models.base_model import BaseModel
from models.user import User
from models.city import City
from models.place import Place
from models.state import State
from models.review import Review
from models.amenity import Amenity


class HBNBCommand (cmd.Cmd):
    """ Access point to command interpreter on console"""
    prompt = '(hbnb)'
myclass_dict = {"BaseModel": BaseModel, "User": User, "State": State,
                "City": City, "Amenity": Amenity, "Place": Place,
                "Review": Review}


def do_nothing(self, arg):
        """ Does nothing """
        return True


def do_quit(self, arg):
        """ Exits the program and saves safely data """
        return True


def do_EOF(self, arg):
        """ Exits the command console"""
        return True


def emptyline(self):
        """ Overrides the empty line method """
        return True


def do_create(self, arg):
        """ Creates a new instance of the basemodel class in JSON"""
        if not arg:
            print("** class name missing **")
            return
        my_data = shlex.split(arg)
        if my_data[0] not in HBNBCommand.myclass_dict.keys():
            print("** class doesn't exist **")
            return
        new_instance = HBNBCommand.myclass_dict[my_data[0]]()
        new_instance.save()
        print(new_instance.id)


def do_show(self, arg):
        """Prints the string representation of an instance
        based on the class name and id"""
        tokens = shlex.split(arg)
        if len(tokens) == 0:
            print("** class name missing **")
            return
        if tokens[0] not in HBNBCommand.myclass_dict.keys():
            print("** class doesn't exist **")
            return
        if len(tokens) <= 1:
            print("** instance id missing **")
            return
        models.storage.reload()
        for key, value in models.storage.all().items():
            if value.__class__.__name__ == tokens[0] \
               and value.id == tokens[1]:
                print(value.__str__())
                return
            print("** no instance found **")


def do_destroy(self, arg):
        """
        Deletes an instance based on the class name and id
        """
        tokens = shlex.split(arg)
        if len(tokens) == 0:
            print("** class name missing **")
            return
        if tokens[0] not in HBNBCommand.myclass_dict.keys():
            print("** class doesn't exist **")
            return
        if len(tokens) <= 1:
            print("** instance id missing **")
            return
        models.storage.reload()
        objs_dict = models.storage.all()
        key = tokens[0] + "." + tokens[1]
        if key in objs_dict:
            del objs_dict[key]
            models.storage.save()
        else:
            print("** no instance found **")


def do_all(self, arg):
        """
        Prints all string representation of all instances
        based or not on the class name
        """
        if arg:
            if arg not in HBNBCommand.myclass_dict.keys():
                print("** class doesn't exist **")
                return

        for key_items in models.storage.all().keys():
            key_items = models.storage.all()[key_items]
            print(key_items)
        return


def do_update(self, arg):
        """
        Updates an instance based on the class name and
        id by adding or updating attribute
        (save the change into the JSON file).
        """
        if not arg:
            print("** class name missing **")
            return
        my_data = shlex.split(arg)
        models.storage.reload()
        objs_dict = models.storage.all()
        if my_data[0] not in HBNBCommand.myclass_dict.keys():
            print("** class doesn't exist **")
            return
        if (len(my_data) == 1):
            print("** instance id missing **")
            return
        try:
            key = my_data[0] + "." + my_data[1]
            objs_dict[key]
        except KeyError:
            print("** no instance found **")
            return
        if (len(my_data) == 2):
            print("** attribute name missing **")
            return
        if (len(my_data) == 3):
            print("** value missing **")
            return
        my_instance = objs_dict[key]
        if hasattr(my_instance, my_data[2]):
            data_type = type(getattr(my_instance, my_data[2]))
            setattr(my_instance, my_data[2], data_type(my_data[3]))
        else:
            setattr(my_instance, my_data[2], my_data[3])
        models.storage.save()


def do_update2(self, arg):
        """
        Updates an instance based on the class name and
        id by adding or updating attribute
        (save the change into the JSON file).
        Structure: update [class name] [id] [dictionary]
        """
        if not arg:
            print("** class name missing **")
            return
        my_dictionary = "{" + arg.split("{")[1]
        my_data = shlex.split(arg)
        models.storage.reload()
        objs_dict = models.storage.all()
        if my_data[0] not in HBNBCommand.myclass_dict.keys():
            print("** class doesn't exist **")
            return
        if (len(my_data) == 1):
            print("** instance id missing **")
            return
        try:
            key = my_data[0] + "." + my_data[1]
            objs_dict[key]
        except KeyError:
            print("** no instance found **")
            return
        if (my_dictionary == "{"):
            print("** attribute name missing **")
            return

        my_dictionary = my_dictionary.replace("\'", "\"")
        my_dictionary = json.loads(my_dictionary)
        my_instance = objs_dict[key]
        for my_key in my_dictionary:
            if hasattr(my_instance, my_key):
                data_type = type(getattr(my_instance, my_key))
                setattr(my_instance, my_key, my_dictionary[my_key])
            else:
                setattr(my_instance, my_key, my_dictionary[my_key])
        models.storage.save()


def do_count(self, arg):
        """
        Counts number of instances of a class
        """
        counter = 0
        objects_dict = models.storage.all()
        for key in objects_dict:
            if (arg in key):
                counter += 1
        print(counter)


def default(self, arg):
        """ handle new ways of inputing data and Retrieve all instances class using: <class name>.all() """
        count = 0
        words = arg.split(".")

        if words[0] in myclass_dict and words[1] == "all()":
            self.do_all(words[0])
        elif words[0] in myclass_dict and words[1] == "count()":
            if (words[0] not in myclass_dict):
                print("** class doesn't exist **")
                return (False)
            else:
                for key in models.storage.all():
                    if key.startswith(words[0]):
                        count += 1
                print(count)
        else:
            print("*** Unknown syntax: {}".format(inp))


if __name__ == '__main__':
    HBNBCommand().cmdloop()
