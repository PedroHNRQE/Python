from random import randint

n1 = randint(1, 10)
n2 = randint(1, 10)
n3 = randint(1, 10)
n4 = randint(1, 10)
n5 = randint(1, 10)
valores = n1, n2, n3, n4, n5

print(f'Os valores sorteados foram: ', end='')
for i in valores:
    print(i, end=' ')

print(f'\n O maior valor sorteado foi {max(valores)}')
print(f'O menor valor sorteado foi {min(valores)}')

# Guanabara

numeros = randint(1, 10), randint(1, 10), randint(1, 10), randint(1, 10), randint(1, 10)

print(f'Os valores sorteados foram: ', end='')
for n in numeros:
    print(n, end=' ')

print(f'\nO maior valor sorteado foi {max(numeros)}')
print(f'O menor valor sorteado foi {min(numeros)}')