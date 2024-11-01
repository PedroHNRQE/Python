media = 0
soma = 0
maisVelho = 0
maisVelhoNome = ''
menosVinte = 0

for c in range(1, 5):
    print('----- {}° Pessoa -----'.format(c))
    nome = str(input('Nome: '))
    idade = int(input('Idade: '))
    soma += idade
    sexo = str(input('Sexo [M/F]: '))
    if c == 1:
        maisVelho = idade
    else:
        if sexo in 'Mn':
            if idade > maisVelho:
                maisVelhoNome = nome
                maisVelho = idade
            elif maisVelho == idade:
                maisVelhoNome = nome
                maisVelho = maisVelho
    if sexo in 'Ff' and idade <= 20:
        menosVinte += 1

media += soma / 4
print('-'*20, ' Analise Geral ', '-'*20)
print('A media de idade do grupo é de {} anos'.format(media))
print('O homem mais velho tem {} anos e se chama {}'.format(maisVelho, maisVelhoNome))
print('Ao todo sao {} mulheres com menos de 20 anos'.format(menosVinte))


# Guanabara


somaridade = 0
mediaidade = 0
maioridadehomem = 0
nomevelho = ''
totmulher20 = 0
for p in range(1, 5):
    print('----- {}° Pessoa -----'.format(p))
    nome1 = str(input('Nome: ')).strip()
    idade1 = int(input('Idade: '))
    sexo1 = str(input('Sexo [M/F]: ')).strip()
    somaridade += idade1
    if p == 1 and sexo1 in 'Mm':
        maioridadehomem = idade1
        nomevelho = nome1
    if sexo1 in 'Mm' and idade1 > maioridadehomem:
        maioridadehomem = idade1
        nomevelho = nome1
    if sexo1 in 'Ff' and idade1 < 20:
        totmulher20 += 1
mediaidade = somaridade / 4
print('A media de idade do grupo é de {} anos'.format(mediaidade))
print('O homem mais velho tem {} anos e se chama {}'.format(maioridadehomem, nomevelho))
print('Ao todo sao {} mulheres com menos de 20 anos'.format(totmulher20))
