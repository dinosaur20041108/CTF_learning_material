from pwn import *
elf =ELF ("JIT-ROP")
p=gdb.debug ("./JIT-ROP")
p=process("JIT-ROP")
p.sendafter("RCTF","name")
p.interactive()