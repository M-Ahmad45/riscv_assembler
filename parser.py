from riscv import registers, instructions
def get_tokens(instr:str):
    opcode = ""
    i = 0
    while instr[i]!=" ":
        opcode+=instr[i]
        i+=1
    others = instr[i+1:].split(",")
    others = [i.strip() for i in others]
    return opcode,others

def r_type(op,operands):
    #others[0]-> rd others[1]->rs1 others[2]->rs2
    instr = 0
    rd = registers[operands[0]]
    rs1 = registers[operands[1]]
    rs2 = registers[operands[2]]
    opcode = int(instructions[op]['op'])
    funct3 = int(instructions[op]['funct3'],2)
    funct7 = int(instructions[op]['funct7'],2)
    instr = instr | opcode 
    instr = instr | (rd<<7) 
    instr = instr | (funct3<<12)
    instr = instr | (rs1<<15)
    instr = instr | (rs2<<20)
    instr = instr | (funct7<<25)
    return f"{instr:#010x}"
    