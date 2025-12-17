`timescale 1ns/1ps
module ALU (
    input  logic [7:0] A,
    input  logic [7:0] B,
    input  logic [2:0] op,
    output logic [7:0] Y
);

    always_comb begin
        Y = 8'h00;
        case (op)
            3'b000: Y = A + B;
            3'b001: Y = A - B;
            3'b010: Y = A & B;
            3'b011: Y = A | B;
            3'b100: Y = A ^ B;
            3'b101: Y = (A < B) ? 8'd1 : 8'd0;
            default: Y = 8'd0;
        endcase
    end

endmodule
