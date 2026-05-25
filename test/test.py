import cocotb
from cocotb.triggers import Timer


@cocotb.test()
async def cache_test(dut):

    # Initialize signals
    dut.ui_in.value = 0
    dut.uio_in.value = 0
    dut.ena.value = 1
    dut.clk.value = 0
    dut.rst_n.value = 0

    # Reset
    await Timer(10, units="ns")
    dut.rst_n.value = 1

    # -----------------------------
    # WRITE: Store 25 at address 2
    # -----------------------------

    # data = 25
    # address = 2

    dut.ui_in.value = (25 << 2) | 0b10
    dut.uio_in.value = 1

    # clock pulse
    dut.clk.value = 1
    await Timer(10, units="ns")

    dut.clk.value = 0
    await Timer(10, units="ns")

    # -----------------------------
    # READ
    # -----------------------------

    dut.uio_in.value = 0
    dut.ui_in.value = 0b10

    await Timer(10, units="ns")

    result = dut.uo_out.value.integer

    cocotb.log.info(f"Cache Output = {result}")

    assert result == 25
