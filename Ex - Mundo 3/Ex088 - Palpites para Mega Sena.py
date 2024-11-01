from random import randint
from time import sleep
p = list()

print('-' * 30)
print(f'{'JOGO NA MEGA SENA':^30}')
print('-' * 30)
jogos = int(input('Quantos jogos voce quer que eu sorteie? '))

for j in range(1, jogos+1):
    for n in range(0, 6):
        numero = randint(1, 60)
        if numero in p:
            numero = randint(1, 60)
        p.append(numero)
    print(f'Jogo {j}: {p}')
    sleep(1.5)
    p.clear()

# Guanabara

lista = list()
jogoz = list()
print('-' * 30)
print('      JOGO NA MEGA SENA      ')
print('-' * 30)
quant = int(input('Quantos jogos voce quer eu sorteie? '))
tot = 1
while tot <= quant:
    cont = 0
    while True:
        num = randint(1, 60)
        if num not in lista:
            lista.append(num)
            cont += 1
        if cont >= 6:
            break
    lista.sort()
    jogoz.append(lista[:])
    lista.clear()
    tot += 1
print('-=' * 3, f' SORTEANDO {quant} JOGOS ', '-=' * 3)
for i, l in enumerate(jogoz):
    print(f'Jogo {i+1}: {l}')