#!/usr/bin/python3
# Displays prompt to take in user input


import cmd
import sys
class HBNBCommand(cmd.Cmd):
    # Creates prompt as (hbnb)
    intro = ''
    prompt = '(hbnb) '
    file = None

    # Define methods of object
    def do_quit(self, arg):
        if arg == 'quit':
            self.close()
        return True


if __name__ == '__main__':
    HBNBCommand().cmdloop()
