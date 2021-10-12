# VMTranslator.py

import sys
import Parser
import CodeWriter
from Command_Type import CommandType

class VMTranslator:
    __vmFile = None
    __vmFileName = ""
    __asmFilePath = ""

    __parser = None
    __codeWriter = None

    def __init__(self, vmFilePath):
        # Get the vmFileName
        # Eg: if vmFilePath = "../asd/sdfs/xcv/<filename>.vm"
        # then __vmFileName = <filename>
        __vmFileName = vmFilePath.split('/')[-1].split(".")[0]

        # __asmFilePath = "../asd/sdfs/xcv/<filename>" (removing the .vm extension)
        vmFilePath_parts = vmFilePath.split('.')
        self.__asmFilePath = '.'.join(vmFilePath_parts[:-1])

        self.__parser = Parser.Parser()
        self.__codeWriter = CodeWriter.CodeWriter(self.__asmFilePath)

        self.__vmFile = open(vmFilePath, 'r')
        self.__translateVMtoASM()
        self.__vmFile.close()
        self.__codeWriter.closeOutputFile()


    def __translateVMtoASM(self):
        for line in self.__vmFile:
            self.__parser.parse(line)

            if(self.__parser.commandType() == CommandType.C_IGNORE):
                continue

            elif (self.__parser.commandType() == CommandType.C_ARITHMETIC):
                self.__codeWriter.writeAsmInstructionComment(line)
                self.__codeWriter.writeArithmetic(self.__parser.arg1())

            elif (self.__parser.commandType() in [CommandType.C_PUSH, CommandType.C_POP]):
                cmd = "push" if (self.__parser.commandType() == CommandType.C_PUSH) else "pop"

                self.__codeWriter.writeAsmInstructionComment(line)
                self.__codeWriter.writePushPop(cmd, self.__parser.arg1(), self.__parser.arg2(), self.__vmFileName)

if (__name__ == '__main__'):
    help_msg = '''
    ==================================================
    | HELP                                           |
    ==================================================
    | Run below command to execute VMTranslator:     |
    | >> VMTranslator.py <ASM file path>             |
    | eg: >> VMTranslator.py Add.vm                  |
    ==================================================
    '''

    if (len(sys.argv) < 2):
        print(help_msg)
    else:
        vmFilePath = sys.argv[1]
        vmTranslator = VMTranslator(vmFilePath)