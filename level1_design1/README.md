# Multiplexer Design Verification

The verification environment is setup using [Vyoma's UpTickPro](https://vyomasystems.com) provided for the hackathon.

![](https://github.com/vyomasystems-lab/challenges-Vinuthna3031/blob/master/vyoma.png?raw=true)
![](https://drive.google.com/file/d/1iO0vpRrfoze44BEh9zbQ88ruruLMR55d/view?usp=sharing)

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
dut.sel.value=0
```

The assert statement is used for comparing the adder's outut to the expected value.

The following error is seen:
```
assert dut.sum.value == A+B, "Adder result is incorrect: {A} + {B} != {SUM}, expected value={EXP}".format(
                     AssertionError: Adder result is incorrect: 7 + 5 != 2, expected value=12
```
## Test Scenario **(Important)**
- Test Inputs: a=7 b=5
- Expected Output: sum=12
- Observed Output in the DUT dut.sum=2

Output mismatches for the above inputs proving that there is a design bug

## Design Bug
Based on the above test input and analysing the design, we see the following

```
 always @(a or b) 
  begin
    sum = a - b;             ====> BUG
  end
```
For the adder design, the logic should be ``a + b`` instead of ``a - b`` as in the design code.

## Design Fix
Updating the design and re-running the test makes the test pass.

![](https://i.imgur.com/5XbL1ZH.png)

The updated design is checked in as adder_fix.v

## Verification Strategy

## Is the verification complete ?
