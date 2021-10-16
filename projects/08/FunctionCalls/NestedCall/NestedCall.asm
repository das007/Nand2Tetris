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

// ASM code for File : Sys.vm

//function Sys.init 0
(Sys.init)
// Initializing 0 local variables to 0

//push constant 4000	// test THIS and THAT context save
@4000
D=A
@SP
A=M
M=D
@SP
M=M+1

//pop pointer 0
@SP
M=M-1
@SP
A=M
D=M
@THIS
M=D

//push constant 5000
@5000
D=A
@SP
A=M
M=D
@SP
M=M+1

//pop pointer 1
@SP
M=M-1
@SP
A=M
D=M
@THAT
M=D

//call Sys.main 0
@Sys.main$ret.1
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
@Sys.main
0;JMP
(Sys.main$ret.1)

//pop temp 1
@SP
M=M-1
@SP
A=M
D=M
@6
M=D

//label LOOP
(LOOP)

//goto LOOP
@LOOP
0;JMP

//function Sys.main 5
(Sys.main)
// Initializing 5 local variables to 0
D=0
@SP
A=M
M=D
@SP
M=M+1
@SP
A=M
M=D
@SP
M=M+1
@SP
A=M
M=D
@SP
M=M+1
@SP
A=M
M=D
@SP
M=M+1
@SP
A=M
M=D
@SP
M=M+1

//push constant 4001
@4001
D=A
@SP
A=M
M=D
@SP
M=M+1

//pop pointer 0
@SP
M=M-1
@SP
A=M
D=M
@THIS
M=D

//push constant 5001
@5001
D=A
@SP
A=M
M=D
@SP
M=M+1

//pop pointer 1
@SP
M=M-1
@SP
A=M
D=M
@THAT
M=D

//push constant 200
@200
D=A
@SP
A=M
M=D
@SP
M=M+1

//pop local 1
@LCL
D=M
@1
D=D+A
@R13
M=D
@SP
M=M-1
@SP
A=M
D=M
@R13
A=M
M=D

//push constant 40
@40
D=A
@SP
A=M
M=D
@SP
M=M+1

//pop local 2
@LCL
D=M
@2
D=D+A
@R13
M=D
@SP
M=M-1
@SP
A=M
D=M
@R13
A=M
M=D

//push constant 6
@6
D=A
@SP
A=M
M=D
@SP
M=M+1

//pop local 3
@LCL
D=M
@3
D=D+A
@R13
M=D
@SP
M=M-1
@SP
A=M
D=M
@R13
A=M
M=D

//push constant 123
@123
D=A
@SP
A=M
M=D
@SP
M=M+1

//call Sys.add12 1
@Sys.add12$ret.2
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
@Sys.add12
0;JMP
(Sys.add12$ret.2)

//pop temp 0
@SP
M=M-1
@SP
A=M
D=M
@5
M=D

//push local 0
@LCL
D=M
@0
A=D+A
D=M
@SP
A=M
M=D
@SP
M=M+1

//push local 1
@LCL
D=M
@1
A=D+A
D=M
@SP
A=M
M=D
@SP
M=M+1

//push local 2
@LCL
D=M
@2
A=D+A
D=M
@SP
A=M
M=D
@SP
M=M+1

//push local 3
@LCL
D=M
@3
A=D+A
D=M
@SP
A=M
M=D
@SP
M=M+1

//push local 4
@LCL
D=M
@4
A=D+A
D=M
@SP
A=M
M=D
@SP
M=M+1

//add
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

//add
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

//add
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

//add
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

//function Sys.add12 0
(Sys.add12)
// Initializing 0 local variables to 0

//push constant 4002
@4002
D=A
@SP
A=M
M=D
@SP
M=M+1

//pop pointer 0
@SP
M=M-1
@SP
A=M
D=M
@THIS
M=D

//push constant 5002
@5002
D=A
@SP
A=M
M=D
@SP
M=M+1

//pop pointer 1
@SP
M=M-1
@SP
A=M
D=M
@THAT
M=D

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

//push constant 12
@12
D=A
@SP
A=M
M=D
@SP
M=M+1

//add
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

// END OF PROGRAM
(END_OF_PROGRAM)
@END_OF_PROGRAM
0;JMP
