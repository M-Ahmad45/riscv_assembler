lw x1, 10(x0)
lw x2, 1(x0)
add x3, x1, x2
addi x4, x3, -5
beq x4, x2, -8
slt x5,x2,x3
add x4, x2, x3