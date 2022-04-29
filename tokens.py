
def get_tokens(instr:str):
    opcode = ""
    i = 0
    while instr[i]!=" ":
        opcode+=instr[i]
        i+=1
    others = instr[i+1:].split(",")
    others = [i.strip() for i in others]
    return opcode,others
