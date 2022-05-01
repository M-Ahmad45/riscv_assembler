from riscv import instructions
from _parser import get_tokens, i_type, r_type

instr = input(">")

op, operands = get_tokens(instr)
instr_type = instructions[op]['type']

if instr_type=="R":
    print(r_type(op,operands))
elif instr_type=="I":
    print(i_type(op,operands))