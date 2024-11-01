real = float(input('Quantos reais voce tem na carteira? R$ '))
dolar = real / 3.27
print('Com R${} voce pode comprar US${:.2f}'.format(real, dolar))
