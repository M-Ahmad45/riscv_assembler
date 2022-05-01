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
    opcode = int(instructions[op]['op'],2)
    funct3 = int(instructions[op]['funct3'],2)
    funct7 = int(instructions[op]['funct7'],2)

    instr = instr | opcode 
    instr = instr | (rd<<7) 
    instr = instr | (funct3<<12)
    instr = instr | (rs1<<15)
    instr = instr | (rs2<<20)
    instr = instr | (funct7<<25)
    print(bin(instr))
    return f"{instr:#010x}"

def i_type(op,operands):
    if op=='lw':
        return lw(op,operands)
    instr = 0
    rd = registers[operands[0]]
    rs1 = registers[operands[1]]
    imm:str = operands[2]
    if imm.isalnum():
        imm=int(imm,16)
    else:
        imm=int(imm)
    opcode = int(instructions[op]['op'],2)
    funct3 = int(instructions[op]['funct3'],2)

    instr = opcode | (rd<<7) | (funct3<<12) | (rs1<<15) | (imm<<20)
    return f"{instr:#010x}"

def get_offset_imm(operand:str):
    imm = ''
    i = 0
    while operand[i]!=' ' and operand[i]!='(':
        imm+=operand[i]
        i+=1
    if imm.isalnum():
        imm=int(imm,16)
    else:
        imm=int(imm)
    rs1 = ''
    i+=1
    while operand[i]!=')' and operand[i]!=' ':
        rs1+=operand[i]
        i+=1
    return imm,rs1

def lw(op,operands):
    instr = 0
    opcode = int(instructions[op]['op'],2)
    funct3 = int(instructions[op]['funct3'],2)
    rd = registers[operands[0]]
    imm,rs1 = get_offset_imm(operands[1])
    rs1 = registers[rs1]

    instr = opcode | (rd<<7) | (funct3<<12) | (rs1<<15) | (imm<<20)
    return  f"{instr:#010x}"
    







