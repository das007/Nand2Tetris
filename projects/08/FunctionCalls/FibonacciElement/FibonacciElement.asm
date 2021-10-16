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

// ASM code for File : Main.vm

//function Main.fibonacci 0
(Main.fibonacci)
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

//push constant 2
@2
D=A
@SP
A=M
M=D
@SP
M=M+1

//lt                     // checks if n<2
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
@LESS_THAN_1
D;JLT
D=0
@END_OF_COMPARISON_1
0;JMP
(LESS_THAN_1)
D=-1
(END_OF_COMPARISON_1)
@SP
A=M
M=D
@SP
M=M+1

//if-goto IF_TRUE
@SP
M=M-1
@SP
A=M
D=M
@IF_TRUE
D;JNE

//goto IF_FALSE
@IF_FALSE
0;JMP

//label IF_TRUE          // if n<2, return n
(IF_TRUE)

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

//label IF_FALSE         // if n>=2, returns fib(n-2)+fib(n-1)
(IF_FALSE)

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

//push constant 2
@2
D=A
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

//call Main.fibonacci 1  // computes fib(n-2)
@Main.fibonacci$ret.2
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
@1
D=D-A
@ARG
M=D
@SP
D=M
@LCL
M=D
@Main.fibonacci
0;JMP
(Main.fibonacci$ret.2)

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

//push constant 1
@1
D=A
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

//call Main.fibonacci 1  // computes fib(n-1)
@Main.fibonacci$ret.3
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
@1
D=D-A
@ARG
M=D
@SP
D=M
@LCL
M=D
@Main.fibonacci
0;JMP
(Main.fibonacci$ret.3)

//add                    // returns fib(n-1) + fib(n-2)
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
D=D+M
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

//push constant 4
@4
D=A
@SP
A=M
M=D
@SP
M=M+1

//call Main.fibonacci 1   // computes the 4'th fibonacci element
@Main.fibonacci$ret.4
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
@1
D=D-A
@ARG
M=D
@SP
D=M
@LCL
M=D
@Main.fibonacci
0;JMP
(Main.fibonacci$ret.4)

//label WHILE
(WHILE)

//goto WHILE              // loops infinitely
@WHILE
0;JMP

// END OF PROGRAM
(END_OF_PROGRAM)
@END_OF_PROGRAM
0;JMP
