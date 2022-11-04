import os
dirname = os.path.dirname(__file__)
filename = os.path.join(dirname, "532DEC.txt")

with open(filename, "w") as file:
    file.writelines("v2.0 raw\n")
    for var in range(32):
        value = 1 << var
        file.write(str(hex(value).replace("0x", ""))+" ")
