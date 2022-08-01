# Sequence detector Design Verification

The verification environment is setup using [Vyoma's UpTickPro](https://vyomasystems.com) provided for the hackathon.

![](https://github.com/vyomasystems-lab/challenges-Vinuthna3031/blob/master/vyoma.png)

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
The assert statement is used for comparing the sequence detector's output to the expected value.

The following error is seen:
```
assert x=="00010010" , "Result is incorrect: {op} != {out}, expected value={EXP}".format(
                     AssertionError: Result is incorrect: 00010010 != 00010000, expected value=00010010
```
## Test Scenario 

- Test Inputs: Each bit of "10110111" is given at the active edge of clock.
- Expected Output: "0001010" 
- Observed Output in the DUT: "00010000"

Output mismatches for the above inputs proving that there is a design bug.

![](https://github.com/vyomasystems-lab/challenges-Vinuthna3031/blob/master/level1_design2/seq_detector_failedcase.png)

## Design Bug
Based on the testcase and analysing the design, we see the following

```
SEQ_1:
begin
  if(inp_bit == 1)
    next_state = IDLE;  <==BUG
  else
    next_state = SEQ_10;
end
SEQ_10:
begin
  if(inp_bit == 1)
    next_state = SEQ_101;
  else
    next_state = IDLE;
end
SEQ_101:
begin
  if(inp_bit == 1)
    next_state = SEQ_1011;
  else
    next_state = IDLE;  <==BUG
end
SEQ_1011:
begin
  next_state = IDLE;  <==BUG
end
```
As the sequence detector should include overlapping-
When it is in the state SEQ_1, if it receives inp_bit as 1 it should be in the same state itself.
When it is in the state SEQ_101, if it receives inp_bit as 0 it should jump to SEQ_10.
When it is in the state SEQ_1011, it is supposed to see for inp_bit=0 so which replicates the state SEQ_1.  

## Verification Strategy
Tried giving a sequence which involves overlapping and stored seq_seen values at every active clock edge in a string and finally verified with the expected output sequence.

## Is the verification complete ?
Yes. And the bugs are sucessfully exposed.
