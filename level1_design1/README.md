# Multiplexer Design Verification

The verification environment is setup using [Vyoma's UpTickPro](https://vyomasystems.com) provided for the hackathon.

![](https://github.com/vyomasystems-lab/challenges-Vinuthna3031/blob/master/vyoma.png?raw=true)

## Verification Environment

The [CoCoTb](https://www.cocotb.org/) based Python test is developed as explained. The test drives inputs to the Design Under Test (mux module here) which takes in 31 2-bit inputs *inp0-inp30*, 5-bit select line *sel* and gives 2-bit output *out*.

The values are assigned to the input port using 
```
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
```

The assert statement is used for comparing the multiplexer's outut to the expected value.

The following error is seen:
```
 assert dut.out.value == dut.inp30.value, "Multiplexer output is incorrect: {op} != {out}, expected value={EXP}".format(
                     AssertionError: Multiplexer output is incorrect: 1 != 0, expected value=1
```
## Test Scenario 
### Test case 1 (basictest1_mux)
- Test Inputs: inp0-inp30 values are same as above except for the select value i.e.,*sel=0*
- Expected Output: out=1
- Observed Output in the DUT dut.out.value=1
Therefore, the test is passed.

### Test case 2 (basictest2_mux)
- Test Inputs: inp0-inp30 values are same as above except for the select value i.e.,*sel=30*
- Expected Output: out=1
- Observed Output in the DUT dut.out.value=0

Output mismatches for the above inputs proving that there is a design bug

### Test case 3 (test_mux)
- Test Inputs: inp0-inp30 values are same as above except for the select value i.e.,*sel=12*
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
