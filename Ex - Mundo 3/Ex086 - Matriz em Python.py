matriz = [[], [], []]

for c in range(0, 3):
    valor = int(input(f'Digite um valor [0], [{c}]: '))
    matriz[0].append(valor)
for c in range(0, 3):
    valor = int(input(f'Digite um valor [1], [{c}]: '))
    matriz[1].append(valor)
for c in range(0, 3):
    valor = int(input(f'Digite um valor [2], [{c}]: '))
    matriz[2].append(valor)

print(f'{matriz[0]}\n{matriz[1]}\n{matriz[2]}')

# Guanabara

matriz = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
for linha in range(0, 3):
    for coluna in range(0, 3):
        matriz[linha][coluna] = (int(input(f'Digite um valor para [{linha}], [{coluna}]: ')))

for linha in range(0, 3):
    for coluna in range(0, 3):
        print(f'[{matriz[linha][coluna]:^5}]', end='')
    print()