ALU Documentation
Overview


An Arithmetic Logic Unit (ALU) is a fundamental digital circuit used to perform arithmetic and logical operations on binary data. It is a core component of processors, microcontrollers, and digital systems. The ALU accepts binary operands and an operation-select control signal, and it produces a result based on the selected operation.


In this project, an 8-bit combinational ALU is specified. The ALU performs arithmetic and bitwise logical operations on two 8-bit unsigned inputs. The design is purely combinational, meaning the output responds immediately to changes in inputs without relying on clock signals, reset signals, or sequential elements. This ALU is intended for evaluation of an AI agent’s ability to correctly interpret specifications and implement digital logic from scratch.


Functionality
ALU algorthim

In order to understand the ALU functionality, the following parameters are required:

First operand (A)
 Second operand (B) 
 Operation selection (op)
 ALU result (Y)


The ALU algorithm works as follows:
Y = 0;
case (op)
    000: Y = A + B;
    001: Y = A − B;
    010: Y = A & B;
    011: Y = A | B;
    100: Y = A ^ B;
    101: Y = (A < B) ? 1 : 0;
    default: Y = 0;
endcase

Here, < : Unsigned comparison operator + : 8-bit unsigned addition (result truncated to 8 bits) -: 8-bit unsigned subtraction (result truncated to 8 bits) |: Bitwise OR operation &: Bitwise AND operation ^: Bitwise XOR operation; A : First 8-bit input operand; B : Second 8-bit input operand; op : 3-bit operation select signal; Y : 8-bit ALU output result

At the beginning of ALU operation output Y is inttial assigned to zero value.All ALU operations are purely combinational. The output is computed directly from the current values of inputs A, B, and op, with no dependency on previous computations.

FSM-Controlled Process
there is no explicit multi-state FSM 

Working example
Let us consider the following parameters:
A = 8'h10;B=8'h12;op=3'b000;

Solution:
A=8'h10;B=8'h12
Y= A + B;
The ALU ouput is Y = 8'h22;




