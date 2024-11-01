grupo = list()
pessoa = dict()
mulheres = list()

soma = 0
while True:
    pessoa['nome'] = str(input('Nome: '))
    pessoa['sexo'] = str(input('Sexo [M/F] ')).upper().strip()[0]
    if pessoa['sexo'] == 'F':
        mulheres.append(pessoa['nome'])
    while pessoa['sexo'] not in 'FM':
        print('ERRO! Digite somente M ou F.')
        pessoa['sexo'] = str(input('Sexo [M/F] ')).upper().strip()[0]
    pessoa['idade'] = int(input('Idade: '))
    soma += pessoa['idade']
    resp = str(input('Quer Continuar? ')).upper().strip()[0]
    grupo.append(pessoa.copy())
    while resp not in 'SN':
        print('ERRO! Digite somente Sim ou Nao.')
        resp = str(input('Quer Continuar? ')).upper().strip()[0]
    if resp in 'N':
        break
media = soma / len(grupo)
print('=-' *20)
print(f'A) Ao todo temos {len(grupo)} pessoas cadastradas.')
print(f'B) A media de idade é de {media:.1f} anos')
print(f'C) As mulheres cadastradas foram ', end='')
for m in mulheres:
    print(f'{m} ', end='')
print(f'\nD) Lista das pessoas que estao acima da media: ')
for v in grupo:
    if v['idade'] >= media:
        print(f' nome = {v['nome']}; sexo = {v['sexo']}; idade = {v['idade']}')
print('<<< ENCERRADO >>>')
