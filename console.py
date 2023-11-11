#!/usr/bin/python3
"""This is the entry point for our command line and execution loop
This module contains the class definiton of the HBNB """

import readline
import cmd
from models.base_model import BaseModel
from models.user import User
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.review import Review
import models
import re


class HBNBCommand(cmd.Cmd):
    """Our class definition of the HBNB command line
    interface that is provided for single command shelling"""
    prompt = "(hbnb) "

    def __init__(self):
        """The magic init method for initializing attributes"""
        super().__init__()
        self.valid_classes = {
                "BaseModel": BaseModel,
                "User": User,
                "State": State,
                "City": City,
                "Amenity": Amenity,
                "Place": Place,
                "Review": Review}
        self.storage = models.storage  # storage is already reloaded.
        self.dict_of_objects = self.storage.all()

    def emptyline(self):
        """Method overriden to deal with empty lines appropriately."""
        pass

    def do_quit(self, arg):
        """Quit command to exit the program"""
        return True

    def do_EOF(self, line):
        """EOF command to quit the commadnline Ctrl + D"""
        # print()
        return True

    def onecmd(self, line):
        """ The onecmd module that executes a given line"""
        self_cmd_dict = {
                "all": self.do_all,
                "count": self.do_count,
                "show": self.do_show,
                "destroy": self.do_destroy,
                "update": self.do_update
                }
        list_of_cmd = parse_arg(line)
        try:
            cmd = list_of_cmd[0]
        except IndexError:
            cmd = "Invalid"
        if "." in cmd and "(" in cmd:
            list_of_cmd_attr = parse_dot_command(line)
            try:
                cmd = list_of_cmd_attr.pop(1)
            except IndexError:
                cmd = "Invalid"
            # args = " ".join(list_of_cmd_attr)  You won't need this eventua
            function = self_cmd_dict.get(cmd, None)
            if function is None:
                r = super(HBNBCommand, self).onecmd(line)
            else:
                function(list_of_cmd_attr)
            r = False
        else:
            r = super(HBNBCommand, self).onecmd(line)
        return r

    def do_create(self, args):
        """command to crate some instance: This create will
        accept some class (either BaseModel or other specified class
        and will output the id of the newly created object"""
        if type(args) == str:
            list_of_args = parse_arg(args)
        elif type(args) == list:
            list_of_args = args[:]
        if len(list_of_args) == 0:
            print("** class name missing **")
        elif (list_of_args[0] not in self.valid_classes or
                len(list_of_args) > 1):
            print("** class doesn't exist **")
        else:
            Class_of_object = self.valid_classes.get(list_of_args[0])
            any_object = Class_of_object()
            any_object.save()
            print(any_object.id)

    def do_show(self, args):
        """Command to print a given object based on the class name and id"""
        if type(args) == str:
            list_of_args = parse_arg(args)
        elif type(args) == list:
            list_of_args = args[:]
        if len(list_of_args) == 0:
            print("** class name missing **")
        elif (list_of_args[0] not in self.valid_classes):
            print("** class doesn't exist **")
        elif len(list_of_args) == 1:
            print("** instance id missing **")
        else:
            key = f"{list_of_args[0]}.{list_of_args[1]}"
            obj = self.dict_of_objects.get(key, None)
            if obj is None:
                print("** no instance found **")
            else:
                print(obj)

    def do_destroy(self, args):
        """ Method to destroy an instance with given id """
        if type(args) == str:
            list_of_args = parse_arg(args)
        elif type(args) == list:
            list_of_args = args[:]
        if len(list_of_args) == 0:
            print("** class name missing **")
        elif (list_of_args[0] not in self.valid_classes):
            print("** class doesn't exist **")
        elif len(list_of_args) == 1:
            print("** instance id missing **")
        else:
            key = f"{list_of_args[0]}.{list_of_args[1]}"
            obj = self.dict_of_objects.get(key, None)
            if obj is None:
                print("** no instance found **")
            else:
                models.storage.delete_instance(key)
                models.storage.save()

    def do_all(self, args):
        """The command for showing all instances or instances of a class"""
        if type(args) == str:
            list_of_args = parse_arg(args)
        elif type(args) == list:
            list_of_args = args[:]
        if len(list_of_args) == 0:
            list_of_prints = []
            for obj in self.dict_of_objects.values():
                list_of_prints.append(obj.__str__())
            print(list_of_prints)
        else:
            list_of_prints = []
            if list_of_args[0] not in self.valid_classes:
                print("** class doesn't exist **")
            else:
                for key, value in self.dict_of_objects.items():
                    if key.startswith(list_of_args[0]):
                        list_of_prints.append(value.__str__())
                print(list_of_prints)

    def do_count(self, args):
        """The command for showing all instances or instances of a class"""
        if type(args) == str:
            list_of_args = parse_arg(args)
        elif type(args) == list:
            list_of_args = args[:]
        if len(list_of_args) == 0:
            count_of_instances = 0
            for obj in self.dict_of_objects.values():
                count_of_instances += 1
            print(count_of_instances)
        else:
            count_of_instances = 0
            if list_of_args[0] not in self.valid_classes:
                print("** class doesn't exist **")
            else:
                for key, value in self.dict_of_objects.items():
                    if key.startswith(list_of_args[0]):
                        count_of_instances += 1
                print(count_of_instances)

    def do_update(self, args):
        """The update command for updating a given instance using its id"""
        if type(args) == str:
            list_of_args = parse_arg(args)
        elif type(args) == list:
            list_of_args = args[:]
        # Let us try with updating with dict_of_objects...
        if len(list_of_args) == 0:
            print("** class name missing **")
        elif list_of_args[0] not in self.valid_classes:
            print("** class doesn't exist **")
        elif len(list_of_args) == 1:
            print("** instance id missing **")
        elif (f"{list_of_args[0]}.{list_of_args[1]}" not in
                list(self.dict_of_objects.keys())):
            print("** no instance found **")
        elif len(list_of_args) == 2:
            print("** attribute name missing **")
        elif len(list_of_args) == 3:
            print("** value missing **")
        else:
            key = f"{list_of_args[0]}.{list_of_args[1]}"
            obj = self.dict_of_objects.get(key)
            attr_name = list_of_args[2]
            try:
                attr_value = eval(list_of_args[3])
            except (NameError, SyntaxError):
                attr_value = list_of_args[3]
            setattr(obj, attr_name, attr_value)
            models.storage.save()


