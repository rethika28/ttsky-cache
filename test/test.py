import cocotb
from cocotb.triggers import RisingEdge


@cocotb.test()
async def cache_test(dut):

    # Initialize
    dut.ui_in.value = 0
    dut.uio_in.value = 0
    dut.ena.value = 1
    dut.rst_n.value = 0
    dut.clk.value = 0

    # Reset
    for _ in range(2):
        dut.clk.value = 0
        await RisingEdge(dut.clk)

    dut.rst_n.value = 1

    # Write value 25 to address 2
    # ui_in[7:2] = data
    # ui_in[1:0] = address

    dut.ui_in.value = (25 << 2) | 0b10
    dut.uio_in.value = 1

    # Clock pulse for write
    dut.clk.value = 1
    await RisingEdge(dut.clk)

    dut.clk.value = 0

    # Disable write
    dut.uio_in.value = 0

    # Read from address 2
    dut.ui_in.value = 0b10

    await RisingEdge(dut.clk)

    result = int(dut.uo_out.value)

    print("Cache Output =", result)

    assert result == 25, f"Expected 25 but got {result}"
