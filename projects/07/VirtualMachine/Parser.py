# Parser.py

from Command_Type import CommandType

class Parser:
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
            return
        else:
            # Remove Trailing Comments if present
            line = self.__removeTrailingComment(line)

        # Check for different command types and initialize the args respectively
        if (line.startswith("push")):
            self.__commandType = CommandType.C_PUSH
            self.__splitInstruction(line)

        elif (line.startswith("pop")):
            self.__commandType = CommandType.C_POP
            self.__splitInstruction(line)

        elif (line.startswith("label")):
            self.__commandType = CommandType.C_LABEL
            self.__splitBranchInstructions(line)

        elif (line.startswith("goto")):
            self.__commandType = CommandType.C_GOTO
            self.__splitBranchInstructions(line)

        elif (line.startswith("if")):
            self.__commandType = CommandType.C_IF
            self.__splitBranchInstructions(line)
            
        elif (line.startswith("call")):
            self.__commandType = CommandType.C_CALL
            self.__splitInstruction(line)
            
        elif (line.startswith("function")):
            self.__commandType = CommandType.C_FUNCTION
            self.__splitInstruction(line)
            
        elif (line == "return"):
            self.__commandType = CommandType.C_RETURN

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

    def __splitBranchInstructions(self, line):
        args = line.split(' ')
        self.__arg1 = args[1]

    def __removeTrailingComment(self, line):
        return (line.split("//")[0]).strip()