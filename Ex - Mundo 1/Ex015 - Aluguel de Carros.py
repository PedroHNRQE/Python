dias = int(input('Quantos dias alugados? '))
kil = float(input('Quantos quilometros rodados? '))
total = (dias * 60) + (kil * 0.15)
print('O total a pagar e de R${:.2f}'.format(total))
