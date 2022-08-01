# See LICENSE.vyoma for details

import cocotb
from cocotb.triggers import Timer

@cocotb.test()
async def basictest1_mux(dut):
    """Test for mux2"""

    cocotb.log.info('##### CTB: Develop your test here ########')
    
    dut.inp0.value=1
    dut.inp1.value=2
    dut.inp2.value=3
    dut.inp3.value=1
    dut.inp4.value=2
    dut.inp5.value=3
    dut.inp6.value=1
    dut.inp7.value=2
    dut.inp8.value=3
    dut.inp9.value=1
    dut.inp10.value=2
    dut.inp11.value=3
    dut.inp12.value=1
    dut.inp13.value=2
    dut.inp14.value=3
    dut.inp15.value=1
    dut.inp16.value=2
    dut.inp17.value=3
    dut.inp18.value=1
    dut.inp19.value=2
    dut.inp20.value=3
    dut.inp21.value=1
    dut.inp22.value=2
    dut.inp23.value=3
    dut.inp24.value=1
    dut.inp25.value=2
    dut.inp26.value=3
    dut.inp27.value=1
    dut.inp28.value=2
    dut.inp29.value=3
    dut.inp30.value=1
    dut.sel.value=0
    await Timer(2, units='ns')

    assert dut.out.value == dut.inp0.value, "Multiplexer output is incorrect: {op} != {out}, expected value={EXP}".format(
            op=int(dut.inp0.value),out=int(dut.out.value), EXP=int(dut.inp0.value))


@cocotb.test()
async def basictest2_mux(dut):
    """Test for mux2"""

    cocotb.log.info('##### CTB: Develop your test here ########')

    dut.inp0.value=1
    dut.inp1.value=2
    dut.inp2.value=3
    dut.inp3.value=1
    dut.inp4.value=2
    dut.inp5.value=3
    dut.inp6.value=1
    dut.inp7.value=2
    dut.inp8.value=3
    dut.inp9.value=1
    dut.inp10.value=2
    dut.inp11.value=3
    dut.inp12.value=1
    dut.inp13.value=2
    dut.inp14.value=3
    dut.inp15.value=1
    dut.inp16.value=2
    dut.inp17.value=3
    dut.inp18.value=1
    dut.inp19.value=2
    dut.inp20.value=3
    dut.inp21.value=1
    dut.inp22.value=2
    dut.inp23.value=3
    dut.inp24.value=1
    dut.inp25.value=2
    dut.inp26.value=3
    dut.inp27.value=1
    dut.inp28.value=2
    dut.inp29.value=3
    dut.inp30.value=1
    dut.sel.value=30
    await Timer(2, units='ns')

    assert dut.out.value == dut.inp30.value, "Multiplexer output is incorrect: {op} != {out}, expected value={EXP}".format(
            op=int(dut.inp30.value),out=int(dut.out.value), EXP=int(dut.inp30.value))



