from random import randint
pc = randint(1, 10)
partidas = 0
vitorias = 0
par = 'DEU PAR'
impar = 'DEU IMPAR'
resultado = ''

print('=-='*20)
print('VAMOS JOGAR PAR OU IMPAR')
print('=-='*20)

while True:
    eu = int(input('Digite um valor: '))
    votoeu = str(input('Par ou Impar? [P/I] ')).upper().strip()
    if votoeu not in "PpIi":
        print('Valor Invalido!')
        break
    soma = eu + pc
    if soma % 2 == 0:
        resultado = par
    else:
        resultado = impar
    print('-' * 45)
    print(f'Voce jogou {eu} e o computador {pc}. Total de {eu + pc} {resultado}')
    print('-' * 45)
    if votoeu == 'P' and resultado == par:
        print('Voce GANHOU!')
        partidas += 1
        vitorias += 1
    elif votoeu == 'P' and resultado == impar:
        print('Voce PERDEU!')
        partidas += 1
    elif votoeu == 'I' and resultado == par:
        print('Voce PERDEU!')
        partidas += 1
    elif votoeu == 'I' and resultado == impar:
        print('Voce GANHOU!')
        partidas += 1
        vitorias += 1
    if partidas == 2:
        break
print(f'GAME OVER! Voce venceu {vitorias} vezes.')

# Guanabara
v = 0
while True:
    jogador = int(input('Difa um valor: '))
    computador = randint(0, 10)
    total = jogador + computador
    tipo = ' '
    while tipo not in 'PI':
        tipo = str(input('Par ou Impar? [P/I]')).strip().upper()[0]
    print(f'Voce jogou {jogador} e o computador {computador}. Total de {total}')
    print(f'DEU PAR' if total % 2 == 0 else 'DEU IMPAR')
    if tipo == 'P':
        if total % 2 == 0:
            print('Voce VENCEU!')
            v += 1
        else:
            print('Voce PERDEU!')
            break
    elif tipo == 'I':
        if total % 2 == 1:
            print('Voce VENCEU!')
            v += 1
        else:
            print('Voce PERDEU!')
            break
    print('Vamos jogar novamente...')
print(f'GAME OVER! Voce venceu {v} vezes')