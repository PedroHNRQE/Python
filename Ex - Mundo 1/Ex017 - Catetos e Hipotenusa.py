from math import sqrt, hypot

catetoO = float(input('Comprimento do cateto oposto: '))
catetoA = float(input('Comprimento do cateto adjacente: '))

##hipo = sqrt(catetoO * catetoO + catetoA * catetoA)
hipo = hypot(catetoO, catetoA)

print('A hipotenusa vai medir {:.2f}'.format(hipo))
