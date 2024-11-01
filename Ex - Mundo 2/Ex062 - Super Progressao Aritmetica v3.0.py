print('Gerador de PA')
print('=-=' * 5)
p1 = int(input('Primeiro termo: '))
r = int(input('Razao da PA: '))
novoTermo = 1
termo = p1
cont = 1
while cont <= 10:
    print('{} -> '.format(termo), end='')
    termo += r
    cont += 1
print('Fim')
while novoTermo != 0:
    novoTermo = int(input('Quantos termos voce quer mostrar a mais? '))
    novoCont = cont + novoTermo - 1
    while cont <= novoCont:
        print('{} -> '.format(termo), end='')
        termo += r
        cont += 1
    print('Fim')

# Guanabara

print('Gerador de PA')
print('-=' * 10)
primeiro = int(input('Primeiro termo: '))
razao = int(input('Razao de PA: '))
termo1 = primeiro
contador = 1
total = 0
mais = 10
while mais != 0:
    total = total + mais
    while contador <= total:
        print('{} -> '.format(termo1), end='')
        termo1 += razao
        contador += 1
    print('PAUSA')
    mais = int(input('Quantos termos voce quer mostrar a mais? '))
print('Progressao finalizada com {} termos.'.format(contador))