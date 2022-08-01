# challenges-MaharshiLegacy
challenges-MaharshiLegacy created by GitHub Classroom
# Level-1 Design-1 MUX Design Verification

The verification environment is setup using [Vyoma's UpTickPro](https://vyomasystems.com) provided for the hackathon.

Make sure to include the Gitpod id in the screenshot

![image](https://user-images.githubusercontent.com/109369461/182188547-d876c620-256d-474b-abfa-10c45914a707.png)


## Verification Environment

The [CoCoTb](https://www.cocotb.org/) based Python test is developed as explained. The test drives inputs to the Design Under Test (adder module here) which takes in 4-bit inputs a and b and gives 5-bit output sum

The values are assigned to the input port using 

  A = 1
  Sel = 0

    # input driving
    dut.inp0.value = A
    dut.sel.value = Sel




The following error is seen:

assert dut.out.value == A, "Mux result is incorrect for selected {S}(selectionline) and {A}(input0). because given (input0){OUT}!=(recieved o/p){out}".format( A=int(dut.inp0.value), S=int(dut.sel.value),OUT=int(dut.out.value), out=int(dut.inp0.value))
                     AssertionError: Mux result is incorrect for selected 0(selectionline) and 1(input0). because given (input0)0!=(recieved o/p)1

## Test Scenario *(Important)*
- Test Inputs: a=1 sel=0
- Expected Output: sum=1
- Observed Output in the DUT dut.sum=0

Output mismatches for the above inputs proving that there is a design bug

## Design Bug
Based on the above test input and analysing the design, we see the following


begin
    case(sel)
      5'b00000: out = 2'b00;  //bug
      ....
      ....
    endcase
 end

![image](https://user-images.githubusercontent.com/109369461/182188803-bddf37a1-4750-4d04-a459-4358c119517d.png)


## Design Fix
Updating the design and re-running the test makes the test pass.

![image](https://user-images.githubusercontent.com/109369461/182191912-67d2261d-914e-4b6b-803f-7228821237b4.png)



## Verification Strategy
i have done direct testbench

## Is the verification complete ?
YES

# Level-1 Design-2 FSM SEQUENCE DETECTOR Design Verification

The verification environment is setup using [Vyoma's UpTickPro](https://vyomasystems.com) provided for the hackathon.

Make sure to include the Gitpod id in the screenshot

![image](https://user-images.githubusercontent.com/109369461/182188547-d876c620-256d-474b-abfa-10c45914a707.png)

## Verification Environment

The [CoCoTb](https://www.cocotb.org/) based Python test is developed as explained. The test drives inputs to the Design Under Test (adder module here) which takes in 4-bit inputs a and b and gives 5-bit output sum

The values are assigned to the input port using 

   
    dut.reset.value = 1
    await FallingEdge(dut.clk)
    dut.reset.value = 0
    await FallingEdge(dut.clk) 
    dut.inp_bit.value=1
    await FallingEdge(dut.clk) 
    dut.inp_bit.value=0
    await FallingEdge(dut.clk) 
    dut.inp_bit.value=1
    await FallingEdge(dut.clk) 
    dut.inp_bit.value=1
    await FallingEdge(dut.clk) 
    
    assert dut.seq_seen.value == 1, "FSM sequence for {Current_state}(current state)== {SEQ1011}(detect_seq_state) but  {Seq_seen}(seq_seen) != 1".format( Current_state=int(dut.current_state.value),SEQ1011=dut.SEQ_1011.value,Seq_seen=dut.seq_seen.value)


The assert statement is used for comparing the adder's outut to the expected value.

The following error is seen:

assert dut.seq_seen.value == 1, "FSM sequence for {Current_state}(current state)== {SEQ1011}(detect_seq_state) but  {Seq_seen}(seq_seen) != 1".format( Current_state=int(dut.current_state.value),SEQ1011=dut.SEQ_1011.value,Seq_seen=dut.seq_seen.value)
                     AssertionError: FSM sequence for 4(current state)== 4(detect_seq_state) but  0(seq_seen) != 1

## Test Scenario *(Important)*
- Test Inputs: a=1011
- Expected Output: sum=1
- Observed Output in the DUT dut.out=0

Output mismatches for the above inputs proving that there is a design bug

## Design Bug
Based on the above test input and analysing the design, we see the following


  assign seq_seen = current_state == SEQ_1011 ? 0 : 0;


![image](https://user-images.githubusercontent.com/109369461/182193362-1db0fe2e-e67d-4261-b97d-e143eda53f1f.png)


## Design Fix
Updating the design and re-running the test makes the test pass.

![Uploading image.png…]()


## Verification Strategy
direct verification strategy by given direct stimuli
## Is the verification complete ?
yes
