#!/usr/bin/python3
# Displays prompt to take in user input


import cmd
import sys
from models.base_model import BaseModel
from models.__init__ import storage
from models.user import User
from models.place import Place
from models.city import City
from models.review import Review
from models.state import State


class HBNBCommand(cmd.Cmd):
    # Creates prompt as (hbnb)
    intro = ''
    prompt = '(hbnb) '
    file = None
    classes = {
            'BaseModel': BaseModel,
            'User': User,
            'Place': Place,
            'City': City,
            'Review': Review,
            'State': State
              }

    # Define method of objects
    def do_quit(self, arg):
        'Quit command to exit the program'
        print('')
        return True

    def do_EOF(self, arg):
        'Exits shell upon End of File'
        print('')
        return True

    def do_create(self, arg):
        'Creates a new instance of BaseModel, saves it and prints the id'
        if arg is '':
            print("** class name missing **")
        elif arg not in self.classes:
            print("** class doesn't exist **")
        else:
            new = self.classes[arg]()
            storage.save()
            print("{}".format(new.id))

    def do_show(self, arg):
        'Prints the string rep of an instance based on class name and id'
        args = arg.split(" ")
        obj_dict = storage.all()
        if arg is '':
            print("** class name missing **")
        elif arg not in self.classes:
            print("** class doesn't exist **")
        elif args[1] is not id:
            print("** instance id missing **")
        else:
            try:
                print("** no instance found **")
            except:
                print(obj_dict)

    def emptyline(self):
        'Empties last command'
        pass

    # Ovewrites help message
    def help_help(self):
        'Help message for help'
        print("Prints messages with information of command")

    def help_create(self):
        'Creates instance of object'
        print("For a new instance of an obj saves it and prints id")

    def help_quit(self):
        'Help message for quit'
        print('Exits the shell')

    def help_EOF(self):
        'Help message for EOF'
        print('Upon end of file, exits shell')

if __name__ == '__main__':
    HBNBCommand().cmdloop()
