salario = float(input('Digite seu salario atual: R$'))
aumento = 15 * salario / 100
salarioFinal = salario + aumento
print('seu salario que era de R${:.2f} com o aumento de 15% ficara R${:.2f}'.format(salario, salarioFinal))
