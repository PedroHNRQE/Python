dados = dict()
gols = list()

dados['nome'] = str(input('Nome do Jogador: '))
partidas = int(input(f'Quantas partidas {dados['nome']} jogou? '))
for g in range(0, partidas):
    gols.append(int(input(f'   Quantos gols na partida {g+1}? ')))
    dados['gols'] = gols
dados['total'] = sum(gols)
print('=-' * 25)
print(dados)
print('=-' * 25)
for k, v in dados.items():
    print(f'O campo {k} tem o valor {v}')
print('=-' * 25)
print(f'O jogador {dados['nome']} jogou {partidas} partidas.')
for i, v in enumerate(gols):
    print(f'    => Na partida {i+1}, fez {v} gols.')
print(f'Foi um total de {dados['total']} gols.')