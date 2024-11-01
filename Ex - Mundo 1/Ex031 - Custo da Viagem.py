distancia = int(input('Qual e a distancia da sua viagem? '))
print('Voce esta prestes a comecar uma viagem de {:.1f}Km.'.format(distancia))

if distancia <= 200:
    passagem = distancia * 0.50
    print('E o preco da sua passagem sera de R${:.2f}'.format(passagem))
else:
    passagem = distancia * 0.45
    print('E o preco da sua passagem sera de R${:.2f}'.format(passagem))
