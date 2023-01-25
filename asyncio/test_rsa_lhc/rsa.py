# from Crypto.Util.number import *

#6*(a**2)+10*a*b-a*c*3+4*(b**2)-b*c*2= 94963804112945027587268840423509
#c*2-b*4-a*6 = 658989191820960796

e = 65537

p = c**10 + a*c - c + 37*b + 141
q = 575 + b*c - (a**17) + 14*c

n = p*q

with open('./secret.txt') as l:
    flag = l.readline()

flag = int.from_bytes(flag.encode(), byteorder='big')
ct = pow(flag,e,n)

print(hex(ct))


# c*2-b*4-a*6 = 658989191820960796
# 2c - 4b - 6a = 658989191820960796
# 2c = 658989191820960796 + 4b + 6a
# c = 329494595910480398 + 2b + 3a