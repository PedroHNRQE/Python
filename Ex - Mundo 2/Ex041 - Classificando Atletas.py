ano = int(input('Digite o ano de nascimento: '))
idade = 2024 - ano
print(idade)

if idade > 25:
    print('Acima de 25 anos: MASTER')
elif 19 <= idade < 25:
    print('Até 25 anos: SÊNIOR')
elif 14 <= idade < 19:
    print('Até 19 anos: JÚNIOR')
elif 9 <= idade < 14:
    print('Até 14 anos: INFANTIL')
elif idade < 9:
    print('Até 9 anos: MIRIM')
else:
    print('Valor Invalido! ')