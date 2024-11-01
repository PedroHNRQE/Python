aluno = dict()


aluno['nome'] = str(input('Nome: '))
aluno['media'] = float(input(f'Media de {aluno['nome']}: '))
print('=-' * 20)
print(f' - nome é igual a {aluno['nome']}')
print(f' - media é igual a {aluno['media']}')
print(f' - Situacao é igual a ', end='')
if aluno['media'] >= 7:
    aluno['situacao'] = 'APROVADO'
elif aluno['media'] <= 4:
    aluno['situacao'] = 'REPROVADO'
else:
    aluno['situacao'] = 'EM RECUPERACAO'
print(aluno['situacao'])

 # Guanabara
 # No caso o codigo foi quase o mesmo, com a diferenca de da forma mostrar o resultado
print('Usando o FOR')
for k, v in aluno.items():
    print(f' - {k} é igual a {v}')

