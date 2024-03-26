from pwn import *
p = remote('127.0.0.1', 9999)

def register(name):
    p.sendlineafter(b'3. exit', '1')
    p.sendlineafter(b'What\'s your name?', name)
    p.recvuntil(b'Here is your token(in hex): ')
    s = p.recvline().strip().decode()
    iv = bytes.fromhex(s[:32])
    token = bytes.fromhex(s[32:])
    return iv, token

def login(iv, token):
    iv = hex(int.from_bytes(iv, 'big'))[2:]
    token = hex(int.from_bytes(token, 'big'))[2:]
    p.sendlineafter(b'3. exit', '2')
    p.sendlineafter(b'Your token(in hex): ', iv+token)
    s = p.recvline().strip().decode()
    iv = bytes.fromhex(s[:32])
    name = bytes.fromhex(s[32:])
    return iv, name

# step 1
iv, token = register('bdmin')

# step 2
token = bytes([(token[0] ^ ord('b') ^ ord('a'))]) + token[1:]
iv, name = login(iv, token)

# step 3
new_iv = []
for i in range(16):
    new_iv.append(iv[i] ^ name[i] ^ b'yusa'[i%4])
iv = bytes(new_iv)
login(iv, token)

p.interactive()