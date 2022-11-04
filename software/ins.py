import os

dirname = os.path.dirname(__file__)
filename = os.path.join(dirname, "ins.txt")

WE_A = 2**0
CS_A = 2**1

WE_B = 2**2
CS_B = 2**3

WE_C = 2**4
CS_C = 2**5


ALU_ADD = 0
ALU_SUB = 2**6
ALU_OUT = 2**7


WE_M = 2**8
CS_M = 2**9

WE_PC = 2**10
EN_PC = 2**11
CS_PC = 2**12

HLT = 2**15

micro_program = [
    CS_M | CS_A | WE_A | WE_PC | EN_PC | CS_PC,
    CS_M | CS_B | WE_B | WE_PC | EN_PC | CS_PC,
    ALU_OUT | CS_C | WE_C,
    CS_C | WE_M | CS_M | WE_PC | EN_PC | CS_PC,
    HLT,
]

with open(filename, "w") as file:
    file.writelines("v2.0 raw\n")
    for v in micro_program:
        file.write(str(hex(v).replace("0x", ""))+" ")
