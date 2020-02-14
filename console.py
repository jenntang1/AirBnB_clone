#!/usr/bin/python3
# Displays prompt to take in user input


import cmd
import sys
class HBNBCommand(cmd.Cmd):
    # Creates prompt as (hbnb)
    intro = ''
    prompt = '(hbnb) '
    file = None

    # Define method of objects
    def do_quit(self, arg):
        'Quit command to exit the program'
        if arg == 'quit':
            self.close()
        return True
    
    def do_EOF(self, arg):
        'Closes console if end of file'
        print('')
        return True

    def do_create(self, arg):
        ' Creates a new instance of BaseModel, saves it (to the JSON file) and prints the id '
        new = BaseModel()
        # with ():
        print("{}".format(self.id))
        if 

if __name__ == '__main__':
    HBNBCommand().cmdloop()
