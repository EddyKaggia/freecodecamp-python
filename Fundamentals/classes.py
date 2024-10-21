# CLASSES IN PYTHON
#  -------------------
# In addition to using the Python-provided types, we can declare our own classes, and from classes we can instantiate objects.

# An object is an instance of a class. A class is the type of an object.

# We can define a class in this way:

# class <class_name>:
#     # my class
# For example let's define a Dog class

# class Dog:
#     # the Dog class
# A class can define methods:

class Dog:
    # the Dog class
    def bark(self):
        print('WOF!')
        
# self as the argument of the method points to the current object instance, and must be specified when defining a method.

# We create an instance of a class, an object, using this syntax:
roger = Dog()

# Now roger is a new object of type Dog.

# If you run
print(type(roger))

# You will get <class '__main__.Dog'>

# A special type of method, __init__() is called constructor, and we can use it to initialize one or more properties when we create a new object from that class:
class Dog:
    # the Dog class
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def bark(self):
        print('WOF!')
        
# We use it in this way:
roger = Dog('Roger', 8)
print(roger.name) # 'Roger'
print(roger.age)  # 8

roger.bark() # 'WOF!'

# One important feature of classes is inheritance.

# We can create an Animal class with a method walk():
class Animal:
    def walk(self):
        print('Walking..')
        
# and the Dog class can inherit from Animal:
class Dog(Animal):
    def bark(self):
        print('WOF!')
        
# Now creating a new object of class Dog will have the walk() method as that's inherited from Animal:
roger = Dog()
roger.walk() # 'Walking..'
roger.bark() # 'WOF!'