import os
import assembly as ASM
import pin
import re


class Code(object):
    def __init__(self, number, source) -> None:
        self.numer = number
        self.source = source.upper()
        self.op = None
        self.src = None
        self.dst = None
        self.prepare_source()

    def get_op(self):
        if self.op in OP2:
            return OP2[self.op]
        if self.op in OP1:
            return OP1[self.op]
        if self.op in OP0:
            return OP0[self.op]
        raise SyntaxError(self)

    def get_am(self, addr):
        if not addr:
            return 0, 0
        if addr in REGISTERS:
            return pin.AM_REG, REGISTERS[addr]
        if re.match(r'^[0-9]+$', addr):
            return pin.AM_INS, int(addr)
        if re.match(r'^0X[0-9A-F]+$', addr):
            return pin.AM_INS, int(addr, 16)
        raise SyntaxError(self)

    def prepare_source(self):
        tup = self.source.split(',')
        if len(tup) > 2:
            raise SyntaxError(self)
        if len(tup) == 2:
            self.src = tup[1].strip()

        tup = re.split(r" +", tup[0])
        if len(tup) > 2:
            raise SyntaxError(self)
        if len(tup) == 2:
            self.dst = tup[1].strip()
        self.op = tup[0].strip()

    def compile_code(self):
        op = self.get_op()

        amd, dst = self.get_am(self.dst)
        ams, src = self.get_am(self.src)

        if op in OP2SET:
            ir = op | (amd << 2) | ams
        elif op in OP1SET:
            ir = op | amd
        else:
            ir = op

        return [ir, dst, src]

    def __repr__(self):
        return f'[{self.numer}]-{self.source}'


class SyntaxError(Exception):
    def __init__(self, code: Code, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.code = code


dirname = os.path.dirname(__file__)

inputfile = os.path.join(dirname, "program.asm")
outputfile = os.path.join(dirname, "program.txt")

annotation = re.compile(r"(.*?);.*")
codes = []
OP2 = {
    'MOV': ASM.MOV
}
OP1 = {
}

OP0 = {
    "NOP": ASM.NOP,
    "HLT": ASM.HLT,
}

OP2SET = set(OP2.values())
OP1SET = set(OP1.values())
OP2SET = set(OP1.values())

REGISTERS = {
    'A': pin.A,
    'B': pin.B,
    'C': pin.C,
    'D': pin.D,

}


def compile_program():
    with open(inputfile, encoding="utf8") as file:
        lines = file.readlines()
    for index, line in enumerate(lines):
        source = line.strip()
        if not source:
            continue
        if ";" in source:
            match = annotation.match(source)
            source = match.group(1)

        code = Code(index+1, source)
        codes.append(code)
    with open(outputfile, "w") as file:
        file.writelines("v2.0 raw\n")
        for code in codes:
            values=code.compile_code()
            for v in values:
                file.write(str(hex(v).replace("0x", ""))+" ")



def main():
    try:
        compile_program()
    except SyntaxError as e:
        print(f'Syntax error at {e.code}')
        return
    print("OK!")


if __name__ == "__main__":
    main()
