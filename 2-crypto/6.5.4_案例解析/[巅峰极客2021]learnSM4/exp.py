from sm4 import _linear_map, loop_left_shift, S_BOX, _byte_pack, _byte_unpack
from pwn import *
import itertools
import string
from hashlib import sha256

def _linear_map_inv(byte4):
    _left = loop_left_shift
    return byte4 ^ _left(byte4, 2) ^ _left(byte4, 4) ^ _left(byte4, 8) ^ _left(byte4, 12) \
        ^ _left(byte4, 14) ^ _left(byte4, 16) ^ _left(byte4, 18) ^ _left(byte4, 22) \
        ^ _left(byte4, 24) ^ _left(byte4, 30)

S_INV_BOX = {y:x for x, y in S_BOX.items()}

def _s_inv_box(byte):
    return S_INV_BOX.get(byte)

def _non_linear_map_inv(byte_array):
    return (_s_inv_box(byte_array[0]), _s_inv_box(byte_array[1]),
            _s_inv_box(byte_array[2]), _s_inv_box(byte_array[3]))

def _rep_t_inv(byte4):
    b_array = _byte_unpack(_linear_map_inv(byte4))
    return _byte_pack(_non_linear_map_inv(b_array))

c1_list = []
conn = remote('127.0.0.1', 10001)
s = conn.recvline().strip()
s_last = s[12:28]
ans = s[-64:]
for i in itertools.product(string.ascii_letters+string.digits, repeat=4):
    s_first = ''.join(i)
    s = s_first + s_last
    if (sha256(s).hexdigest() == ans):
        conn.sendline(s_first)
        break


for i in range(4):
    conn.sendlineafter('r:', '0')
    conn.sendlineafter('i:', str(i))
    conn.sendlineafter('msg(hex):\n', '01')
    conn.recvline()
    c1 = conn.recvline()
    c1_list.append(int(c1))

for i in range(4):
    conn.sendlineafter('r:', '0')
    conn.sendlineafter('i:', str(i))
    conn.sendlineafter('msg(hex):\n', '01')
    conn.recvline()
    c1 = conn.recvline()

c1 = 0
for i in c1_list:
    c1 = c1 * 256 + i

x0, x1, x2, x3 = 0, 0, 0, 1
rk = _rep_t_inv(c1 ^ x0) ^ x1 ^ x2 ^ x3

conn.sendlineafter('Give me answer:', str(rk))
conn.interactive()