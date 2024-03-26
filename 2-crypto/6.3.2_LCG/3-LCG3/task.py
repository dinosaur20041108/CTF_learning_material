from Crypto.Util.number import *
flag = b'xxx'
plaintext = bytes_to_long(flag)
length = plaintext.bit_length()
a = getPrime(length)
b = getPrime(length)
m = getPrime(length)
seed = plaintext
for i in range(10):
    seed = (a*seed+b)%m
    if i > 7:
        print(seed)
ciphertext = seed
print("a = ",a)
print("b = ",b)
print("m = ",m)
# 1777214117121496355116809632947505045506788918442938748675
# 1006766436196275859665678602430108501972430566559062228711
# a =  2149591301214849380012343197213374567615949414713743294817
# b =  2066890008421519722437270046908245188484062751421642157301
# n =  1809675717674850305385699488680931200417546590161688440171
