MSR = 1
MAR = 2
MBR = 2
RAM = 4
IR = 5
DST = 6
SRC = 7
A = 8
B = 9
C = 10
D = 11
DI = 12
SI = 13
SP = 14
BP = 15
CS = 16
DS = 17
SS = 18
ES = 19
VEC = 20
T1 = 21
T2 = 22

_DST_SHIFT = 5

MSR_OUT = MSR
MAR_OUT = MAR
MBR_OUT = MBR
RAM_OUT = RAM
IR_OUT = IR
DST_OUT = DST
SRC_OUT = SRC
A_OUT = A
B_OUT = B
C_OUT = C
D_OUT = D
DI_OUT = DI
SI_OUT = SI
SP_OUT = SP
BP_OUT = BP
CS_OUT = CS
DS_OUT = DS
SS_OUT = SS
ES_OUT = ES
VEC_OUT = VEC
T1_OUT = T1
T2_OUT = T2

MSR_IN = MSR << _DST_SHIFT
MAR_IN = MAR << _DST_SHIFT
MBR_IN = MBR << _DST_SHIFT
RAM_IN = RAM << _DST_SHIFT
IR_IN = IR << _DST_SHIFT
DST_IN = DST << _DST_SHIFT
SRC_IN = SRC << _DST_SHIFT
A_IN = A << _DST_SHIFT
B_IN = B << _DST_SHIFT
C_IN = C << _DST_SHIFT
D_IN = D << _DST_SHIFT
DI_IN = DI << _DST_SHIFT
SI_IN = SI << _DST_SHIFT
SP_IN = SP << _DST_SHIFT
BP_IN = BP << _DST_SHIFT
CS_IN = CS << _DST_SHIFT
DS_IN = DS << _DST_SHIFT
SS_IN = SS << _DST_SHIFT
ES_IN = ES << _DST_SHIFT
VEC_IN = VEC << _DST_SHIFT
T1_IN = T1 << _DST_SHIFT
T2_IN = T2 << _DST_SHIFT

SRC_R = 2**10
SRC_W = 2**11
DST_R = 2**12
DST_W = 2**13

PC_WE = 2**14
PC_CS = 2**15
PC_EN = 2**16

PC_OUT = PC_CS

PC_IN = PC_CS | PC_WE
PC_INC = PC_CS | PC_WE | PC_EN

HLT = 2**31

ADDR2 = 1 << 7
ADDR1 = 1 << 6
ADDR2_SHIFT = 4
ADDR1_SHIFT = 2

AM_INS = 0
AM_REG = 1
AM_DIR = 2
AM_RAM = 3

CYC = 2**30
