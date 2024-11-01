valores = int(input('Digite um numero: ')), int(input('Digite outro numero: ')), int(input('Digite mais um numero: ')), int(input('Digite o ultimo numero: '))

print(f'Voce digitou os valores {valores}')
print(f'O valor 9 apareceu {valores.count(9)} vezes')
if 3 in valores:
    print(f'O valor 3 apareceu na {valores.index(3)+1}ª posicao')
else:
    print(f'O valor 3 nao esta na tupla')
print(f'Os valores pares digitados foram: ', end='')
for i in valores:
    if i % 2 == 0:
        print(i, end=' ')

