from riscv import instructions
from _parser import get_tokens, i_type, r_type, b_type
import sys

if len(sys.argv)<3: #one arg is main.py
    print("Usage: python main.py <input file> <output file>")
else:
    filename = sys.argv[1]
    outname = sys.argv[2]
    with open(filename,'r') as file:
        out = open(outname,'w')
        for line in file.readlines():
            op, operands = get_tokens(line)
            instr_type = instructions[op]['type']
            if instr_type=="R":
                instr = r_type(op,operands)
            elif instr_type=="I":
                instr =  i_type(op,operands)
            elif instr_type=="B":
                instr = b_type(op,operands)
            out.write(instr+"\n")