def parse_arg(str_cmd):
    """Function that parses the string command"""
    l_cmd = []
    characters = ""
    within_quotes = False
    for char in str_cmd:
        if char == "\"" or within_quotes:
            if char == "\"" and within_quotes:
                within_quotes = False
                l_cmd.append(characters)
                characters = ""
                continue
            elif char == "\"":
                within_quotes = True
                continue
            else:
                characters += char
        elif not within_quotes and (char == " " or char == "\n"):
            l_cmd.append(characters)
            characters = ""
        else:
            characters = characters + char
    if characters != "":
        l_cmd.append(characters)
    # remove idle words or arguments
    new_list = []
    for chars in l_cmd:
        if chars:
            new_list.append(chars)
    return new_list


def parse_dot_command(str_cmd):
    """Function that parses the string command"""
    l_cmd = []
    characters = ""
    split_string = ".,( )"
    within_quotes = False
    for char in str_cmd:
        if char == "\"" or within_quotes:
            if char == "\"" and within_quotes:
                within_quotes = False
                l_cmd.append(characters)
                characters = ""
                continue
            elif char == "\"":
                within_quotes = True
                continue
            else:
                characters += char
        elif not within_quotes and (char in split_string or char == "\n"):
            l_cmd.append(characters)
            characters = ""
        else:
            characters = characters + char
    if characters != "":
        l_cmd.append(characters)
    # remove idle words or arguments
    new_list = []
    for chars in l_cmd:
        if chars:
            new_list.append(chars)
    return new_list


def split_dot_command(command_str):
    """Function to split dot commands """
    list_of_cmd_attr = re.split(r"[.,\(\s+\)]", command_str)
    return list_of_cmd_attr


if __name__ == "__main__":
    HBNBCommand().cmdloop()
