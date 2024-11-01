valorCasa = float(input('Qual e o valor da casa: '))
salarioComprador = float(input('Valor do salario: '))
anosParaPagar = float(input('Em quantos anos vai ser pago: '))

mensalidade = valorCasa / (anosParaPagar * 12)
salario30 = 30 * salarioComprador / 100

print('Para pagar uma casa de R${:.2f} em {} anos a prestacao sera de R${:.2f}'.format(valorCasa, anosParaPagar, mensalidade))

if mensalidade > salario30:
    print('Emprestimo NEGADO!')
else:
    print('Emprestimo APROVADO!')