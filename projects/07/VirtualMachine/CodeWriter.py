# CodeWriter.py

import sys

class CodeWriter:
    __asm_fp = None
    __vmFileName = ""

    # Conditional Operator Counter
    __cond_opt_cnt = 0
    __fun_ret_lbl_cnt = 0

    def __init__(self, asmFileName):
        self.__asm_fp = open(asmFileName+".asm", 'w')

    #################################
    # STACK functions : START
    def __push(self):
        '''
        Assuming D contains the value to be pushed
        Store D at Top of Stack
        '''
        self.__asm_fp.write("@SP" + "\n")
        self.__asm_fp.write("A=M" + "\n")
        self.__asm_fp.write("M=D" + "\n")

        # increment SP
        self.__incSP()

    def __pop(self):
        '''
            Storing the Top of Stack(TOS) in D
        '''
        # decrement SP
        self.__decSP()

        # Store Top of Stack(TOS) in D
        self.__asm_fp.write("@SP" + "\n")
        self.__asm_fp.write("A=M" + "\n")
        self.__asm_fp.write("D=M" + "\n")

    def __incSP(self):
        # increment stack pointer
        self.__asm_fp.write("@SP" + "\n")
        self.__asm_fp.write("M=M+1" + "\n")

    def __decSP(self):
        # decrement stack pointer
        self.__asm_fp.write("@SP" + "\n")
        self.__asm_fp.write("M=M-1" + "\n")

    # STACK functions : END
    #################################

    def writePushPop(self, cmd, memSegment, index):
        '''
            Write ASM instructions to PUSH or POP to Memory Segments
        '''
        if (memSegment in ["local", "argument", "this", "that"]):
            dict_memSeg = {"local":"LCL", "argument":"ARG", "this":"THIS", "that":"THAT"}
            if (cmd == "push"):
                self.__asm_fp.write("@" + dict_memSeg[memSegment] + "\n")
                self.__asm_fp.write("D=M" + "\n")
                self.__asm_fp.write("@" + str(index) + "\n")
                self.__asm_fp.write("A=D+A" + "\n") # A = LCL + index
                self.__asm_fp.write("D=M" + "\n") # D = RAM[LCL+index]
                self.__push()

            else:
                self.__asm_fp.write("@" + dict_memSeg[memSegment] + "\n")
                self.__asm_fp.write("D=M" + "\n")
                self.__asm_fp.write("@" + str(index) + "\n")
                self.__asm_fp.write("D=D+A" + "\n")
                self.__asm_fp.write("@R13" + "\n")
                self.__asm_fp.write("M=D" + "\n") # R13 = LCL+index

                self.__pop()

                self.__asm_fp.write("@R13" + "\n")
                self.__asm_fp.write("A=M" + "\n")
                self.__asm_fp.write("M=D" + "\n") # RAM[LCL+index] = TOS

        elif (memSegment == "constant"):

            if(cmd == "push"):
                self.__asm_fp.write("@" + str(index) + "\n")
                self.__asm_fp.write("D=A" + "\n")
                self.__push()

            else:
                print("Syntax Error : POP operation cannot be performed in constant")
                sys.exit(1)

        elif (memSegment in ["pointer", "static", "temp"]):

            m = ""
            if (memSegment == "pointer"):
                m = "THIS" if (index == 0) else "THAT"
            elif (memSegment == "temp"):
                m = str(5 + index)
            else:
                m = self.__vmFileName + "." + str(index)

            if(cmd == "push"):
                self.__asm_fp.write("@" + m + "\n")
                self.__asm_fp.write("D=M" + "\n")
                self.__push()

            else:
                self.__pop()
                self.__asm_fp.write("@" + m + "\n")
                self.__asm_fp.write("M=D" + "\n")

    def writeArithmetic(self, cmd):
        '''
            Write ASM instructions to perform ARITHMETIC operations
        '''
        if (cmd == "add"):
            # POP operand2 (op2)
            self.__pop()

            # Store op2 to R13 (temp register)
            self.__storeOperand2()

            # POP op1
            self.__pop()

            # add : op1 + op2
            self.__addition()

            # Push result on stack
            self.__push()

        elif (cmd == "sub"):
            # POP operand2 (op2)
            self.__pop()

            # Store op2 to R13 (temp register)
            self.__storeOperand2()

            # POP op1
            self.__pop()

            # subtract : op1 - op2
            self.__subtraction()

            # Push result on stack
            self.__push()

        elif (cmd == "neg"):
            # POP operand1 (op1)
            self.__pop()

            #negate :  -op1
            self.__negation()

            # Push result on stack
            self.__push()

        elif (cmd == "eq"):
            # POP operand2 (op2)
            self.__pop()

            # Store op2 to R13 (temp register)
            self.__storeOperand2()

            # POP op1
            self.__pop()

            # subtract : op1 - op2
            self.__subtraction()

            # check for equality (op1 == op2)
            self.__check_eq()

            # Push result on stack
            self.__push()

        elif (cmd == "gt"):
            # POP operand2 (op2)
            self.__pop()

            # Store op2 to R13 (temp register)
            self.__storeOperand2()

            # POP op1
            self.__pop()

            # subtract : op1 - op2
            self.__subtraction()

            # check for greater than (op1 > op2)
            self.__check_gt()

            # Push result on stack
            self.__push()

        elif (cmd == "lt"):
            # POP operand2 (op2)
            self.__pop()

            # Store op2 to R13 (temp register)
            self.__storeOperand2()

            # POP op1
            self.__pop()

            # subtract : op1 - op2
            self.__subtraction()

            # check for less than (op1 < op2)
            self.__check_lt()

            # Push result on stack
            self.__push()

        elif (cmd == "and"):
            # POP operand2 (op2)
            self.__pop()

            # Store op2 to R13 (temp register)
            self.__storeOperand2()

            # POP op1
            self.__pop()

            # AND : op1 & op2
            self.__logicalAND()

            # Push result on stack
            self.__push()

        elif (cmd == "or"):
            # POP operand2 (op2)
            self.__pop()

            # Store op2 to R13 (temp register)
            self.__storeOperand2()

            # POP op1
            self.__pop()

            # OR : op1 | op2
            self.__logicalOR()

            # Push result on stack
            self.__push()

        elif (cmd == "not"):
            # POP operand1 (op1)
            self.__pop()

            #logical NOT
            self.__logicalNOT()

            # Push result on stack
            self.__push()

    def writeLabel(self, label):
        self.__asm_fp.write("(" + label + ")" + "\n")

    def writeGoto(self, label):
        self.__asm_fp.write("@" + label + "\n")
        self.__asm_fp.write("0;JMP" + "\n")

    def writeIf(self, label):
        self.__pop()
        self.__asm_fp.write("@" + label + "\n")
        self.__asm_fp.write("D;JNE" + "\n")

    def writeCall(self, functionName, nArgs):
        self.__fun_ret_lbl_cnt = self.__fun_ret_lbl_cnt + 1
        returnLabel = functionName + "$ret." + str(self.__fun_ret_lbl_cnt)
        
        # push returnLabel
        self.__asm_fp.write("@" + returnLabel + "\n")
        self.__asm_fp.write("D=A" + "\n")
        self.__push()
    
        # push ["LCL", "ARG", "THIS", "THAT"]
        memSegs = ["LCL", "ARG", "THIS", "THAT"]
        for mSeg in memSegs:
            self.__asm_fp.write("// Push " + mSeg + " on Stack" + "\n")
            self.__asm_fp.write("@" + mSeg + "\n")
            self.__asm_fp.write("D=M" + "\n")
            self.__push()
        
        # ARG = SP - 5 - nArgs
        self.__asm_fp.write("// ARG = SP - 5 - nArgs" + "\n")
        self.__asm_fp.write("@5" + "\n")
        self.__asm_fp.write("D=A" + "\n")
        self.__asm_fp.write("@SP" + "\n")
        self.__asm_fp.write("D=M-D" + "\n")
        self.__asm_fp.write("@" + str(nArgs) + "\n")
        self.__asm_fp.write("D=D-A" + "\n")
        self.__asm_fp.write("@ARG" + "\n")
        self.__asm_fp.write("M=D" + "\n")
        
        # LCL = SP
        self.__asm_fp.write("@SP" + "\n")
        self.__asm_fp.write("D=M" + "\n")
        self.__asm_fp.write("@LCL" + "\n")
        self.__asm_fp.write("M=D" + "\n")
        
        # Goto functionName
        self.__asm_fp.write("@" + functionName + "\n")
        self.__asm_fp.write("0;JMP" + "\n")
        
        # (returnLabel)
        self.__asm_fp.write("(" + returnLabel + ")" + "\n")
    
    def writeFunction(self, functionName, nVars):
        self.__asm_fp.write("(" + functionName + ")" + "\n")
        self.__asm_fp.write("// Initializing "+ str(nVars) + " local variables to 0" + "\n")
        if (nVars > 0):
            self.__asm_fp.write("D=0" + "\n")
            for i in range(0, nVars): # TODO: Implement for loop in asm
                self.__push()
        
    def writeReturn(self):
        # endframe = LCL ~~> R14 = LCL
        self.__asm_fp.write("@LCL" + "\n")
        self.__asm_fp.write("D=M" + "\n")
        self.__asm_fp.write("@R14" + "\n")
        self.__asm_fp.write("M=D" + "\n")
        
        # retAddr = *(endFrame - 5) ~~> R15 = *(R14 - 5)
        self.__asm_fp.write("@5" + "\n")
        self.__asm_fp.write("D=A" + "\n")
        self.__asm_fp.write("@R14" + "\n")
        self.__asm_fp.write("D=M-D" + "\n")
        self.__asm_fp.write("A=D" + "\n")
        self.__asm_fp.write("D=M" + "\n")
        self.__asm_fp.write("@R15" + "\n")
        self.__asm_fp.write("M=D" + "\n")
        
        # *ARG = pop() ~~> *ARG = returnValue
        self.__pop()
        self.__asm_fp.write("@ARG" + "\n")
        self.__asm_fp.write("A=M" + "\n")
        self.__asm_fp.write("M=D" + "\n")
        
        # SP = ARG + 1 ~~> RAM[SP] = RAM[ARG] + 1
        self.__asm_fp.write("@ARG" + "\n")
        self.__asm_fp.write("D=M" + "\n")
        self.__asm_fp.write("@SP" + "\n")
        self.__asm_fp.write("M=D+1" + "\n")
        
        memSegs = ["THAT", "THIS", "ARG", "LCL"]
        
        for i in range(0,len(memSegs)):
            self.__asm_fp.write("// " + memSegs[i] + " = *(endFrame-" + str(i+1) + ")\n")
            self.__asm_fp.write("@R14" + "\n")
            self.__asm_fp.write("D=M" + "\n")
            self.__asm_fp.write("@" + str(i+1) + "\n")
            self.__asm_fp.write("A=D-A" + "\n")
            self.__asm_fp.write("D=M" + "\n")
            self.__asm_fp.write("@" + memSegs[i] + "\n")
            self.__asm_fp.write("M=D" + "\n")
        
        # goto retAddr
        self.__asm_fp.write("// goto retAddr" + "\n")
        self.__asm_fp.write("@R15" + "\n")
        self.__asm_fp.write("A=M" + "\n")
        self.__asm_fp.write("0;JMP" + "\n")
        
    def setFileName(self, fileName):
        self.__vmFileName = fileName
        self.__asm_fp.write("\n// ASM code for File : " + fileName + ".vm" + "\n")
    
    def writeInit(self):
        # BootStrap Code
        self.__asm_fp.write("// Bootstrap Code" + "\n")
        self.__asm_fp.write("\n// Set SP=256" + "\n")
        self.__asm_fp.write("@256" + "\n")
        self.__asm_fp.write("D=A" + "\n")
        self.__asm_fp.write("@SP" + "\n")
        self.__asm_fp.write("M=D" + "\n")
        
        self.__asm_fp.write("\n// Call Sys.init" + "\n")
        self.writeCall("Sys.init", 0)

    #################################
    # ARITHMETIC functions : START
    def __addition(self):
        self.__asm_fp.write("@R13" + "\n")
        self.__asm_fp.write("D=D+M" + "\n")

    def __subtraction(self):
        self.__asm_fp.write("@R13" + "\n")
        self.__asm_fp.write("D=D-M" + "\n")

    def __negation(self):
        self.__asm_fp.write("D=-D" + "\n")

    def __logicalAND(self):
        self.__asm_fp.write("@R13" + "\n")
        self.__asm_fp.write("D=D&M" + "\n")

    def __logicalOR(self):
        self.__asm_fp.write("@R13" + "\n")
        self.__asm_fp.write("D=D|M" + "\n")

    def __logicalNOT(self):
        self.__asm_fp.write("D=!D" + "\n")

    def __check_eq(self):
        self.__cond_opt_cnt = self.__cond_opt_cnt + 1

        self.__asm_fp.write("@EQUAL_" + str(self.__cond_opt_cnt) + "\n")
        self.__asm_fp.write("D;JEQ" + "\n")

        # if (D!=0): set D=0 (false)
        self.__asm_fp.write("D=0" + "\n")
        self.__asm_fp.write("@END_OF_COMPARISON_" + str(self.__cond_opt_cnt) + "\n")
        self.__asm_fp.write("0;JMP" + "\n")

        # if (D==0): set D=-1 i.e 0xFFFFFFFF (true)
        self.__asm_fp.write("(EQUAL_" + str(self.__cond_opt_cnt) + ")" + "\n")
        self.__asm_fp.write("D=-1" + "\n")

        self.__asm_fp.write("(END_OF_COMPARISON_" + str(self.__cond_opt_cnt) + ")" + "\n")

    def __check_gt(self):
        self.__cond_opt_cnt = self.__cond_opt_cnt + 1

        self.__asm_fp.write("@GREATER_THAN_" + str(self.__cond_opt_cnt) + "\n")
        self.__asm_fp.write("D;JGT" + "\n")

        # if (D<=0): set D=0 (false)
        self.__asm_fp.write("D=0" + "\n")

        self.__asm_fp.write("@END_OF_COMPARISON_" + str(self.__cond_opt_cnt) + "\n")
        self.__asm_fp.write("0;JMP" + "\n")

        # if (D>0): set D=-1 (true)
        self.__asm_fp.write("(GREATER_THAN_" + str(self.__cond_opt_cnt) + ")" + "\n")
        self.__asm_fp.write("D=-1" + "\n")

        self.__asm_fp.write("(END_OF_COMPARISON_" + str(self.__cond_opt_cnt) + ")" + "\n")

    def __check_lt(self):
        self.__cond_opt_cnt = self.__cond_opt_cnt + 1

        self.__asm_fp.write("@LESS_THAN_" + str(self.__cond_opt_cnt) + "\n")
        self.__asm_fp.write("D;JLT" + "\n")

        # if (D>=0): set D=0 (false)
        self.__asm_fp.write("D=0" + "\n")

        self.__asm_fp.write("@END_OF_COMPARISON_" + str(self.__cond_opt_cnt) + "\n")
        self.__asm_fp.write("0;JMP" + "\n")

        # if (D<0): set D=-1 i.e 0xFFFFFFFF (true)
        self.__asm_fp.write("(LESS_THAN_" + str(self.__cond_opt_cnt) + ")" + "\n")
        self.__asm_fp.write("D=-1" + "\n")

        self.__asm_fp.write("(END_OF_COMPARISON_" + str(self.__cond_opt_cnt) + ")" + "\n")

    # ARITHMETIC functions : END
    #################################

    #################################
    # UTILITY functions : START
    def __storeOperand2(self):
        # Store operand2 to R13 register
        self.__asm_fp.write("@R13" + "\n")
        self.__asm_fp.write("M=D" + "\n")

    def writeAsmInstructionComment(self, asmInstruction):
        self.__asm_fp.write("\n//" + asmInstruction)

    def __endProgram(self):
        self.__asm_fp.write("\n// END OF PROGRAM" + "\n")
        self.__asm_fp.write("(END_OF_PROGRAM)" + "\n")
        self.__asm_fp.write("@END_OF_PROGRAM" + "\n")
        self.__asm_fp.write("0;JMP" + "\n")

    def closeOutputFile(self):
        self.__endProgram()
        self.__asm_fp.close()

    # UTILITY functions : END
    #################################