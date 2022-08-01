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
    dut.a.value=12
    dut.b.value=13
    await Timer(2,'ns')
    assert dut.c.value==dut.a.value*dut.b.value,"Result is incorrect: {op} != {out}, expected value={EXP}".format(
        op=int(dut.a.value * dut.b.value), out=int(dut.c.value), EXP=int(dut.a.value * dut.b.value))
