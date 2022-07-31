# See LICENSE.vyoma for details

# SPDX-License-Identifier: CC0-1.0

import os
import random
from pathlib import Path
from cocotb.triggers import Timer

import cocotb
from cocotb.clock import Clock
from cocotb.triggers import RisingEdge, FallingEdge

@cocotb.test()
async def test_multiplier(dut):
    dut.a.value=2
    dut.b.value=3
    assert dut.c.value==6,"Result is incorrect "
    

    
    













        

        

