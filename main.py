from riscv import instructions
from parser import get_tokens, r_type

instr = input(">")

op, operands = get_tokens(instr)
instr_type = instructions[op]['type']

if instr_type=="R":
    print(r_type(op,operands))