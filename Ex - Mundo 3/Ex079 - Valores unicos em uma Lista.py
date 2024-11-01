lista = []

while True:
    lista.append(int(input('Digite um valor: ')))
    for i, elemento in enumerate(lista):
        if elemento in lista[i + 1:]:
            print(f'Elemento repetido: {elemento}')
            lista.remove(elemento)
    opcao = str(input('Quer continuar? [S/N] ')).upper().strip()[0]
    if opcao == 'N':
        lista.sort()
        print(f'{lista}')
        break

# Guanabara

numeros = list()

while True:
    n = int(input('Digite um valor: '))
    if n not in numeros:
        numeros.append(n)
        print('Valor adicionado com sucesso...')
    else:
        print('Valor duplicado! Nao vou adicionar...')
    r = str(input('Quer continuar ?'))
    if r in 'Nn':
        break
print('-=' * 30)
numeros.sort()
print(f'Voce digitou os valores {numeros}')