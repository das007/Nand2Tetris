// This file is part of www.nand2tetris.org
// and the book "The Elements of Computing Systems"
// by Nisan and Schocken, MIT Press.
// File name: projects/04/Fill.asm

// Runs an infinite loop that listens to the keyboard input.
// When a key is pressed (any key), the program blackens the screen,
// i.e. writes "black" in every pixel;
// the screen should remain fully black as long as the key is pressed. 
// When no key is pressed, the program clears the screen, i.e. writes
// "white" in every pixel;
// the screen should remain fully clear as long as no key is pressed.

// Set SCREEN_SIZE = 24576
@24576
D=A
@SCREEN_SIZE
M=D

// Infinite LOOP listening to Keyboard press event
(KBD_LISTENER)

// Read KBD
@KBD
D=M

// if (KBD != 0) then "Paint the screen black"
@SCREEN_BLACK
D;JNE

// else if (KBD == 0) then "Paint the screen white"
@SCREEN_WHITE
D;JEQ

// Keep checking for keyboard events
@KBD_LISTENER
0;JMP


////////////////////////////////
// Code to make the screen black
////////////////////////////////
(SCREEN_BLACK)

// Set SCREEN_REG = 16384
@16384
D=A
@SCREEN_REG
M=D

(LOOP1)

// Set SCREEN Byte = -1 >> BLACK
@SCREEN_REG
D=M
A=D
M=-1

// increment screen register
@SCREEN_REG
M=M+1
D=M

// Check if whole screen is painted
@SCREEN_SIZE
D=M-D

// If Not then keep painting black
@LOOP1
D;JNE

// Else Jump to KBD_LISTENER and check for next keyboard event
@KBD_LISTENER
0;JMP

////////////////////////////////
// Code to make the screen white
////////////////////////////////
(SCREEN_WHITE)

// Set SCREEN_REG = 16384
@16384
D=A
@SCREEN_REG
M=D

(LOOP2)

// Set SCREEN Byte = 0 >> WHITE
@SCREEN_REG
D=M
A=D
M=0

// increment screen register
@SCREEN_REG
M=M+1
D=M

// Check if whole screen is painted
@SCREEN_SIZE
D=M-D

// If Not then keep painting white
@LOOP2
D;JNE

// Else Jump to KBD_LISTENER and check for next keyboard event
@KBD_LISTENER
0;JMP

/////////////////////