@cocotb.test()
async def test_mux(dut):
    """Test for mux2"""

    cocotb.log.info('##### CTB: Develop your test here ########')

    dut.inp0.value=1
    dut.inp1.value=2
    dut.inp2.value=3
    dut.inp3.value=1
    dut.inp4.value=2
    dut.inp5.value=3
    dut.inp6.value=1
    dut.inp7.value=2
    dut.inp8.value=3
    dut.inp9.value=1
    dut.inp10.value=2
    dut.inp11.value=3
    dut.inp12.value=1
    dut.inp13.value=2
    dut.inp14.value=3
    dut.inp15.value=1
    dut.inp16.value=2
    dut.inp17.value=3
    dut.inp18.value=1
    dut.inp19.value=2
    dut.inp20.value=3
    dut.inp21.value=1
    dut.inp22.value=2
    dut.inp23.value=3
    dut.inp24.value=1
    dut.inp25.value=2
    dut.inp26.value=3
    dut.inp27.value=1
    dut.inp28.value=2
    dut.inp29.value=3
    dut.inp30.value=1
    for i in range(31):
        dut.sel.value=i
        if i==0:
            await Timer(2, units='ns')

            assert dut.out.value == dut.inp0.value, "Multiplexer output is incorrect: {op} != {out}, expected value={EXP}".format(
                    op=int(dut.inp0.value),out=int(dut.out.value), EXP=int(dut.inp0.value))
        elif i==1:
            await Timer(2, units='ns')

            assert dut.out.value == dut.inp1.value, "Multiplexer output is incorrect: {op} != {out}, expected value={EXP}".format(
                    op=int(dut.inp1.value),out=int(dut.out.value), EXP=int(dut.inp1.value))
        
        elif i==2:
            await Timer(2, units='ns')

            assert dut.out.value == dut.inp2.value, "Multiplexer output is incorrect: {op} != {out}, expected value={EXP}".format(
                    op=int(dut.inp2.value),out=int(dut.out.value), EXP=int(dut.inp2.value))

        elif i==3:
            await Timer(2, units='ns')

            assert dut.out.value == dut.inp3.value, "Multiplexer output is incorrect: {op} != {out}, expected value={EXP}".format(
                    op=int(dut.inp3.value),out=int(dut.out.value), EXP=int(dut.inp3.value))

        elif i==4:
            await Timer(2, units='ns')

            assert dut.out.value == dut.inp4.value, "Multiplexer output is incorrect: {op} != {out}, expected value={EXP}".format(
                    op=int(dut.inp4.value),out=int(dut.out.value), EXP=int(dut.inp4.value))
        elif i==5:
            await Timer(2, units='ns')

            assert dut.out.value == dut.inp5.value, "Multiplexer output is incorrect: {op} != {out}, expected value={EXP}".format(
                    op=int(dut.inp5.value),out=int(dut.out.value), EXP=int(dut.inp5.value))
        elif i==6:
            await Timer(2, units='ns')

            assert dut.out.value == dut.inp6.value, "Multiplexer output is incorrect: {op} != {out}, expected value={EXP}".format(
                    op=int(dut.inp6.value),out=int(dut.out.value), EXP=int(dut.inp6.value))
        elif i==7:
            await Timer(2, units='ns')

            assert dut.out.value == dut.inp7.value, "Multiplexer output is incorrect: {op} != {out}, expected value={EXP}".format(
                    op=int(dut.inp7.value),out=int(dut.out.value), EXP=int(dut.inp7.value))
        elif i==8:
            await Timer(2, units='ns')

            assert dut.out.value == dut.inp8.value, "Multiplexer output is incorrect: {op} != {out}, expected value={EXP}".format(
                    op=int(dut.inp8.value),out=int(dut.out.value), EXP=int(dut.inp8.value))
        elif i==9:
            await Timer(2, units='ns')

            assert dut.out.value == dut.inp9.value, "Multiplexer output is incorrect: {op} != {out}, expected value={EXP}".format(
                    op=int(dut.inp9.value),out=int(dut.out.value), EXP=int(dut.inp9.value))
        elif i==10:
            await Timer(2, units='ns')

            assert dut.out.value == dut.inp10.value, "Multiplexer output is incorrect: {op} != {out}, expected value={EXP}".format(
                    op=int(dut.inp10.value),out=int(dut.out.value), EXP=int(dut.inp10.value))
        elif i==11:
            await Timer(2, units='ns')

            assert dut.out.value == dut.inp11.value, "Multiplexer output is incorrect: {op} != {out}, expected value={EXP}".format(
                    op=int(dut.inp11.value),out=int(dut.out.value), EXP=int(dut.inp11.value))
        elif i==12:
            await Timer(2, units='ns')

            assert dut.out.value == dut.inp12.value, "Multiplexer output is incorrect: {op} != {out}, expected value={EXP}".format(
                    op=int(dut.inp12.value),out=int(dut.out.value), EXP=int(dut.inp12.value))
            
        elif i==13:
            await Timer(2, units='ns')

            assert dut.out.value == dut.inp13.value, "Multiplexer output is incorrect: {op} != {out}, expected value={EXP}".format(
                    op=int(dut.inp13.value),out=int(dut.out.value), EXP=int(dut.inp13.value))
        elif i==14:
            await Timer(2, units='ns')

            assert dut.out.value == dut.inp14.value, "Multiplexer output is incorrect: {op} != {out}, expected value={EXP}".format(
                    op=int(dut.inp14.value),out=int(dut.out.value), EXP=int(dut.inp14.value))
        elif i==15:
            await Timer(2, units='ns')

            assert dut.out.value == dut.inp15.value, "Multiplexer output is incorrect: {op} != {out}, expected value={EXP}".format(
                    op=int(dut.inp15.value),out=int(dut.out.value), EXP=int(dut.inp15.value))
        elif i==16:
            await Timer(2, units='ns')

            assert dut.out.value == dut.inp16.value, "Multiplexer output is incorrect: {op} != {out}, expected value={EXP}".format(
                    op=int(dut.inp16.value),out=int(dut.out.value), EXP=int(dut.inp16.value))
        elif i==17:
            await Timer(2, units='ns')

            assert dut.out.value == dut.inp17.value, "Multiplexer output is incorrect: {op} != {out}, expected value={EXP}".format(
                    op=int(dut.inp17.value),out=int(dut.out.value), EXP=int(dut.inp17.value))
        elif i==18:
            await Timer(2, units='ns')

            assert dut.out.value == dut.inp18.value, "Multiplexer output is incorrect: {op} != {out}, expected value={EXP}".format(
                    op=int(dut.inp18.value),out=int(dut.out.value), EXP=int(dut.inp18.value))
        elif i==19:
            await Timer(2, units='ns')

            assert dut.out.value == dut.inp19.value, "Multiplexer output is incorrect: {op} != {out}, expected value={EXP}".format(
                    op=int(dut.inp19.value),out=int(dut.out.value), EXP=int(dut.inp19.value))
        elif i==20:
            await Timer(2, units='ns')

            assert dut.out.value == dut.inp20.value, "Multiplexer output is incorrect: {op} != {out}, expected value={EXP}".format(
                    op=int(dut.inp20.value),out=int(dut.out.value), EXP=int(dut.inp20.value))
        elif i==21:
            await Timer(2, units='ns')

            assert dut.out.value == dut.inp21.value, "Multiplexer output is incorrect: {op} != {out}, expected value={EXP}".format(
                    op=int(dut.inp21.value),out=int(dut.out.value), EXP=int(dut.inp21.value))
        elif i==22:
            await Timer(2, units='ns')

            assert dut.out.value == dut.inp22.value, "Multiplexer output is incorrect: {op} != {out}, expected value={EXP}".format(
                    op=int(dut.inp22.value),out=int(dut.out.value), EXP=int(dut.inp22.value))
        elif i==23:
            await Timer(2, units='ns')

            assert dut.out.value == dut.inp23.value, "Multiplexer output is incorrect: {op} != {out}, expected value={EXP}".format(
                    op=int(dut.inp23.value),out=int(dut.out.value), EXP=int(dut.inp23.value))                    
        elif i==24:
            await Timer(2, units='ns')

            assert dut.out.value == dut.inp24.value, "Multiplexer output is incorrect: {op} != {out}, expected value={EXP}".format(
                    op=int(dut.inp24.value),out=int(dut.out.value), EXP=int(dut.inp24.value)) 
        elif i==25:
            await Timer(2, units='ns')

            assert dut.out.value == dut.inp25.value, "Multiplexer output is incorrect: {op} != {out}, expected value={EXP}".format(
                    op=int(dut.inp25.value),out=int(dut.out.value), EXP=int(dut.inp25.value)) 
        elif i==26:
            await Timer(2, units='ns')

            assert dut.out.value == dut.inp26.value, "Multiplexer output is incorrect: {op} != {out}, expected value={EXP}".format(
                    op=int(dut.inp26.value),out=int(dut.out.value), EXP=int(dut.inp26.value)) 
        elif i==27:
            await Timer(2, units='ns')

            assert dut.out.value == dut.inp27.value, "Multiplexer output is incorrect: {op} != {out}, expected value={EXP}".format(
                    op=int(dut.inp27.value),out=int(dut.out.value), EXP=int(dut.inp27.value)) 
        elif i==28:
            await Timer(2, units='ns')

            assert dut.out.value == dut.inp28.value, "Multiplexer output is incorrect: {op} != {out}, expected value={EXP}".format(
                    op=int(dut.inp28.value),out=int(dut.out.value), EXP=int(dut.inp28.value)) 
        elif i==29:
            await Timer(2, units='ns')

            assert dut.out.value == dut.inp29.value, "Multiplexer output is incorrect: {op} != {out}, expected value={EXP}".format(
                    op=int(dut.inp29.value),out=int(dut.out.value), EXP=int(dut.inp29.value)) 
        elif i==30:
            await Timer(2, units='ns')

            assert dut.out.value == dut.inp30.value, "Multiplexer output is incorrect: {op} != {out}, expected value={EXP}".format(
                    op=int(dut.inp30.value),out=int(dut.out.value), EXP=int(dut.inp30.value)) 


