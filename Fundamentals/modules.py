# MODULES IN PYTHON
# -------------------
# Every Python file is a module.

# You can import a module from other files, and that's the base of any program of moderate complexity, as it promotes a sensible organization and code reuse.

# In the typical Python program, one file acts as the entry point. The other files are modules and expose functions that we can call from other files.

# The file dog.py contains this code:
def bark():
    print('WOF!')
    
# We can import this function from another file using import. And once we do, we can reference the function using the dot notation, dog.bark():

# import dog
dog.bark()

# Or, we can use the from .. import syntax and call the function directly:

# from dog import bark
bark()

# The first strategy allows us to load everything defined in a file.

# The second strategy lets us pick the things we need.

# Those modules are specific to your program, and importing depends on the location of the file in the filesystem.

# Suppose you put dog.py in a lib subfolder.

# In that folder, you need to create an empty file named __init__.py. This tells Python the folder contains modules.

# Now you can choose - you can import dog from lib:

# from lib import dog
dog.bark()

# or you can reference the dog module specific function importing from lib.dog:

# from lib.dog import bark 
bark()