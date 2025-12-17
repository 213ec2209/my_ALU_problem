# \# ALU Documentation

# 

# \## Overview

# 

# An Arithmetic Logic Unit (ALU) is a fundamental digital circuit used to perform arithmetic and logical operations on binary data. The ALU forms a core component of processors, controllers, and cryptographic hardware modules. It operates on two input operands and produces a result based on a selected operation. Typical ALU operations include addition, subtraction, bitwise logical functions, and comparison operations. The ALU described in this document is an 8-bit Asynchronous ALU that performs operations on two 8-bit inputs. The result is registered as combinational type.

# 

# 

# 

# 

# 

# In order to understand the ALU functionality, the following parameters are required:

# 

# First operand (A)

# 

# 

# 

# Second operand (B)

# 

# 

# 

# Operation select (op)

# 

# 

# 

# ALU result (Y)

# 

# 

# 

# 

# 

# 

# 

# The ALU performs different arithmetic and logical operations based on the value of the operation select signal op. All operations are executed synchronously on the rising edge of the clock.

# 

# 

# 

# The ALU operation is defined as follows:

# 

# 

# 

# the ALU samples inputs A, B, and op

# 

# 

# 

# Based on op, the corresponding operation is performed

# 

# 

# 

# The computed result is stored in output register Y

# 

# 

# 

# Operation Encoding

# 

# op	Operation	Description

# 

# 000	ADD	Addition of A and B

# 

# 001	SUB	Subtraction of B from A

# 

# 010	AND	Bitwise AND

# 

# 011	OR	Bitwise OR

# 

# 100	XOR	Bitwise XOR

# 

# 101	SLT	Set Less Than (unsigned comparison)

# 

# Others	DEFAULT	Output forced to zero

# 

# 

# 

# 

# 

# 

# 

# Functionality

# 

# 

# 

# The ALU module accepts two 8-bit input operands (A and B) and a 3-bit operation selector (op). Based on the value of op the ALU computes the corresponding arithmetic or logical operation and produces an 8-bit output (Y).

# 

# Inputs

# 

# 

# 

# A : 8-bit input operand

# 

# 

# 

# B : 8-bit input operand

# 

# 

# 

# op : 3-bit operation selector

# 

# 

# 

# Outputs

# 

# 

# 

# Y : 8-bit result of the selected operation

# 

# 

# 

# 

# 

# 

# 

# Arithmetic Operations

# 

# 

# 

# Addition (ADD) and subtraction (SUB) are performed using standard 8-bit arithmetic.

# 

# 

# 

# Overflow is ignored and truncated to 8 bits.

# 

# 

# 

# Logical Operations

# 

# 

# 

# Bitwise logical operations include AND, OR, and XOR.

# 

# 

# 

# Each operation is performed independently on corresponding bits of the operands.

# 

# 

# 

# Set-on-Less-Than (SLT)

# 

# 

# 

# The SLT operation compares operands A and B.

# 

# 

# 

# If A is less than B, the output is set to 8'd1; otherwise, it is set to 8'd0.

# 

# 

# 

# The comparison is performed as an unsigned comparison.

# 

# 

# 

# Default Case Handling

# 

# 

# 

# For undefined operation codes, the output is set to zero.

# 

# 

# 

# \### 

# 

# ALU Operation Algorithm

# 

# 

# 

# The ALU computation follows the steps below:

# 

# 

# 

# Step 1 — Input Sampling

# 

# 

# 

# The operands A and B, along with the operation code op, are sampled.

# 

# 

# 

# Step 2 — Operation Decode

# 

# 

# 

# The operation code determines which arithmetic or logical function is executed.

# 

# 

# 

# Step 3 — Result Computation

# 

# 

# 

# Depending on op, the ALU computes:

# 

# 

# 

# The ALU operations can be expressed as:

# 

# 

# 

# ADD:

# 

# Y = A + B

# 

# 

# 

# SUB:

# 

# Y = A − B

# 

# 

# 

# AND:

# 

# Y = A ∧ B

# 

# 

# 

# OR:

# 

# Y = A ∨ B

# 

# 

# 

# XOR:

# 

# Y = A ⊕ B

# 

# 

# 

# SLT:

# 

# Y = 1 if A < B else 0 (unsigned comparison)

# 

# 

# 

# Step 4 — Default Handling

# 

# 

# 

# If op does not match a valid operation, the output is set to zero.

# 

# Y=0

# 

# 

# 

# 

# 

# The ALU algorithm works as follows:

# if op == 000:

# 

#     Y = A + B

# 

# elif op == 001:

# 

#     Y = A - B

# 

# elif op == 010:

# 

#     Y = A \\\& B

# 

# elif op == 011:

# 

#     Y = A | B

# 

# elif op == 100:

# 

#     Y = A ^ B

# 

# elif op == 101:

# 

#     if A < B:

# 

#         Y = 1

# 

#     else:

# 

#         Y = 0

# 

# else:

# 

#     Y = 0

# 

# Here, < : unsigned compare + : 8 bit addition -: 8-bit subtraction |: 8-bit or operation \\\&: 8-bit and operation ^: 8-bit XOR operation:{} : Concatenation

# 

# The ALU module provides a compact and efficient implementation of basic arithmetic and logical operations for 8-bit data paths. Its fully combinational nature ensures low latency and easy integration into larger digital systems. The inclusion of a zero flag enables straightforward control-flow decisions, making the module suitable for simple processors, controllers, and RTL problem benchmarks.

# 

# 

# 

# 

# 

# FSM-Controlled Process

# 

# The ALU operates in a single-state synchronous process controlled entirely by the clock signal.

# 

# 

# 

# There is no explicit multi-state FSM

# 

# 

# 

# 

# 

# 

# 

# The output Y is updated when all input and op get

# 

# 

# 

# 

# 

# \## 

# 

# \## Working example

# 

# 

# 

# Example 1 — Addition

# 

# A = 8'd10

# 

# B = 8'd5

# 

# op = 3'b000 (ADD)

# 

# 

# 

# Y = 15

# 

# 

# 

# 

# 

# Example 2 — Bitwise AND

# 

# A = 8'b10101010

# 

# B = 8'b11001100

# 

# op = 3'b010 (AND)

# 

# 

# 

# Y = 8'b10001000

# 

# 

# 

# 

# 

# Example 3 — Set-on-Less-Than

# 

# A = 8'd3

# 

# B = 8'd7

# 

# op = 3'b101 (SLT)

# 

# 

# 

# Y = 1

# 

# 

# 

# 

# 

# Example 4 — Default Operation

# 

# A = 8'd12

# 

# B = 8'd4

# 

# op = 3'b111 (Invalid)

# 

# 

# 

# Y = 0

# 

# 

# 

# 

# 

# 

# 

# 

# 

# ALU operation

# 

# Let us consider the following parameters:

# 

# A = 8'h12; B= 8'h10 ;op=3'b000;

# 

# Solution:

# A = 8'h12;

# B=  8'h10;

# 

# Y = A + B

# 

#   = 8'h12 + 8'h10

# 

#   = 8'h22

# 

# The ALY output Y is  = 8'h22



