velocidade = int(input('Qual e a velocidade atual do carro? '))

if velocidade > 80:
    multa = (velocidade - 80) * 7
    print('MULTADO! Voce excedeu o limite permitido que e de 80Km/h')
    print('Voce deve pagar uma multa de R${:.2f}!'.format(multa))
else:
    print('Tenha um bom dia! Dirija com seguranca')
