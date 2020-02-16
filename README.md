![hbnblogo](https://i.imgur.com/Ztfv04o.png)

# hbnb (The Holberton B&B) #
The program codes contained in this repository is the first phase in implementing the hbnb web application.  This web application allows an user to create an account to make a posting of their property for short-term rent.  It also allows an user to look through all postings to rent a property.  The first phase is to set up a console for development and debugging.  In development, the base class implementation will handle initialization, serialization and deserialization of instances into JSON.  It will be a simple flow of instance into dictionary into JSON into a file.  Additionally, the console will be a command line interpreter that handles creating, displaying, destroying and updating user data (objects creation through sub-classes).  It's able to take in commands in interactive and non-interactive mode.  Also, as part of development, a file storage engine will save all instances as JSON strings into a file.  In debugging, unittests using the Pythong unittest module will be performed on thhe base class, sub-classes and file storage engine.  The second phase is to develop the first part of the client side interface.  It will be a static website made with HTML 5.  The third phase of this project will be creating a database with MySQL for advanced file storage.  The fourth phase will be deploying the static website.  There could be Go Live issues that arises.  Thus, debugging is quite important at this point.  The fifth phase is to create a web server and a dynamic website.  The sixth phase is using RESTful API to expose and manipulate all data stored in JSON.  The final phase is loading data from client side into server side.  

The following illustrates the project scope.  
![hbnbscope](https://i.imgur.com/mx6uz0U.png)

The following illustrates the file organization of this repository.  
![fileorg](https://i.imgur.com/7FXAWhA.png)

The following illustrates the console in interactive mode.  


The following iluustrates the console in non-interactive mode.  


# General #
0. How to create a Python package?  
A Python package is a way to organize files and directories in a large-scale project.  In Python, each file is treated as a module and each directory is treated as a sub-module.  In each directory, there must be an \_\_init\_\_.py file so that Python knows to include the directory in the package.  Usually, the \_\_init\_\_.py file is empty but could include a list of modules.  In this project, the top-level module is called models which contains the base class and all its sub-classes.  And within it, there's a sub-module called engine that holds the file storage class.  The \_\_init\_\_.py file in models links the base class to the file storage class and vice versa.  In this project, a variable called storage was declared and initialized with the file storage class in the \_\_init\_\_.py file.  When storage is called in the base class, it knows to call and execute the methods from the file storage class.  

The following is the import statements in the \_\_init\_\_.py file.  
```python
from models.engine.file_storage import FileStorage
storage = FileStorage()
storage.reload()
```

The following illustrates the organization of this project's package.  
![Pythonpkg](https://i.imgur.com/MP8fjzC.png)

1. How to create a command interpreter in Python using the cmd module?  


2. What is Unit testing and how to implement it in a large project?  


3. How to serialize and deserialize a Class?  
In Python, the json module would serialize and deserialize a Class.  In order to serialize a Class, 

4. How to write and read a JSON file?  


5. How to manage datetime?  


6. What is an UUID?  


7. What is \*args and how to use it?  


8. What is \*\*kwargs and how to use it?  


9. How to handle named arguments in a function?  



# Resources #
0. Official Python Website  
https://docs.python.org/3/tutorial/modules.html  

1. HBNB videos  
https://www.youtube.com/playlist?list=PLlLHfkTcnvmPOp6jv\_89tRpJUMFrP-Wbi  

2. Python Tips Website  
https://pythontips.com/2013/08/04/args-and-kwargs-in-python-explained/  

3. Python Sheets Website  
https://www.pythonsheets.com/notes/python-tests.html  

# Authors #
Flavio Espinoza <flavio.vilchezespinoza@holbertonschool.com>
Jennifer Tang <jennifer.tang@holbertonschool.com>
