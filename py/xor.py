
import pwn
a=b"abcdefg"
b=b"1234567"
flag="flag{123456789123456789}"
key="maybemiamaybemiamaybemia"
print(pwn.xor{a,b})