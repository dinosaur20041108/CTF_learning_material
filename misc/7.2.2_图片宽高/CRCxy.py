import struct
import binascii
with open('01-图片宽高.png','rb')as f:
    m=f.read()
sign=0
for i in range(5000):
    for j in range(5000):
        c=m[12:16]+struct.pack('>i',i)+struct.pack('>i',j)+m[24:29]
        crc=binascii.crc32(c)&0xffffffff
        if crc==0xBE6698DC:
            print(hex(i),hex(j))
            sign=1
    if sign==1:
        break
