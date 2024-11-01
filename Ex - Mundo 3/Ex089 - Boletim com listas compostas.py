alunos = list()
temp = list()
c = 0
while True:
    temp.append(str(input('Nome: ')))
    temp.append(float(input('Nota 1: ')))
    temp.append(float(input('Nota 2: ')))
    alunos.append((temp[:]))
    temp.clear()
    r = str(input('Quer Continuar? ')).upper().strip()[0]
    if r not in 'S':
        break
print('=-' * 15)
print('No. NOME       MEDIA')
print('-' * 30)
for a in alunos:
    print(f'{c:<3} {alunos[c][0]:<11} {(alunos[c][1] + alunos[c][2]) / 2}')
    c += 1
print('-' * 30)
while True:
    n = int(input('Mostrar notas de qual aluno? '))
    if n > len(alunos):
        break
    print(f'Notas do {alunos[n][0]} sao {alunos[n][1]} e {alunos[n][2]}')
print('Fim')

# Guanabara

ficha = list()
while True:
    nome = str(input('Nome: '))
    nota1 = float(input('Nota 1: '))
    nota2 = float(input('Nota 2: '))
    media = (nota1 + nota2) / 2
    ficha.append([nome, [nota1, nota2], media])
    resp = str(input('Quer continuar? [S/N] '))
    if resp in 'Nn':
        break
print('-=' * 30)
print(f'{"No.":<4}{"NOME":<10}{"MEDIA":>8}')
print('-' * 26)
for i, a in enumerate(ficha):
    print(f'{i:<4}{a[0]:<10}{a[2]:>8.1f}')
while True:
    print('-' * 35)
    opc = int(input('Mostrar notas de qual aluno? (999 interrompe): '))
    if opc == 999:
        print('FINALIZANDO...')
        break
    if opc <= len(ficha) - 1:
        print(f'Notas de {ficha[opc][0]} sao {ficha[opc][1]}')