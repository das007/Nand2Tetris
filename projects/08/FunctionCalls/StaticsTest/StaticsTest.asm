// Bootstrap Code

// Set SP=256
@256
D=A
@SP
M=D

// Call Sys.init
@Sys.init$ret.1
D=A
@SP
A=M
M=D
@SP
M=M+1
// Push LCL on Stack
@LCL
D=M
@SP
A=M
M=D
@SP
M=M+1
// Push ARG on Stack
@ARG
D=M
@SP
A=M
M=D
@SP
M=M+1
// Push THIS on Stack
@THIS
D=M
@SP
A=M
M=D
@SP
M=M+1
// Push THAT on Stack
@THAT
D=M
@SP
A=M
M=D
@SP
M=M+1
// ARG = SP - 5 - nArgs
@5
D=A
@SP
D=M-D
@0
D=D-A
@ARG
M=D
@SP
D=M
@LCL
M=D
@Sys.init
0;JMP
(Sys.init$ret.1)

// ASM code for File : Class1.vm

//function Class1.set 0
(Class1.set)
// Initializing 0 local variables to 0

//push argument 0
@ARG
D=M
@0
A=D+A
D=M
@SP
A=M
M=D
@SP
M=M+1

//pop static 0
@SP
M=M-1
@SP
A=M
D=M
@Class1.0
M=D

//push argument 1
@ARG
D=M
@1
A=D+A
D=M
@SP
A=M
M=D
@SP
M=M+1

//pop static 1
@SP
M=M-1
@SP
A=M
D=M
@Class1.1
M=D

//push constant 0
@0
D=A
@SP
A=M
M=D
@SP
M=M+1

//return
@LCL
D=M
@R14
M=D
@5
D=A
@R14
D=M-D
A=D
D=M
@R15
M=D
@SP
M=M-1
@SP
A=M
D=M
@ARG
A=M
M=D
@ARG
D=M
@SP
M=D+1
// THAT = *(endFrame-1)
@R14
D=M
@1
A=D-A
D=M
@THAT
M=D
// THIS = *(endFrame-2)
@R14
D=M
@2
A=D-A
D=M
@THIS
M=D
// ARG = *(endFrame-3)
@R14
D=M
@3
A=D-A
D=M
@ARG
M=D
// LCL = *(endFrame-4)
@R14
D=M
@4
A=D-A
D=M
@LCL
M=D
// goto retAddr
@R15
A=M
0;JMP

//function Class1.get 0
(Class1.get)
// Initializing 0 local variables to 0

//push static 0
@Class1.0
D=M
@SP
A=M
M=D
@SP
M=M+1

//push static 1
@Class1.1
D=M
@SP
A=M
M=D
@SP
M=M+1

//sub
@SP
M=M-1
@SP
A=M
D=M
@R13
M=D
@SP
M=M-1
@SP
A=M
D=M
@R13
D=D-M
@SP
A=M
M=D
@SP
M=M+1

//return
@LCL
D=M
@R14
M=D
@5
D=A
@R14
D=M-D
A=D
D=M
@R15
M=D
@SP
M=M-1
@SP
A=M
D=M
@ARG
A=M
M=D
@ARG
D=M
@SP
M=D+1
// THAT = *(endFrame-1)
@R14
D=M
@1
A=D-A
D=M
@THAT
M=D
// THIS = *(endFrame-2)
@R14
D=M
@2
A=D-A
D=M
@THIS
M=D
// ARG = *(endFrame-3)
@R14
D=M
@3
A=D-A
D=M
@ARG
M=D
// LCL = *(endFrame-4)
@R14
D=M
@4
A=D-A
D=M
@LCL
M=D
// goto retAddr
@R15
A=M
0;JMP

// ASM code for File : Class2.vm

//function Class2.set 0
(Class2.set)
// Initializing 0 local variables to 0

//push argument 0
@ARG
D=M
@0
A=D+A
D=M
@SP
A=M
M=D
@SP
M=M+1

//pop static 0
@SP
M=M-1
@SP
A=M
D=M
@Class2.0
M=D

//push argument 1
@ARG
D=M
@1
A=D+A
D=M
@SP
A=M
M=D
@SP
M=M+1

//pop static 1
@SP
M=M-1
@SP
A=M
D=M
@Class2.1
M=D

//push constant 0
@0
D=A
@SP
A=M
M=D
@SP
M=M+1

//return
@LCL
D=M
@R14
M=D
@5
D=A
@R14
D=M-D
A=D
D=M
@R15
M=D
@SP
M=M-1
@SP
A=M
D=M
@ARG
A=M
M=D
@ARG
D=M
@SP
M=D+1
// THAT = *(endFrame-1)
@R14
D=M
@1
A=D-A
D=M
@THAT
M=D
// THIS = *(endFrame-2)
@R14
D=M
@2
A=D-A
D=M
@THIS
M=D
// ARG = *(endFrame-3)
@R14
D=M
@3
A=D-A
D=M
@ARG
M=D
// LCL = *(endFrame-4)
@R14
D=M
@4
A=D-A
D=M
@LCL
M=D
// goto retAddr
@R15
A=M
0;JMP

//function Class2.get 0
(Class2.get)
// Initializing 0 local variables to 0

