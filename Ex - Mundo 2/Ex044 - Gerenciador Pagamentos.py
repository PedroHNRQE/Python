preco = float(input('Preco das compras" R$'))
opcao = int(input('FORMAS DE PAGAMENTO\n[ 1 ] a vista dinheiro/cheque\n[ 2 ] a vista cartao\n[ 3 ] 2x no cartao\n[ 4 ] 3x ou mais no cartao\nQual e a opcao? '))




if opcao == 1:
    desconto = (10 * preco) / 100
    precoFinal = preco - desconto
    print('Valor total R${:.2f}'.format(precoFinal))
elif opcao == 2:
    desconto = (5 * preco) / 100
    precoFinal = preco - desconto
    print('Valor total R${:.2f}'.format(precoFinal))
elif opcao == 3:
    parcela = preco / 2
    print('Valor total R${:.2f}, parcelado em 2x no valor de R${:.2f}'.format(preco, parcela))
elif opcao == 4:
    juros = (20 * preco) / 100
    precoFinal = preco + juros
    parcela = precoFinal / 3
    print('Valor total R${:.2f}, parcelado em 3x (com juros) no valor de R${:.2f}'.format(preco, parcela))
else:
    (print('Valor Invalido!'))