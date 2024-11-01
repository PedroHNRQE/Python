from datetime import datetime
dados = dict()

while True:
    dados['nome'] = str(input('Nome: '))
    dados['idade'] = int(input('Ano de Nascimento: '))
    dados['carteira'] = int(input("Carteira de Trabalho (0 nao tem): "))
    if dados['carteira'] == 0:
        del dados['carteira']
        break
    else:
        dados['contratacao'] = int(input('Ano da Contratacao: '))
        dados['salario'] = float(input('Salario: R$'))
        break
dados['idade'] = datetime.now().year - dados ['idade']
dados['aposentadoria'] = dados['idade'] + (dados ['contratacao'] + 35) - datetime.now().year

print('=-' * 15)
for k, v in dados.items():
    print(f' - {k} tem o valor {v}')


