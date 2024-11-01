salario = float(input('Digite seu salario: '))
aumento15 = 15 * salario / 100
aumento10 = 10 * salario / 100

if salario <= 1250:
    salario = salario + aumento15
    print(salario)
else:
    salario = salario + aumento10
    print(salario)