import os
import assembly
import pin

dirname = os.path.dirname(__file__)
filename = os.path.join(dirname, "micro.txt")

micro = [
    pin.HLT for _ in range(0x10000)
]


def compile_addr2(addr, ir, psw, index):
    global micro
    op = ir & 0xf0
    amd = (ir >> 2) & 3
    ams = ir & 3

    INST = assembly.INSTRUCTIONS[2]
    if op not in INST:
        micro[addr] = pin.CYC
        return
    am = (amd, ams)
    if am not in INST[op]:
        micro[addr] = pin.CYC
        return
    EXEC = INST[op][am]
    if index < len(EXEC):
        micro[addr] = EXEC[index]
    else:
        micro[addr] = pin.CYC


def compile_addr1(addr, ir, psw, index):
    pass


def compile_addr0(addr, ir, psw, index):
    global micro
    op = ir

    INST = assembly.INSTRUCTIONS[2]
    if op not in INST:
        micro[addr] = pin.CYC
        return

    EXEC = INST[op]
    if index < len(EXEC):
        micro[addr] = EXEC[index]
    else:
        micro[addr] = pin.CYC


for addr in range(0x10000):
    ir = addr >> 8
    psw = (addr >> 4) & 0xf
    cyc = addr & 0xf

    if cyc < len(assembly.FETCH):
        micro[addr] = assembly.FETCH[cyc]
        continue
    addr2 = ir & (1 << 7)
    addr1 = ir & (1 << 6)

    index = cyc-len(assembly.FETCH)
    if addr2:
        compile_addr2(addr, ir, psw, index)
    elif addr1:
        compile_addr1(addr, ir, psw, index)

    else:
        compile_addr0(addr, ir, psw, index)


with open(filename, "w") as file:
    file.writelines("v2.0 raw\n")
    for v in micro:
        file.write(str(hex(v).replace("0x", ""))+" ")
