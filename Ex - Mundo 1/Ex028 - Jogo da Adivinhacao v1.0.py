from random import randint
from time import sleep

print('-=-' * 20)
print('Vou pensar em um numero entre 0 e 5. Tente adivinhar...')
print('-=-' * 20)

v1 = int(input('Em que numero eu pensei? '))
v2 = randint(0, 5)

print('Processando...')
sleep(2)

if v1 == v2:
    print('Parabens! Eu pensei no numero {}, voce ganhou.'.format(v2))
else:
    print('Voce errou! Eu pensei no numero {}, nao o {}'.format(v2, v1))




