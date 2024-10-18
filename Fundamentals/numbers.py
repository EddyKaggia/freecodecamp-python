# Numbers are always true, except for 0

done = 0

if done:
    print("yes")
else:
    print("no")
    
print(type(done) == bool)

# NUMBER DATA TYPES
# -------------------
# Numbers in Python can be of 3 types: int, float and complex.

# Integer numbers in Python
# ---------------------------
# Integer numbers are represented using the int class. You can define an integer using a value literal:

age = 8
# You can also define an integer number using the int() constructor:

age = int(8)
# To check if a variable is of type int, you can use the type() global function:

type(age) == int #True

# Floating point numbers in Python
# ----------------------------------
# Floating point numbers (fractions) are of type float. You can define an integer using a value literal:

fraction = 0.1
# Or using the float() constructor:

fraction = float(0.1)
# To check if a variable is of type float, you can use the type() global function:

type(fraction) == float #True

# Complex numbers in Python
# ---------------------------
# Complex numbers are of type complex.
# You can define them using a value literal:

complexNumber = 2+3j
# or using the complex() constructor:

complexNumber = complex(2, 3)
# Once you have a complex number, you can get its real and imaginary part:

complexNumber.real #2.0
complexNumber.imag #3.0
# Again, to check if a variable is of type complex, you can use the type() global function:

type(complexNumber) == complex #True

