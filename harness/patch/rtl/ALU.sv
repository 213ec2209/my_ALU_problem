
`timescale 1ns/1ps
module ALU (
    input  logic [7:0] A,// first input
    input   logic[7:0] B, //second input
    input  logic [2:0] op,//which operation
    output  logic [7:0] Y//output of alu operation
);

   always_comb 
 begin
y=8'h00;
 case (op)
            3'b000: Y = A + B;                 // ADD
            3'b001: Y = A - B;                 // SUB
            3'b010: Y = A & B;                 // AND
            3'b011: Y = A | B;                 // OR
            3'b100: Y = A ^ B;                 // XOR
            3'b101: Y = (A < B) ? 8'd1 : 8'd0; // SLT 
            default: Y = 8'd0;
       
endcase
   end  
endmodule


