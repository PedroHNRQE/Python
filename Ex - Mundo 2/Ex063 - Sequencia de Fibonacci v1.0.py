print('=-=' * 10)
print('Sequencia de Fibonacci')
print('=-=' * 10)
termo = int(input('Quantos termos voce quer mostrar? '))
cont = 2
n1 = 0
n2 = 1

print('{} -> {} -> '.format(n1, n2), end='')
while cont < termo:
    n3 = n1 + n2
    print('{} -> '.format(n3), end='')
    n1 = n2
    n2 = n3
    cont += 1
print('FIM')






