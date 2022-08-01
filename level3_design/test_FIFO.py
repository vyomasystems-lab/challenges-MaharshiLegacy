# See LICENSE.vyoma for details

# SPDX-License-Identifier: CC0-1.0

import os
import random
from pathlib import Path

import cocotb
from cocotb.clock import Clock
from cocotb.triggers import RisingEdge, FallingEdge

@cocotb.test()
async def test_seq_bug1(dut):
    """Test for seq detection """

    clock = Clock(dut.clk, 10, units="us")  # Create a 10us period clock on port clk
    cocotb.start_soon(clock.start())        # Start the clock

      # reset
    #dut.EN.value = 1
    #await FallingEdge(dut.clk) 
    #dut.dataIn.value = 10

    #await FallingEdge(dut.clk) 
    
    #assert dut.EMPTY.value == 0, "WE HAVE NOT GIVEN INPUT DATA TO FIFO THAN ALSO FULL SHOW HIGH LOGIC --> {full}= ".format( full=int(dut.EMPTY.value))

