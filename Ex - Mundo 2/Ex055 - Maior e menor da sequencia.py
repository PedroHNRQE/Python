maior = 0
menor = 0

for c in range(1, 6):
    peso = float(input('Peso da {}° pessoa: '.format(c)))
    if c == 1:
        maior = c
        menor = c
    else:
        if peso > maior:
            maior = peso
        menor = peso
        if menor < peso:
            menor = peso
print('O maior peso foi {}Kg'.format(maior))
print('O menor peso foi {}Kg'.format(menor))