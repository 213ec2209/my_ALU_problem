`timescale 1ns/1ps
module ALU (
    input  logic [7:0] A,// first input
    input  logic [7:0] B, //second input
    input  logic [2:0] op,//which operation
    output logic [7:0] Y //output of alu operation
);

    always_comb begin
        Y = 8'h00;
        case (op)
            3'b000: Y = A + B;  // ADD - implemented
            3'b001: Y = 8'd0;   // SUB - TODO: implement A - B
            3'b010: Y = A & B;  // AND - implemented
            3'b011: Y = 8'd0;   // OR - TODO: implement A | B
            3'b100: Y = 8'd0;   // XOR - TODO: implement A ^ B
            3'b101: Y = 8'd0;   // SLT - TODO: implement (A < B) ? 8'd1 : 8'd0
            default: Y = 8'd0;
        endcase
    end

endmodule
