print('-'*30)
print('     LOJA SUPER BARATAO     ')
print('-'*30)

soma = mil = menor = cont = 0
barato = ''

while True:
    produto = str(input('Nome do produto: '))
    preco = float(input('Preco: R$ '))
    print('-' * 30)
    continuar = str(input('Quer continuar? [S/N] ')).upper().strip()[0]
    soma += preco
    cont += 1
    if cont == 1:
        menor = preco
        barato = produto
    else:
        if preco < menor:
            menor = preco
            barato = produto
    if preco > 1000:
        mil += 1
    if continuar == 'N':
        break
print('---------- FIM DO PROGRAMA ---------')
print(f'O total da compra foi R${soma:.2f}')
print(f'Temos {mil} produtos custando mais de R$1000.00')
print(f'O produto mais barato foi {barato} que custa R${menor:.2f}')