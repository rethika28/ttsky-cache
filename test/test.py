import cocotb
from cocotb.triggers import Timer


@cocotb.test()
async def cache_test(dut):

    dut.ui_in.value = 0
    dut.uio_in.value = 0
    dut.ena.value = 1
    dut.clk.value = 0
    dut.rst_n.value = 0

    await Timer(10, units="ns")

    dut.rst_n.value = 1

    # Write value 25 to address 2
    dut.ui_in.value = (25 << 2) | 0b10
    dut.uio_in.value = 1

    # Clock pulse
    dut.clk.value = 1
    await Timer(10, units="ns")

    dut.clk.value = 0
    await Timer(10, units="ns")

    # Disable write
    dut.uio_in.value = 0

    # Read address 2
    dut.ui_in.value = 0b10

    await Timer(10, units="ns")

    result = dut.uo_out.value.integer

    print("Cache Output =", result)

    assert result == 25
