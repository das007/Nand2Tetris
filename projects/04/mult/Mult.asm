// This file is part of www.nand2tetris.org
// and the book "The Elements of Computing Systems"
// by Nisan and Schocken, MIT Press.
// File name: projects/04/Mult.asm

// Multiplies R0 and R1 and stores the result in R2.
// (R0, R1, R2 refer to RAM[0], RAM[1], and RAM[2], respectively.)
//
// This program only needs to handle arguments that satisfy
// R0 >= 0, R1 >= 0, and R0*R1 < 32768.


// Pseudo Code for multiplying 2 integers:
// R0=5, R1=2;
// R2=0;
// i=0;

// for(i=0; i<R1; i++)
// {
	// R2 += R0
// }

// R2 stores the final multiplication result


// set i=0
@i
M=0

// set R2=0
@R2
M=0

// LOOP start
(LOOP)

// D = i
@i
D=M

// D = R1 - i
@R1
D=M-D

@END
D;JEQ // if (i<R1) JMP to END

// D = R0
@R0
D=M

// R2 = R2+R0
@R2
M=D+M

// i = i+1
@i
M=M+1

@LOOP
0;JMP // JMP to start of LOOP

// End of Program
(END)
@END
0;JMP