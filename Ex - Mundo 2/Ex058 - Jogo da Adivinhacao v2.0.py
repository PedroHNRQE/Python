from random import randint
pc = randint(0, 10)
cont = 1
eu = int(input('Sou seu computador...\nAcabei de pensar em um numero entre 0 e 10.\nSera que voce consegue adivinhar qual foi?\nQual é seu palpite? ')).strip

while eu != pc:
    if eu < pc:
        print('Mais... Tente mais uma vez. ')
        eu = int(input('Qual é seu palpite? ')).strip
        cont += 1
    elif eu > pc:
        print('Menos... Tente mais uma vez. ')
        eu = int(input('Qual é seu palpite? ')).strip
        cont += 1
print('Acertou com {} tentativas.'.format(cont))

# Guanabara

# from random import randint
computador = randint(0, 10)
print('Sou seu computador... Acabei de pensar em um numero entre 0 e 10.')
print('Sera que voce consegue adivinhar qual foi?')
acertou = False
palpites = 0
while not acertou:
    jogador = int(input('Qual é seu palpite? '))
    palpites += 1
    if jogador == computador:
        acertou = True
    else:
        if jogador < computador:
            print('Mais... Tente mais uma vez.')
        elif jogador > computador:
            print('Menos... Tente mais uma vez. ')
print('Acertou com {} palpites'.format(palpites))