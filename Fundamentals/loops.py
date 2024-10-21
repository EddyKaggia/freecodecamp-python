# LOOPS IN PYTHON
# -----------------
# Loops are one essential part of programming.

# In Python we have 2 kinds of loops: while loops and for loops.

# WHILE LOOPS IN PYTHON
# -----------------------
# while loops are defined using the while keyword, and they repeat their block until the condition is evaluated as False:
condition = True
while condition == True:
    print("The condition is True")
    
# This is an infinite loop. It never ends.

# Let's halt the loop right after the first iteration:
condition = True
while condition == True:
    print("The condition is True")
    condition = False

print("After the loop")

# In this case, the first iteration is run, as the condition test is evaluated to True. At the second iteration, the condition test evaluates to False, so the control goes to the next instruction after the loop.

# It's common to have a counter to stop the iteration after some number of cycles:
count = 0
while count < 10:
    print("The condition is True")
    count = count + 1

print("After the loop")

# FOR LOOPS IN PYTHON
# ---------------------
# Using for loops we can tell Python to execute a block for a pre-determined amount of times, up front, and without the need of a separate variable and conditional to check its value.

# For example we can iterate the items in a list:
items = [1, 2, 3, 4]
for item in items:
    print(item)
    
# Or, you can iterate a specific amount of times using the range() function:
for item in range(04):
    print(item)
    
# range(4) creates a sequence that starts from 0 and contains 4 items: [0, 1, 2, 3].

# To get the index, you should wrap the sequence into the enumerate() function:
items = [1, 2, 3, 4]
for index, item in enumerate(items):
    print(index, item)
    
# BREAK AND CONTINUE IN PYTHON
# ------------------------------
# Both while and for loops can be interrupted inside the block, using two special keywords: break and continue.

# continue stops the current iteration and tells Python to execute the next one.

# break stops the loop altogether, and goes on with the next instruction after the loop ends.

# The first example here prints 1, 3, 4. The second example prints 1:

items = [1, 2, 3, 4]
for item in items:
    if item == 2:
        continue
    print(item)
    
items = [1, 2, 3, 4]
for item in items:
    if item == 2:
        break
    print(item)