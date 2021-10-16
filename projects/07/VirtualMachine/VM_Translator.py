# VMTranslator.py

import os
import platform
import sys
import Parser
import CodeWriter
from Command_Type import CommandType

class VMTranslator:
    __vmFile = None

    __parser = None
    __codeWriter = None

    def __init__(self, vmFilePath):
        vmFilePathList = []
        vmFileNameList = []
        asmFilePath = ""
        
        if os.path.isdir(vmFilePath):
            for f in os.listdir(vmFilePath):
                filePath = os.path.join(vmFilePath,f)
                filePath = filePath.replace('\\', '/')
                
                if os.path.isfile(filePath) and f.endswith(".vm"):
                    vmFilePathList.append(filePath)
                    vmFileNameList.append(f)
                    
            asmFilePath = vmFilePath + "/" + os.path.basename(vmFilePath)
        else:
            vmFilePathList.append(vmFilePath)
            
            # asmFilePath = "../asd/sdfs/xcv/<filename>" (removing the .vm extension)
            vmFilePath_parts = vmFilePath.split('.')
            asmFilePath = '.'.join(vmFilePath_parts[:-1])
    
        if (len(vmFilePathList) != 0):
            self.__parser = Parser.Parser()
            self.__codeWriter = CodeWriter.CodeWriter(asmFilePath)
            self.__codeWriter.writeInit() # Write Bootstrap code
        
            for i in range(0, len(vmFilePathList)):
                self.__vmFile = open(vmFilePathList[i], 'r')
                self.__codeWriter.setFileName(vmFileNameList[i].split('.')[0])
                self.__translateVMtoASM()
                self.__vmFile.close()
                
            self.__codeWriter.closeOutputFile()

    def __translateVMtoASM(self):
        for line in self.__vmFile:
            self.__parser.parse(line)

            if(self.__parser.commandType() == CommandType.C_IGNORE):
                continue
            else:
                self.__codeWriter.writeAsmInstructionComment(line)

            if (self.__parser.commandType() == CommandType.C_ARITHMETIC):
                self.__codeWriter.writeArithmetic(self.__parser.arg1())

            elif (self.__parser.commandType() in [CommandType.C_PUSH, CommandType.C_POP]):
                cmd = "push" if (self.__parser.commandType() == CommandType.C_PUSH) else "pop"
                self.__codeWriter.writePushPop(cmd, self.__parser.arg1(), self.__parser.arg2())

            elif (self.__parser.commandType() == CommandType.C_LABEL):
                self.__codeWriter.writeLabel(self.__parser.arg1())

            elif (self.__parser.commandType() == CommandType.C_GOTO):
                self.__codeWriter.writeGoto(self.__parser.arg1())

            elif (self.__parser.commandType() == CommandType.C_IF):
                self.__codeWriter.writeIf(self.__parser.arg1())
                
            elif (self.__parser.commandType() == CommandType.C_CALL):
                self.__codeWriter.writeCall(self.__parser.arg1(), self.__parser.arg2())
                
            elif (self.__parser.commandType() == CommandType.C_FUNCTION):
                self.__codeWriter.writeFunction(self.__parser.arg1(), self.__parser.arg2())
                
            else:
                self.__codeWriter.writeReturn()

if (__name__ == '__main__'):
    help_msg = '''
    ========================================================================================
    | HELP                                                                                 |
    ========================================================================================
    | Run below command to execute VMTranslator:                                           |
    |                                                                                      |
    | >> VMTranslator.py <ASM file path in linux format*>                                  |
    |                                                                                      |
    | Note: Please use Linux file format while mentioning filepath                         |
    |       Use forward slash(/) instead of back slash(\)                                  |
    |                                                                                      |
    | eg: >> python37 VM_Translator.py ../../08/FunctionCalls/StaticsTest                  |
    ========================================================================================
    ''' 

    if (len(sys.argv) < 2):
        print(help_msg)
    else:
        vmFilePath = sys.argv[1]
        vmTranslator = VMTranslator(vmFilePath)