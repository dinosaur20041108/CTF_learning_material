n=107820827895585003318160075938897995007771726056433792260306646508197614885172767297860713228269372581388675047053081480259665212535577590049118106812907146179205072239202195537073770739125675017748544703407492971258729480561817875290145208304790655494183395710284259904924825216130329385053835448236320458029
e=89522445598733261357901825227079909455833500144157754746488199484282356592752881911539250096606592386991876444930791131091191645729189063282738620740478951554538143425376616935272546647795666042057430492362510853442637374299569781152667997525016908056524464220471765404748627571107144931587704935347192130747
c=78801382956240362099621219179273906545911347424992980739524362075033074146925440259224069602152252908929563712955805750439181009392136772144489054854771121558867343856732335266122392680114047445081029206150709456363766540038033883249133391765001168831795492173604819457970972375924518104751091565565160890627

from Crypto.Util.number import *
from gmpy2 import *
from RSAwienerHacker import *
import libnum

d=hack_RSA(e,n)#见文件夹内
flag=long_to_bytes(pow(c,d,n))
print(flag)