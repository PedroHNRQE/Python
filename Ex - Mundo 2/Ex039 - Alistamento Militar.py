anoNascimento = int(input('Digite o ano do seu nascimento: '))
idade = 2024 - anoNascimento
tempo = 18 - idade
tempo1 = idade - 18
alistamento = anoNascimento + 18

print('Quem nasceu em {} tem {} anos em 2024'.format(anoNascimento, idade))

if idade < 18:
    print('Ainda faltam {} ano(s) para o alistamento'.format(tempo))
    print('Seu alistamento sera em {}'.format(alistamento))
elif idade == 18:
    print('Voce tem que se alistar IMEDIATAMENTE')
else:
    print('Voce ja deveria ter se alistado ha {} anos'.format(tempo1))
    print('Seu alistamento foi em {}'.format(alistamento))
