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
async def test_seq_bug1(dut):
    """Test for seq detection """

    clock = Clock(dut.clk, 10, units="us")  # Create a 10us period clock on port clk
    cocotb.start_soon(clock.start())        # Start the clock

    # reset
    dut.reset.value = 1
    await FallingEdge(dut.clk)  
    dut.reset.value = 0
    await FallingEdge(dut.clk)

    cocotb.log.info('#### CTB: Develop your test here! ######')
    #input is 10110111
    x=""
    dut.inp_bit.value=1
    await Timer(10, units='us')
    x+=str(dut.seq_seen.value)
    print(int(dut.current_state.value))

    dut.inp_bit.value=0
    await Timer(10, units='us')
    x+=str(dut.seq_seen.value)
    print(int(dut.current_state.value))

    dut.inp_bit.value=1
    await Timer(10, units='us')
    x+=str(dut.seq_seen.value)
    print(int(dut.current_state.value))

    dut.inp_bit.value=1
    await Timer(10, units='us')
    x+=str(dut.seq_seen.value)
    print(int(dut.current_state.value))

    dut.inp_bit.value=0
    await Timer(10, units='us')
    x+=str(dut.seq_seen.value)
    print(int(dut.current_state.value))

    dut.inp_bit.value=1
    await Timer(10, units='us')
    x+=str(dut.seq_seen.value)
    print(int(dut.current_state.value))

    dut.inp_bit.value=1
    await Timer(10, units='us')
    x+=str(dut.seq_seen.value)
    print(int(dut.current_state.value))
    
    dut.inp_bit.value=1
    await Timer(10, units='us')
    x+=str(dut.seq_seen.value)
    print(int(dut.current_state.value))

    assert x=="00010010" , "Result is incorrect: {op} != {out}, expected value={EXP}".format(
            op="00010010",out=x, EXP="00010010")
    













        

        

