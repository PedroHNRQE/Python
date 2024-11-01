numeros = list()

for p in range(0, 5):
    n = int(input('Digite um valor: '))
    if p == 0 or n > numeros[-1]:
        numeros.append(n)
        print('Adicionado ao final da lista... ')
    else:
        pos = 0
        while pos < len(numeros):
            if n <= numeros[pos]:
                numeros.insert(pos, n)
                print(f'Adicionado na posicao {pos} da lista... ')
                break
            pos += 1
        # print('Valor duplicado! Digite novamente')

print(f'O valores digitados foram {numeros}')