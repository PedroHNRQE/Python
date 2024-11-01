n1 = float(input('Primeira nota: '))
n2 = float(input('Segunda nota: '))
media = (n1 + n2) / 2
print('Sua nota: {}'.format(media))

if media >= 7:
    print('Média 7.0 ou superior: APROVADO')
elif media > 5:
    print('Média entre 5.0 e 6.9: RECUPERAÇÃO')
elif media < 5:
    print('Média abaixo de 5.0: REPROVADO')
else:
    print('Valor Invalido!')