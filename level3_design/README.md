# Sequence detector Design Verification

The verification environment is setup using [Vyoma's UpTickPro](https://vyomasystems.com) provided for the hackathon.

![](https://github.com/vyomasystems-lab/challenges-Vinuthna3031/blob/master/vyoma.png?raw=true)

## Verification Environment

The [CoCoTb](https://www.cocotb.org/) based Python test is developed as explained. The test drives inputs to the Design Under Test (seq_detect_1011 module here) which takes in the inputs *clk*, *reset*, *inp_bit* each of 1 bit and gives 1-bit output *seq_seen*.

The values are assigned to the input port using 
```
clock = Clock(dut.clk, 10, units="us")  # Create a 10us period clock on port clk
cocotb.start_soon(clock.start())        # Start the clock

# reset
dut.reset.value = 1
await FallingEdge(dut.clk)  
dut.reset.value = 0
await FallingEdge(dut.clk)

dut.inp_bit.value=1

```
The assert statement is used for comparing the sequence detector's outut to the expected value.

The following error is seen:
```
assert x=="00010010" , "Result is incorrect: {op} != {out}, expected value={EXP}".format(
                     AssertionError: Result is incorrect: 00010010 != 00010000, expected value=00010010
```
## Test Scenario 

### Test case 2 (basictest2_mux)
- Test Inputs: inp0-inp30 values are same as above except for the select value i.e.,*sel=30*
- Expected Output: out=1
- Observed Output in the DUT dut.out.value=0

Output mismatches for the above inputs proving that there is a design bug


![](https://github.com/vyomasystems-lab/challenges-Vinuthna3031/blob/master/level1_design1/mux_failed%20test%20case.png)

## Design Bug
Based on the input of test case 2 and analysing the design, we see the following

```
  5'b11100: out = inp28;
  5'b11101: out = inp29;
  default: out = 0; 
```
For the multiplexer design, if the select line value is 30 output is supposed to be the value of inp30. But there is no logic written for sel=30(5'b11110).

For test case 3, we observed
```
  5'b01010: out = inp10;
  5'b01011: out = inp11;
  5'b01101: out = inp12;        <===Bug
  5'b01101: out = inp13; 
``` 
For *sel=12* no logic is written.

## Design Fix
Updating the design and re-running the test makes the test pass.

![](https://github.com/vyomasystems-lab/challenges-Vinuthna3031/blob/master/level1_design1/mux_fixed%20bugs.png)

The updated design is checked in as mux_fix.v

## Verification Strategy
First attempt was trying with the lowest and highest possible values for *sel* and then continue to check for other values(for which a *for* loop is used ).

## Is the verification complete ?
Yes. And the bugs are sucessfully exposed.
