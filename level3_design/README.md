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
Based on the test case and analysing the design, we see the following

```
module ha(a,b,s,c);
    input a,b;
    output s,c;
     
    assign s = a^b;
    assign c = a+b;       <==Bug
endmodule
```
In half adder, carry should be a&b.

## Verification Strategy
Randomly gave numbers for inputs and checked.

## Is the verification complete ?
Yes. And the bug is sucessfully exposed.
