preco = float(input('Qual e o preco do produto? R$'))
des = 5 * preco / 100
preFin = preco - des
print('O produto que custava R${:.2f}, na promocao com desconto de 5% vai custar R${:.2f}'.format(preco, preFin))
