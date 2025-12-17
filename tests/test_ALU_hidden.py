import cocotb
from cocotb.triggers import Timer


@cocotb.test()
async def test_alu_operations(dut):
    """Verify all operations of the 8-bit ALU"""

    test_vectors = [
        # A     B     op     expected Y
        (0x12, 0x10, 0b000, 0x22),  # ADD
        (0x12, 0x10, 0b001, 0x02),  # SUB
        (0x12, 0x10, 0b010, 0x10),  # AND
        (0x12, 0x10, 0b011, 0x12),  # OR
        (0x12, 0x10, 0b100, 0x02),  # XOR
        (0x12, 0x10, 0b101, 0x00),  # SLT (A >= B)
        (0x05, 0x10, 0b101, 0x01),  # SLT (A < B)
    ]

    for A_val, B_val, op_val, expected in test_vectors:
        dut.A.value = A_val
        dut.B.value = B_val
        dut.op.value = op_val

        # Allow combinational logic to settle
        await Timer(1, units="ns")

        # Explicit X/Z detection (critical for HUD)
        assert dut.Y.value.is_resolvable, (
            f"Y contains X/Z "
            f"(A=0x{A_val:02X}, B=0x{B_val:02X}, op={op_val:03b}, Y={dut.Y.value})"
        )

        # Functional correctness check
        result = dut.Y.value.to_unsigned()
        assert result == expected, (
            f"ALU mismatch: "
            f"A=0x{A_val:02X}, B=0x{B_val:02X}, op={op_val:03b}, "
            f"expected=0x{expected:02X}, got=0x{result:02X}"
        )

        dut._log.info(
            f"PASS: A=0x{A_val:02X}, B=0x{B_val:02X}, "
            f"op={op_val:03b} → Y=0x{result:02X}"
        )


# ------------------------------------------------------------
# Pytest runner wrapper (required for HUD hidden evaluation)
# ------------------------------------------------------------

def test_ALU_hidden_runner():
    import os
    from pathlib import Path
    from cocotb_tools.runner import get_runner

    sim = os.getenv("SIM", "icarus")
    project_root = Path(__file__).resolve().parent.parent

    sources = [
        project_root / "sources" / "ALU.sv"
    ]

    runner = get_runner(sim)

    runner.build(
        sources=sources,
        hdl_toplevel="ALU",
        always=True,
    )

    runner.test(
        hdl_toplevel="ALU",
        test_module="test_ALU_hidden",
    )
