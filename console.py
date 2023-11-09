#!/usr/bin/python3
"""This is the entry point for our command line and execution loop"""
import readline
import cmd
from models.base_model import BaseModel
import models


class HBNBCommand(cmd.Cmd):
    """Our class definition of the HBNB command line
    interface that is provided for single command shelling"""
    prompt = "(hbnb) "

    def __init__(self):
        """The magic init method for initializing attributes"""
        super().__init__()
        self.valid_classes = ["BaseModel"]
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

    def do_create(self, args):
        """command to crate some instance"""
        list_of_args = parse_arg(args)
        if len(list_of_args) == 0:
            print("** class name missing **")
        elif (list_of_args[0] not in self.valid_classes or
                len(list_of_args) > 1):
            print("** class doesn't exist **")
        else:
            bm_object = BaseModel()
            bm_object.save()
            print(bm_object.id)

    def do_show(self, args):
        """Command to print a given object based on the class name and id"""
        list_of_args = parse_arg(args)
        if len(list_of_args) == 0:
            print("** class name missing **")
        elif (list_of_args[0] not in self.valid_classes):
            print("** class doesn't exist **")
        elif len(list_of_args) == 1:
            print("** instance id is missing **")
        else:
            key = f"{list_of_args[0]}.{list_of_args[1]}"
            obj = self.dict_of_objects.get(key, None)
            if obj is None:
                print("** no instance found **")
            else:
                print(obj)

    def do_destroy(self, args):
        """ Method to destroy an instance with given id """
        list_of_args = parse_arg(args)
        if len(list_of_args) == 0:
            print("** class name missing **")
        elif (list_of_args[0] not in self.valid_classes):
            print("** class doesn't exist **")
        elif len(list_of_args) == 1:
            print("** instance id is missing **")
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
        list_of_args = parse_arg(args)
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

    def do_update(self, args):
        """The update command for updating a given instance using its id"""
        list_of_args = parse_arg(args)
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


if __name__ == "__main__":
    HBNBCommand().cmdloop()