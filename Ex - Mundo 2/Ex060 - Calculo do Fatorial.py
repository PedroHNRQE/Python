from math import factorial
num = int(input('Digite um numero para calcular seu fatorial: '))
fatorial = factorial(num)

print('Calculando {}! = '.format(num), end='')
while num > 0:
    print('{}'.format(num), end='')
    print(' x ' if num > 1 else ' = ', end='')  # Isso aqui roubei na net, basicamente coloca o " = " se o num for igual a 1, antes disso ele sempre coloca o ' x '
    num -= 1
print('{}'.format(fatorial))

# Guanabara

n = int(input('Digite um numero para calcular seu Fatorial: '))
c = n
f = 1
print('Calculando {} ! = '.format(n), end='')
while c > 0:
    print('{}'.format(c), end='')
    print(' x ' if c > 1 else ' = ', end='')
    f *= 1  # f = f * 1
    c -= 1
print('{}'.format(f))
