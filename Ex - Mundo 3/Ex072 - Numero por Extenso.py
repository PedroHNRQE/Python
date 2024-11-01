numeros = ('zero', 'um', 'dois', 'tres', 'quatro', 'cinco', 'seis', 'sete', 'oito', 'nove', 'dez',
           'onze', 'doze', 'treze', 'quatorze', 'quinze', 'dezesseis', 'dezessete', 'dezoito', 'dezenove', 'vinte')

while True:
    n = int(input('Digite um numero entre 0 e 20: '))
    while n > 20 or n < 0:
        n = int(input('Tente novamente. Digite um numero entre 0 e 20: '))
    print('-' * 30)
    print(f'Voce digitou o numero {numeros[n]}')
    print('-' * 30)
    opcao = str(input('Voce quer continuar? [S/N] ')).upper().strip()[0]
    if opcao in "N":
        break
    if opcao not in 'S':
        opcao = str(input('Valor Invalido. Voce quer continuar? [S/N] ')).upper().strip()[0]

# Guanabara

'''cont = ('zero', 'um', 'dois', 'tres', 'quatro', 'cinco', 'seis', 'sete', 'oito', 'nove', 'dez',
        'onze', 'doze', 'treze', 'quatorze', 'quinze', 'dezesseis', 'dezessete', 'dezoito', 'dezenove', 'vinte')
while True:
    num = int(input('Digite um numero entre 0 e 20: '))
    if 0 <= num <= 20:
        break
    print(f'Digite novamente. ', end='')
print(f'Voce digitou o numero {cont[num]}')'''