# Command_Type.py

import enum

class CommandType(enum.Enum):
    C_IGNORE = 0 # Commands that need to be ignored. Eg. Comments, Whitepace
    C_ARITHMETIC = 1
    C_PUSH = 2
    C_POP = 3
    C_LABEL = 4
    C_GOTO = 5
    C_IF = 6
    C_FUNCTION = 7
    C_RETURN = 8
    C_CALL = 9