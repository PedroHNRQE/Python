num = int(input('Digite um numero para ver sua tabuada: '))

for c in range(1, 11):
    if num < 0:
        print('Valor Invalido! Tente novamente')
        break
    else:
        print('{} x {} = {}'.format(c, num, c*num))

# Guanabara
n = int(input('Digite um numero para ver sua tabuada: '))

for c in range(1, 11):
    print('{} x {:2} = {}'.format(n, c, n*c))