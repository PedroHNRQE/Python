numeros = list()
pares = list()
impares = list()

c = 0
for n in range(1, 8):
    numeros.append(int(input(f'Digite o {n}° valor: ')))
    if numeros[c] % 2 == 0:
        pares.append(numeros[c])
        c += 1
    elif numeros[c] % 2 == 1:
        impares.append(numeros[c])
        c += 1
pares.sort()
impares.sort()
print('=-=' * 20)
print(f'Os valores pares digitados foram {pares}')
print(f'Os valores impares digitados forma {impares}')

# Guanabara

numeros = [[], []]
valor = 0
for c in range(1, 8):
    valor = int(input(f'Digite o {c}° valor: '))
    if valor % 2 == 0:
        numeros[0].append(valor)
    elif valor % 2 == 1:
        numeros[1].append(valor)
print('-=' * 30)
numeros[0].sort()
numeros[1].sort()
print(numeros[0])
print(numeros[1])