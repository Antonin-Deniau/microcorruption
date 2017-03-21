One-operand instructions:
=========================

RRC(.B)	9-bit rotate right through carry. C->msbit->...->lsbit->C. Clear the carry bit beforehand to do a logical right shift.
SWPB	Swap 8-bit register halves. No byte form.
RRA(.B)	Badly named, this is an 8-bit arithmetic right shift.
SXT	Sign extend 8 bits to 16. No byte form.
PUSH(.B)	Push operand on stack. Push byte decrements SP by 2. CPU BUG: PUSH #4 and PUSH #8 do not work when the short encoding using @r2 and @r2+ is used. The workaround, to use a 16-bit immediate, is trivial, so TI do not plan to fix this bug.
CALL	Fetch operand, push PC, then assign operand value to PC. Note the immediate form is the most commonly used. There is no easy way to perform a PC-relative call; the PC-relative addressing mode fetches a word and uses it as an absolute address. This has no byte form.
RETI	Pop SP, then pop PC. Note that because flags like CPUOFF are in the stored status register, the CPU will normally return to the low-power mode it was previously in. This can be changed by adjusting the SR value stored on the stack before invoking RETI (see below). The operand field is unused.

Relative jumps:
===============

JNE/JNZ	Jump if Z==0 (if !=)
JEQ/Z	Jump if Z==1 (if ==)
JNC/JLO	Jump if C==0 (if unsigned <)
JC/JHS	Jump if C==1 (if unsigned >=)
JN	Jump if N==1 Note there is no "JP" if N==0!
JGE	Jump if N==V (if signed >=)
JL	Jump if N!=V (if signed <)
JMP	Jump unconditionally

Two-operand instructions:
=========================

MOV src,dest	dest = src	The status flags are NOT set.
ADD src,dest	dest += src	 
ADDC src,dest	dest += src + C	 
SUBC src,dest	dest += ~src + C	 
SUB src,dest	dest -= src	Implemented as dest += ~src + 1.
CMP src,dest	dest - src	Sets status only; the destination is not written.
DADD src,dest	dest += src + C, BCD.	 
BIT src,dest	dest & src	Sets status only; the destination is not written.
BIC src,dest	dest &= ~src	The status flags are NOT set.
BIS src,dest	dest |= src	The status flags are NOT set.
XOR src,dest	dest ^= src	 
AND src,dest	dest &=- src

emulated ?:
===========

NOP	MOV r3,r3	Any register from r3 to r15 would do the same thing.
POP dst	MOV @SP+,dst	 

Branch and return can be done by moving to PC (r0):

BR dst	MOV dst,PC
RET	MOV @SP+,PC

The constants were chosen to make status register (r2) twiddling efficient:

CLRC	BIC #1,SR
SETC	BIS #1,SR
CLRZ	BIC #2,SR
SETZ	BIS #2,SR
CLRN	BIC #4,SR
SETN	BIS #4,SR
DINT	BIC #8,SR
EINT	BIC #8,SR

Shift and rotate left is done with add:
=======================================

RLA(.B) dst	ADD(.B) dst,dst
RLC(.B) dst	ADDC(.B) dst,dst

Some common one-operand instructions:
=====================================

INV(.B) dst	XOR(.B) #-1,dst
CLR(.B) dst	MOV(.B) #0,dst
TST(.B) dst	CMP(.B) #0,dst

Increment and decrement (by one or two):
========================================

DEC(.B) dst	SUB(.B) #1,dst
DECD(.B) dst	SUB(.B) #2,dst
INC(.B) dst	ADD(.B) #1,dst
INCD(.B) dst	ADD(.B) #2,dst

Adding and subtracting only the carry bit:
==========================================

ADC(.B) dst	ADDC(.B) #0,dst
DADC(.B) dst	DADD(.B) #0,dst
SBC(.B) dst	SUBC(.B) #0,dst
