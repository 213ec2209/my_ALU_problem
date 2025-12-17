import cocotb
from cocotb.triggers import Timer

@cocotb.test()
async def test_alu_operations(dut):
    """Test all operations of 8-bit ALU"""

    test_vectors = [
        (0x12, 0x10, 0b000, 0x22),
        (0x12, 0x10, 0b001, 0x02),
        (0x12, 0x10, 0b010, 0x10),
        (0x12, 0x10, 0b011, 0x12),
        (0x12, 0x10, 0b100, 0x02),
        (0x12, 0x10, 0b101, 0x00),
        (0x05, 0x10, 0b101, 0x01),
    ]

    for A_val, B_val, op_val, expected in test_vectors:
        dut.A.value = A_val
        dut.B.value = B_val
        dut.op.value = op_val

        await Timer(1, unit="ns")  # delta-cycle settle

        assert dut.Y.value.is_resolvable, (
            f"Y not resolvable: A={A_val:02X}, B={B_val:02X}, op={op_val:03b}"
        )

        result = int(dut.Y.value)

        assert result == expected, (
            f"FAIL: A={A_val:02X}, B={B_val:02X}, "
            f"op={op_val:03b}, Y={result:02X}, exp={expected:02X}"
        )

        dut._log.info(
            f"PASS: A={A_val:02X}, B={B_val:02X}, "
            f"op={op_val:03b} => Y={result:02X}"
        )

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