//push static 0
@Class2.0
D=M
@SP
A=M
M=D
@SP
M=M+1

//push static 1
@Class2.1
D=M
@SP
A=M
M=D
@SP
M=M+1

//sub
@SP
M=M-1
@SP
A=M
D=M
@R13
M=D
@SP
M=M-1
@SP
A=M
D=M
@R13
D=D-M
@SP
A=M
M=D
@SP
M=M+1

//return
@LCL
D=M
@R14
M=D
@5
D=A
@R14
D=M-D
A=D
D=M
@R15
M=D
@SP
M=M-1
@SP
A=M
D=M
@ARG
A=M
M=D
@ARG
D=M
@SP
M=D+1
// THAT = *(endFrame-1)
@R14
D=M
@1
A=D-A
D=M
@THAT
M=D
// THIS = *(endFrame-2)
@R14
D=M
@2
A=D-A
D=M
@THIS
M=D
// ARG = *(endFrame-3)
@R14
D=M
@3
A=D-A
D=M
@ARG
M=D
// LCL = *(endFrame-4)
@R14
D=M
@4
A=D-A
D=M
@LCL
M=D
// goto retAddr
@R15
A=M
0;JMP

// ASM code for File : Sys.vm

//function Sys.init 0
(Sys.init)
// Initializing 0 local variables to 0

//push constant 6
@6
D=A
@SP
A=M
M=D
@SP
M=M+1

//push constant 8
@8
D=A
@SP
A=M
M=D
@SP
M=M+1

//call Class1.set 2
@Class1.set$ret.2
D=A
@SP
A=M
M=D
@SP
M=M+1
// Push LCL on Stack
@LCL
D=M
@SP
A=M
M=D
@SP
M=M+1
// Push ARG on Stack
@ARG
D=M
@SP
A=M
M=D
@SP
M=M+1
// Push THIS on Stack
@THIS
D=M
@SP
A=M
M=D
@SP
M=M+1
// Push THAT on Stack
@THAT
D=M
@SP
A=M
M=D
@SP
M=M+1
// ARG = SP - 5 - nArgs
@5
D=A
@SP
D=M-D
@2
D=D-A
@ARG
M=D
@SP
D=M
@LCL
M=D
@Class1.set
0;JMP
(Class1.set$ret.2)

//pop temp 0 // Dumps the return value
@SP
M=M-1
@SP
A=M
D=M
@5
M=D

//push constant 23
@23
D=A
@SP
A=M
M=D
@SP
M=M+1

//push constant 15
@15
D=A
@SP
A=M
M=D
@SP
M=M+1

//call Class2.set 2
@Class2.set$ret.3
D=A
@SP
A=M
M=D
@SP
M=M+1
// Push LCL on Stack
@LCL
D=M
@SP
A=M
M=D
@SP
M=M+1
// Push ARG on Stack
@ARG
D=M
@SP
A=M
M=D
@SP
M=M+1
// Push THIS on Stack
@THIS
D=M
@SP
A=M
M=D
@SP
M=M+1
// Push THAT on Stack
@THAT
D=M
@SP
A=M
M=D
@SP
M=M+1
// ARG = SP - 5 - nArgs
@5
D=A
@SP
D=M-D
@2
D=D-A
@ARG
M=D
@SP
D=M
@LCL
M=D
@Class2.set
0;JMP
(Class2.set$ret.3)

//pop temp 0 // Dumps the return value
@SP
M=M-1
@SP
A=M
D=M
@5
M=D

//call Class1.get 0
@Class1.get$ret.4
D=A
@SP
A=M
M=D
@SP
M=M+1
// Push LCL on Stack
@LCL
D=M
@SP
A=M
M=D
@SP
M=M+1
// Push ARG on Stack
@ARG
D=M
@SP
A=M
M=D
@SP
M=M+1
// Push THIS on Stack
@THIS
D=M
@SP
A=M
M=D
@SP
M=M+1
// Push THAT on Stack
@THAT
D=M
@SP
A=M
M=D
@SP
M=M+1
// ARG = SP - 5 - nArgs
@5
D=A
@SP
D=M-D
@0
D=D-A
@ARG
M=D
@SP
D=M
@LCL
M=D
@Class1.get
0;JMP
(Class1.get$ret.4)

//call Class2.get 0
@Class2.get$ret.5
D=A
@SP
A=M
M=D
@SP
M=M+1
// Push LCL on Stack
@LCL
D=M
@SP
A=M
M=D
@SP
M=M+1
// Push ARG on Stack
@ARG
D=M
@SP
A=M
M=D
@SP
M=M+1
// Push THIS on Stack
@THIS
D=M
@SP
A=M
M=D
@SP
M=M+1
// Push THAT on Stack
@THAT
D=M
@SP
A=M
M=D
@SP
M=M+1
// ARG = SP - 5 - nArgs
@5
D=A
@SP
D=M-D
@0
D=D-A
@ARG
M=D
@SP
D=M
@LCL
M=D
@Class2.get
0;JMP
(Class2.get$ret.5)

//label WHILE
(WHILE)

//goto WHILE
@WHILE
0;JMP

// END OF PROGRAM
(END_OF_PROGRAM)
@END_OF_PROGRAM
0;JMP
