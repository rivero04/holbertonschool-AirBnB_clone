#!/usr/bin/python3
"""
This is the consolation module. Provides a command line interface to interact with the program.
"""

import cmd
from models.base_model import BaseModel
from models import storage

class HBNBCommand(cmd.Cmd):
    """HBNBCommand class"""
    prompt = '(hbnb) '
    classes = {"BaseModel": BaseModel}

    def do_quit(self, arg):
        """Quit command to exit the program"""
        return True

    def do_EOF(self, arg):
        """EOF command to exit the program"""
        return True

    def do_help(self, arg):
        """Help command to provide assistance"""
        return super().do_help(arg)

    def emptyline(self):
        """An empty line + ENTER shouldn’t execute anything"""
        pass
    
    def do_create(self, arg):
        """Creates a new instance of BaseModel, saves it (to the JSON file) and prints the id"""
        if not arg:
            print ("** class name missing **")
        elif arg not in self.classes:
            print ("* class doesn't exist **")
        else:
            newbase = BaseModel()
            print(newbase.id)
    
    def do_show(self, arg):
        """Prints the string representation of an instance based on the class name and id"""
        args = arg.split()
        if not arg:
            print ("** class name missing **")
        elif args[0] not in self.classes:
            print ("* class doesn't exist **")
        elif len(args) < 2:
            print("** instance id missing **")
        else:
            key = args[0] + "." + args[1]
            if key not in storage.all():
                print("** no instance found **")
            else:
                print(storage.all()[key])
                
    

if __name__ == '__main__':
    HBNBCommand().cmdloop()
