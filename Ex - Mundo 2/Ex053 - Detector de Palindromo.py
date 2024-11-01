frase = str(input('Digite uma frase: ')).upper().split()
frase = ''.join(frase)
fraseIn = ''

for c in range(len(frase) - 1, -1, -1):
    fraseIn += frase[c]

print('O inverso de {} é {}'.format(frase, fraseIn))
if frase == fraseIn:
    print('A frase digitada é um palindromo!')
else:
    print('A frase digitada nao é um palindromo!')


