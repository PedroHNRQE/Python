matriz = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
pares = coluna3 = mai = 0

for linha in range(0, 3):
    for coluna in range(0, 3):
        matriz[linha][coluna] = int(input(f'Digite um valor para [{linha}], [{coluna}]: '))
        if matriz[linha][coluna] % 2 == 0:
            pares += matriz[linha][coluna]
        if matriz[linha][coluna] == matriz[linha][2]:
            coluna3 += matriz[linha][coluna]

for c in range(3):
    if c == 0:
        mai = matriz[1][c]
    elif matriz[1][c] > mai:
        mai = matriz[1][c]

for linha in range(3):
    for coluna in range(3):
        print(f'[{matriz[linha][coluna]:^5}]', end='')
    print()
print('=-=' * 30)
print(f'A soma de todos os pares é {pares}')
print(f'A soma dos valores da terceira coluna é {coluna3}')
print(f'O maior valor da segunda linha é {mai}')