# Bitmanipulation Coprocessor Design Verification

The verification environment is setup using [Vyoma's UpTickPro](https://vyomasystems.com) provided for the hackathon.

![](https://github.com/vyomasystems-lab/challenges-Vinuthna3031/blob/master/vyoma.png)

## Verification Environment

The [CoCoTb](https://www.cocotb.org/) based Python test is developed as explained. The test drives inputs to the Design Under Test (mkbitmanip module here) which takes in the inputs *CLK*, *RST_N* and *mav_putvalue_instr*, *mav_putvalue_src1*, *mav_putvalue_src2*, *mav_putvalue_src3* each of 32 bits and gives 33-bit output *mav_putvalue*.

The values are assigned to the input port using 
```
mav_putvalue_src1 = 0x1
mav_putvalue_src2 = 0x2
mav_putvalue_src3 = 0x3
mav_putvalue_instr = 0x101010B3
```
The assert statement is used for comparing the bit manipulation coprocessor's outut to the expected value.

The following error is seen:
```
assert dut_output == expected_mav_putvalue, error_message
                     AssertionError: Value mismatch DUT = 0x2 does not match MODEL = 0x0
```
## Test Scenario 

- Test Inputs: 
    mav_putvalue_src1 = 0x1
    mav_putvalue_src2 = 0x2
    mav_putvalue_src3 = 0x3
    mav_putvalue_instr = 0x101010B3
- Expected Output: mav_putvalue=0x0
- Observed Output in the DUT dut.mav_putvalue.value=0x2

Output mismatches for the above inputs proving that there is a design bug


![](https://github.com/vyomasystems-lab/challenges-Vinuthna3031/blob/master/level2_design/bitmanipulation_failedcase.png)

## Verification Strategy
Randomly gave values for inputs and checked.

## Is the verification complete ?
Yes.
