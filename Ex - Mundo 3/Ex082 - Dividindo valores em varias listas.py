lista = list()
pares = list()
impares = list()

while True:
    n = int(input('Digite um valor: '))
    lista.append(n)
    r = str(input('Quer continuar? ')).upper().strip()[0]
    if n % 2 == 0:
        pares.append(n)
    else:
        impares.append(n)
    if r not in 'S':
        break
print(f'A lista completa é {lista}')
print(f'A lista de pares é {pares}')
print(f'A lista de impares é {impares}')

# Guanabara

num = list()
pares1 = list()
impares1 = list()

while True:
    num.append(int(input('Digite um numero: ')))
    resp = str(input('Quer continuar? [S/N] '))
    if resp in 'Nn':
        break
for i, v in enumerate(num):
    if v % 2 == 0:
        pares.append(v)
    elif v % 2 == 1:
        impares.append(v)
print('-=' * 30)
print(f'A lista completa é {num}')
print(f'A lista de pares é {pares1}')
print(f'A lista de impares é {impares1}')