![hbnbheader](https://i.imgur.com/smlxqpv.png){.center}

# hbnb (The Holberton B&B) #
The program codes contained in this repository is the first phase in implementing the hbnb web application.  This web application allows an user to create an account to make a posting of their property for short-term rent.  It also allows an user to look through all postings to rent a property.  The first phase is to set up a console for development and debugging.  In development, the base class implementation will handle initialization, serialization and deserialization of instances into JSON.  It will be a simple flow of instance into dictionary into JSON into a file.  Additionally, the console will be a command line interpreter that handles creating, displaying, destroying and updating user data (objects creation through sub-classes).  It's able to take in commands in interactive and non-interactive mode.  Also, as part of development, a file storage engine will save all instances as JSON strings into a file.  In debugging, unittests using the Pythong unittest module will be performed on thhe base class, sub-classes and file storage engine.  The second phase is to develop the first part of the client side interface.  It will be a static website made with HTML 5.  The third phase of this project will be creating a database with MySQL for advanced file storage.  The fourth phase will be deploying the static website.  There could be Go Live issues that arises.  Thus, debugging is quite important at this point.  The fifth phase is to create a web server and a dynamic website.  The sixth phase is using RESTful API to expose and manipulate all data stored in JSON.  The final phase is loading data from client side into server side.  

The following illustrates the project scope.  
![hbnbscope](https://i.imgur.com/mx6uz0U.png)

The following illustrates the file organization of this repository.  
![hbnbfileorg](https://i.imgur.com/7cQM83Z.png)

The following illustrates the console in interactive mode.  In order to start the console, execute the console.py file on the command line.  Then, type in commands like create, show, destroy, update or all followed by the class name.  The quit, EOF and help commands doesn't need additional arguments on the command line.  The all command would display all class objects if no argument follows.  
![hbnbinteractive](https://i.imgur.com/JPUGd72.png)

![hbnbquit](https://i.imgur.com/JxOJ7HF.png)

![hbnbeof](https://i.imgur.com/L3v53mE.png)

The following illustrates the console in non-interactive mode.  
![hbnbnoninteractive](https://i.imgur.com/rnXiN47.png)

## General ##
0. How to create a Python package?  
A Python package is a way to organize files and directories in a large-scale project.  In Python, each file is treated as a module and each directory is treated as a sub-module.  In each directory, there must be an \_\_init\_\_.py file so that Python knows to include the directory in the package.  Usually, the \_\_init\_\_.py file is empty but could include a list of modules.  In this project, the top-level module is called models which contains the base class and all its sub-classes.  And within it, there's a sub-module called engine that holds the file storage class.  The \_\_init\_\_.py file in models links the base class to the file storage class and vice versa.  In this project, a variable called storage was declared and initialized with the file storage class in the \_\_init\_\_.py file.  When storage is called in the base class, it knows to call and execute the methods from the file storage class.  

    The following are the import statements in the \_\_init\_\_.py file.  

```python
from models.engine.file_storage import FileStorage


storage = FileStorage()
storage.reload()
```

The following illustrates the organization of this project's package.  
![hbnbpythonpkg](https://i.imgur.com/MP8fjzC.png)

1. How to create a command interpreter in Python using the cmd module?  
In Python, the cmd module supports building a command line interpreter interactively.  The Cmd class in the module should be passed into the command processor class.  At the bottom of the file, apply a loop to read all lines from input, parse them and execute the command.  In the class, declare a public class attribute to create a custom prompt.  In this project, the commands handled are quit, EOF (end-of-file), empty line, help, create, show, destroy, all and update.  The quit and EOF commands would exit the interpreter normally.  The empty line with ENTER shouldn't execute anything.  The help command will raise messages for the command specified.  The create command creates a new instance of the base class, saves it to JSON and prints a randomly assigned id.  The show command prints a string representation of an instance of the specified class and id.  The destroy command deletes an instance of the specified class and id.  The all command prints a string representation of all instances.  The update command will update an instance's attributes.  

    The following are more details for each command:  

    Create command  
    1. creates a new instance of BaseModel
    2. saves new instance to a json file
    3. prints the randomly assigned id
    4. if class name is not given, print “\*\* class name missing \*\*”
    5. if class name doesn’t exist, print “\*\* class doesn’t exist \*\*”

    Show command  
    1. prints a string representation of an instance
    2. if class name is not given, print “\*\* class name missing \*\*”
    3. if class name doesn’t exist, print “\*\* class doesn’t exist \*\*”
    4. if the randomly assigned id is not given, print “\*\* instance id missing \*\*”
    5. if the instance doesn’t exist for the id given, print “\*\* no instance found \*\*”

    Destroy command  
    1. deletes an instance
    2. saves the deletion into json file
    3. if class name is not given, print “\*\* class name missing \*\*”
    4. if class name doesn’t exist, print “\*\* class doesn’t exist \*\*”
    5. if the randomly assigned id is missing, print “\*\* instance id missing \*\*”
    6. if the instance doesn’t exist for the id given, print “\*\* no instance found \*\*”

    All command  
    1. prints all string representation for all instances when no class name is given
    2. prints all string representation for a class when a class name is given
    3. if class name doesn't exist, print "\*\* class doesn't exist \*\*"

    Update command  
    1. updates an instance with given class anme and randomly assigned id
    2. only one attribute could be updated at a time
    3. if the class name is not given, print "\*\* class name missing \*\*"
    4. if the class name doesn't exist, print "\*\* class doesn't exist \*\*"
    5. if the instance doesn't exist for the id given, print "\*\* no instance found \*\*"
    6. if the attribute is not given, print "\*\* attribute name missing \*\*"
    7. if the value of the attribute doesn't exist, print "\*\* value missing \*\*"

    The following outlines the command line interpreter for this project using the cmd module.  

```python
import cmd
import sys


class HBNBCommand(cmd.Cmd):
    prompt = '(hbnb)'

    def do_quit(self, arg):
        return True

    def do_EOF(self, arg):
        return True

    def do_create(self, arg):
        do something

    def do_show(self, arg):
        do something

    def emptyLine(self):
        pass

    def help(self):
        print ("help message")

if __name__ == '__main__':
   HBNBCommand().cmdloop()
```

2. What is Unit testing and how to implement it in a large project?  
In a large-scale project, unit tests are important in validating all classes.  By importing the unittest module, test cases could be automated and executed with a simple command (see below).  

```python
python3 -m unittest discover tests
```

The files in the tests directory is structured similar to the models directory.  Each class in the models directory has its own test file.  The subclasses: user, city, state, place, amenity and review inherits test cases from the base class.  

3. How to serialize and deserialize a Class?  
In Python, the json module would serialize and deserialize a Class.  In order to serialize a Class, use the load function to convert a string into a JSON object and save it to a file.  Or use the loads function to also convert a string into a JSON object but it goes to standard output that's human readable.  In order to deserialize a Class, use the dump function to convert the JSON object into a string and save it to a file.  Or use the dumps function to also convert the JSON object into a string but it goes to standard output.  

4. How to write and read a JSON file?  
In Python, the json module needs to be imported to write to a file and read from a file.  When paired with the with statement, the JSON file could be comprehensively opened and closed.  In this project, the save method serializes an object and saves it to a JSON file and the reload method reads the JSON object from its file and deserializes it to an object.  Essentially, these two methods makes up the FileStorage class which is the first storage engine of this project.  
    
    The following illustrates writing and reading a JSON file.  

```python
""" Example of writing JSON into a file """
import json


with open('file.json', 'r') as file_object:
    data = json.load(file_object)
```

```python
""" Example of reading JSON from a file """
import json


with open('file.json', 'w') as file_object:
    json.dump(data, file_object)
```

5. How to manage datetime?  
In Python, datetime is a module that helps with manipulating dates and times.  The classes are date, time, datetime, timedelta and tzinfo.  In this project, the datetime class is imported to create datetime objects that are categorized as aware or naive.  By default, a datetime object is naive but could be made aware to account for time zones and daylight savings.  It already has class attributes: year, month, day, hour, minute, second, microsecond and tzinfo (time zone information).  When datetime objects are creates, they are immutable, hashable and supports pickling.  Use the now function to create an instance of datetime with the current date and time.  Use the strptime function to create a datetime object from a string.  Use the strftime function to create a string into a datetime object.  

6. What is an UUID?  
UUID stands for Universal Unique Identifier that's a Python library.  It generates random and unique ids that could be represented as a string, integer or hexadecimal.  The string would be 16 bytes, the integer would be 128 bits and the hexadecimal would be a 32 character string.  Within UUID, there are a few functions that would generate random objects.  The most commonly used are uuid1() and uuid4().  The difference is that uuid1() would generate an id that contains the computer's ip address but uuid4() doesn't.  

7. What is \*args and how to use it?  
\*args is a tuple containing arguments that are passed to a function.  When used, many arguments could be passed into a function.  However, it's needs to be passed in positionally which means the arguments need to be in a particular order.  

```python
def args_example(arg1, arg2, arg3):
    print("arg1:", arg1)
    print("arg2:", arg2)
    print("arg3:", arg3)

args = ("Hello", "World", "!")
args_exampe(*args)

arg1: Hello
arg2: World
arg3: !
```

8. What is \*\*kwargs and how to use it?  
\*\*kwargs is a dictionary containing key/value pair arguments that are passed to a function.  Similiar to \*args, many arguments could be passed into a function.  Unlike \*args, \*\*kwargs has to be keyword arguments so that the function could match the argument to the key in the dictionary.  

```python
def kwargs_example(**kwargs):
    for key, value in kwargs.items():
        print("{}: {}".format(key, value))

kwargs_example(kwarg1="Betty Holberton", kwarg2="Malala Yousafzai", kwarg3="Maya Angelou")

kwarg1: Betty Holberton
kwarg2: Malala Yousafzai
kwarg3: Maya Angelou
```

9. How to handle named arguments in a function?  
In this project, the name/keyword argument will be a dictionary.  The key would be the class attribute name  and the value would be the unique id, first created datetime object and the updated datetime object.  

## Resources ##
0. Official Python Website  
https://docs.python.org/3/tutorial/modules.html  

1. HBNB videos  
https://www.youtube.com/playlist?list=PLlLHfkTcnvmPOp6jv\_89tRpJUMFrP-Wbi  

2. Python Tips Website  
https://pythontips.com/2013/08/04/args-and-kwargs-in-python-explained/  

3. Python Sheets Website  
https://www.pythonsheets.com/notes/python-tests.html  

## Authors ##
Flavio Espinoza <flavio.vilchezespinoza@holbertonschool.com>  
Jennifer Tang <jennifer.tang@holbertonschool.com>
