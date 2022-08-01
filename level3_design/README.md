# 16-bit Array Multiplier Design Verification

The verification environment is setup using [Vyoma's UpTickPro](https://vyomasystems.com) provided for the hackathon.

![](https://github.com/vyomasystems-lab/challenges-Vinuthna3031/blob/master/vyoma.png?raw=true)

## Verification Environment

The [CoCoTb](https://www.cocotb.org/) based Python test is developed as explained. The test drives inputs to the Design Under Test (buggy_multiplier_16bit module here) which takes in the inputs *a*, *b* each of 16 bits and gives 32-bit output *c*.

The values are assigned to the input port using 
```
dut.a.value=12
dut.b.value=13
```
The assert statement is used for comparing the multiplier's outut to the expected value.

The following error is seen:
```
assert dut.c.value==dut.a.value*dut.b.value,"Result is incorrect: {op} != {out}, expected value={EXP}".format(
                     AssertionError: Result is incorrect: 156 != 12, expected value=156
```
## Test Scenario 

- Test Inputs: a=12, b=13
- Expected Output: out=156
- Observed Output in the DUT dut.out.value=12

Output mismatches for the above inputs proving that there is a design bug


![](https://github.com/vyomasystems-lab/challenges-Vinuthna3031/blob/master/level3_design/failedcase.png)

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
