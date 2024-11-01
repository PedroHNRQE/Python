cont = 1
while True:
    print('=-='*13)
    num = int(input('Quer ver a tabuada de qual valor? '))
    print('=-='*13)
    if num < 0:
        print('Valor invalido')
        break
    while True:
        print(f'{num} x {cont:2} = {cont * num:2}')
        cont += 1
        if cont == 11:
            cont = 1
            break
print('FIM')

# Guanabara

while True:
    n = int(input('Quer ver tabuada de qual valor? '))
    print('-' * 30)
    if n < 0:
        break
    for c in range(1, 11):
        print(f'{n} x {c} = {num * c}')
    print('-' * 30)
print('PROGRAMA TABUADA ENCERRADO. Volte sempre! ')



