import cocotb
from cocotb.triggers import Timer


@cocotb.test()
async def cache_test(dut):

    # Initialize
    dut.ui_in.value = 0
    dut.uio_in.value = 0
    dut.ena.value = 1
    dut.clk.value = 0
    dut.rst_n.value = 0

    # Apply reset
    await Timer(10, units="ns")

    dut.clk.value = 1
    await Timer(10, units="ns")

    dut.clk.value = 0
    dut.rst_n.value = 1

    await Timer(10, units="ns")

    # --------------------------------
    # WRITE value 25 at address 2
    # --------------------------------

    dut.ui_in.value = (25 << 2) | 0b10
    dut.uio_in.value = 1

    # clock edge
    dut.clk.value = 1
    await Timer(10, units="ns")

    dut.clk.value = 0
    await Timer(10, units="ns")

    # --------------------------------
    # READ from address 2
    # --------------------------------

    dut.uio_in.value = 0
    dut.ui_in.value = 0b10

    await Timer(10, units="ns")

    # Read output safely
    result = dut.uo_out.value.binstr

    cocotb.log.info(f"Cache Output Binary = {result}")

    # Expected = 00011001 (25)
    assert result == "00011001"
