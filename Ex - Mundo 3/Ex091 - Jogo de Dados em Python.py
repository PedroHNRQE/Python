from random import randint
from time import sleep
from operator import itemgetter

jogadores = dict()
podio = list()

for j in range(1, 5):
    jogadores[f'jogador{j}'] = randint(1, 6)

print('Valores Sorteados: ')
for k, v in jogadores.items():
    print(f'{k} tirou {v} no dado')
    sleep(1)

print('=-=' * 15)
print(f'{"==":>4}{" RANKING DOS JOGADORES ":^4}{"==":<4}')
podio = sorted(jogadores.items(), key=itemgetter(1), reverse=True)  # Entendi nada

for i, v in enumerate(podio):
    print(f'  {i+1} lugar: {v[0]} com {v[1]}')



