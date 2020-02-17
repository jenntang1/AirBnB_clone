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
from models.amenity import Amenity

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
            'State': State,
            'Amenity': Amenity,
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
        elif arg not in HBNBCommand.classes:
            print("** class doesn't exist **")
        else:
            new = HBNBCommand.classes[arg]()
            storage.save()
            print("{}".format(new.id))

    def do_show(self, arg):
        'Prints the string rep of an instance based on class name and id'
        args = arg.split(" ")
        obj_dict = storage.all()
        if arg is '':
            print("** class name missing **")
        elif args[0] not in HBNBCommand.classes:
            print("** class doesn't exist **")
        elif len(args) < 2:
            print("** instance id missing **")
        else:
            key = args[0] + '.' + args[1]
            try:
                print(obj_dict[key])
            except:
                print("** no instance found **")

    def do_destroy(self, arg):
        'Delete an object based on class name and id'
        args = arg.split(" ")
        if arg is '':
            print("** class name missing **")
        elif args[0] not in HBNBCommand.classes:
            print("** class doesn't exist **")
        elif len(args) < 2:
            print("** instance id missing **")
        else:
            key = args[0] + '.' + args[1]
            obj_dict = storage.all()
            try:
                del(obj_dict[key])
                storage.save()
            except:
                print("** no instance found **")

    def do_all(self, arg):
        'Prints all string reps of all instaces, with or without class'
        obj_dict = storage.all()
        if not arg:
            for key, value in obj_dict.items():
                print("{}".format(obj_dict[key]))
        else:
            for key, value in obj_dict.items():
                skey = key.split(".")
                if skey[0] == arg:
                    print("{}".format(obj_dict[key]))

    def do_update(self, arg):
        obj_dict = storage.all()
        args = arg.split(" ")
        if arg is '':
            print("** class name missing **")
        elif args[0] not in HBNBCommand.classes:
            print("** class doesn't exist **")
        elif len(args) < 2:
            print("** instance id missing **")
        #elif args[1] not in obj_dict.items() and args[0] + args[1] not in obj_dict.items():
        elif args[1] == 0:
            for key, value in obj_dict.items():
                skey = key.split(".")
                if skey[1] != args[1]:
                    print("** no instance found **")
        elif len(args) < 3:
            print("** attribute name missing **")
        elif len(args) < 4:
            print("** value missing **")
        else:
            for key, value in obj_dict.items():
                skey = key.split(".")
                if skey[1] == args[1]:
                    val = args[3]
                    updater = {args[2]: args[3]}
                    (obj_dict[key].__dict__).update(updater)
            storage.save()

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
