# Parser.py

from Command_Type import CommandType

class Parser:
    # __vm_fp = None
    # __curr_line = ""
    __commandType = 0
    __arg1 = ""
    __arg2 = 0

    def parse(self, line):
        # Trim leading and trailing whitespace
        line = line.strip()

        # Check for
        # 1. Whitespace or Comment
        if (line == "" or line.startswith("//")):
            self.__commandType = CommandType.C_IGNORE

        elif (line.startswith("push")):
            self.__commandType = CommandType.C_PUSH
            self.__splitInstruction(line)

        elif (line.startswith("pop")):
            self.__commandType = CommandType.C_POP
            self.__splitInstruction(line)

        else:
            self.__commandType = CommandType.C_ARITHMETIC
            self.__arg1 = line

    def commandType(self):
        return self.__commandType

    def arg1(self):
        return self.__arg1

    def arg2(self):
        return self.__arg2

    def __splitInstruction(self, line):
        args = line.split(' ')
        self.__arg1 = args[1]
        self.__arg2 = int(args[2])