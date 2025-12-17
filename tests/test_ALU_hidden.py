import cocotb
from cocotb.triggers import Timer

@cocotb.test()
async def test_alu_operations(dut):
    """Test all operations of 8-bit ALU"""

    test_vectors = [
        (0x12, 0x10, 0b000, 0x22),  # ADD
        (0x12, 0x10, 0b001, 0x02),  # SUB
        (0x12, 0x10, 0b010, 0x10),  # AND
        (0x12, 0x10, 0b011, 0x12),  # OR
        (0x12, 0x10, 0b100, 0x02),  # XOR
        (0x12, 0x10, 0b101, 0x00),  # SLT
        (0x05, 0x10, 0b101, 0x01),  # SLT (A<B)
    ]

    for A_val, B_val, op_val, expected in test_vectors:
        dut.A.value = A_val
        dut.B.value = B_val
        dut.op.value = op_val

        await Timer(1, unit="ns")  # wait for combinational logic

        assert dut.Y.value.to_unsigned() == expected, \
            f"ALU failed for A={A_val}, B={B_val}, op={op_val:03b}: expected {expected}, got {dut.Y.value.to_unsigned()}"

        dut._log.info(f"PASS: A={A_val:02X}, B={B_val:02X}, op={op_val:03b} => Y={dut.Y.value.to_unsigned():02X}")

# CRITICAL: Pytest wrapper function
def test_ALU_hidden_runner():
    import os
    from pathlib import Path
    from cocotb_tools.runner import get_runner
    
    sim = os.getenv("SIM", "icarus")
    proj_path = Path(__file__).resolve().parent.parent
    
    sources = [proj_path / "sources/ALU.sv"]  # Note: sources/ not rtl/
    
    runner = get_runner(sim)
    runner.build(
        sources=sources,
        hdl_toplevel="ALU",
        always=True,
    )
    runner.test(
        hdl_toplevel="ALU",
        test_module="test_ALU_hidden"
    )

