from registers import registers
from tokens import get_tokens

instructions = {
    'add': {'type':'R','op':51,'funct3':b'000','funct7':b'0000000'},
    'sub': {'type':'R','op':51,'funct3':b'000','funct7':b'0100000'},
    'or':  {'type':'R','op':51,'funct3':b'110','funct7':b'0000000'},
    'xor': {'type':'R','op':51,'funct3':b'100','funct7':b'0000000'},
    'and': {'type':'R','op':51,'funct3':b'111','funct7':b'0000000'},
    'slt': {'type':'R','op':51,'funct3':b'010','funct7':b'0000000'},
    'sltu':{'type':'R','op':51,'funct3':b'011','funct7':b'0000000'},
}

def r_type(op,operands):
    #others[0]-> rd others[1]->rs1 others[2]->rs2
    instr = 0
    rd = registers[operands[0]]
    rs1 = registers[operands[1]]
    rs2 = registers[operands[2]]
    opcode = instructions[op]['op']
    funct3 = int(instructions[op]['funct3'],2)
    funct7 = int(instructions[op]['funct7'],2)
    instr = instr | opcode 
    instr = instr | (rd<<7) 
    instr = instr | (funct3<<12)
    instr = instr | (rs1<<15)
    instr = instr | (rs2<<20)
    instr = instr | (funct7<<25)
    return f"{instr:#010x}"
    
instr = input(">")

op, operands = get_tokens(instr)
i_type = instructions[op]['type']

if i_type=="R":
    print(r_type(op,operands))