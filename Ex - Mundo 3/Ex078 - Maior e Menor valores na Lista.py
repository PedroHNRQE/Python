valores = [int(input('Digite um valor para a posicao 0: ')),
           int(input('Digite um valor para a posicao 1: ')),
           int(input('Digite um valor para a posicao 2: ')),
           int(input('Digite um valor para a posicao 3: ')),
           int(input('Digite um valor para a posicao 4: '))]

n1 = min(valores)
n2 = max(valores)
print('=-=' * 30)
print(f'Voce digitou os valores {valores}')
print(f"O menor valor digitado foi {n1} na posicao {valores.index(n1)}")
print(f'O maior valor digitado foi {n2} na posicao {valores.index(n2)}')

# Guanabara

listanum = []
mai = 0
men = 0
for c in range(0, 5):
    listanum.append(int(input(f'Digite um valor para a posicao {c}: ')))
    if c == 0:  # ou seja, para o c ser igual a zero, ele é o primeiro valor a ser lido
        mai = men = listanum[c]
    else:
        if listanum[c] > mai:
            mai = listanum[c]
        if listanum[c] < men:
            men = listanum[c]
print('=-' * 30)
print(f'Voce digitou os valores {listanum}')
print(f"O menor valor digitado foi {men} na posicao ", end='')
for i, v in enumerate(listanum):
    if v == men:
        print(f'{i}... ', end='')
print(f'\nO maior valor digitado foi {mai} na posicao ', end='')
for i, v in enumerate(listanum):
    if v == mai:
        print(f'{i}... ', end='')