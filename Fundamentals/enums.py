# Enums in Python
# -----------------
# Enums are readable names that are bound to a constant value.

# To use enums, import Enum from the enum standard library module:

from enum import Enum
# Then you can initialize a new enum in this way:

class State(Enum):
    INACTIVE = 0
    ACTIVE = 1
# Once you do so, you can reference State.INACTIVE and State.ACTIVE, and they serve as constants.

# Now if you try to print State.ACTIVE for example:

print(State.ACTIVE)
# it will not return 1, but State.ACTIVE.

# The same value can be reached by the number assigned in the enum: print(State(1)) will return State.ACTIVE. Same for using the square brackets notation State['ACTIVE'].

# You can, however, get the value using State.ACTIVE.value.

# You can list all the possible values of an enum:

list(State) # [<State.INACTIVE: 0>, <State.ACTIVE: 1>]
# You can count them:

len(State) # 2