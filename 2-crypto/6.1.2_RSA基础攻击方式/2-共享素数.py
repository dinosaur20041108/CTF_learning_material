e=65537 
n1=97651955426214592033572365773920057508427271716707728935577093505679682172372037636450110482557482581706749399826008020235313113944314376784907620141813540662534339234459496768240479220230957160400392913463409022293150429520768318670419503933186212191126307407839258074528684084840185308927331947537145829447
n2=66614608752278705185634904394365361979042404918604096433974094458632279000060400427645038515243709686328401390645112697979593615158483692603354348148482259753616268091570444012203646513399123035447707361637792128736541860728977309005359893376233152775475579396612879271884234088653699303606533505374905232923
c1=63953261435394891069612549636244603374173902686957436699829372333004288757335171873681401446375646490812908682109590243996379898870002800896829966763855784343173371142195534847739577115446177220108666069599165923313053697108515804761639807236996792227009426406166247412285289649024825203381481266356972774150
c2=57194972314389051543512820205703581413440756041185322107796772858205215016985575901911128530044596380489776006585803175505500161134431388478575594371310142237309980755948653414728132043884818377338689153219237884062208507665330097950793748413372319469773142224317762978585059400442666153359320918649028613087
#
from Crypto.Util.number import *
from gmpy2 import *
p=GCD(n1,n2)#求n1,n2最大公因数说明使用了相同的素数
print (p)
q=n1//p
#
d=invert(e,(p-1)*(q-1))
m=powmod(c1,d,n1)
print(long_to_bytes(m))