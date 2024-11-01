num = int(input('Digite um numero: '))
divisoes = 0


for c in range(1, num + 1):
    if num % c == 0:
        print('\033[33m', end='')
        divisoes += 1
    else:
        print('\033[31m', end='')
    print('{} '.format(c), end='')
print('\n\033[mO numero {} foi divisivel {} vezes'.format(num, divisoes))
if divisoes == 2:
    print('O valor digitado é PRIMO')
else:
    print('O valor digitado nao é PRIMO')

