add x1, x0, x0
add x2, x0, x0
addi x3, x0, 11
slt x4, x3, x1
bne x4,x0, 16
add x2, x2, x1
addi x1,x1, 1
beq x0, x0, -16
add x31,x2,x0
beq x31, x31, 0