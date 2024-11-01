numero = int(input("Digite um numero: "))

milha = (numero // 1000) % 10
centenas = (numero // 100) % 10
dezenas = (numero // 10) % 10
unidade = (numero // 1) % 10

print('Unidade: {} \nDezena: {} \nCentena: {} \nMilhar: {}'.format(unidade, dezenas, centenas, milha))
