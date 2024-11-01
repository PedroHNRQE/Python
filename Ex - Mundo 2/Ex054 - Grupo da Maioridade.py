from datetime import date

idade = 0
maior = 0
menor = 0

for c in range(1, 8):
    ano = int(input('Em que ano voce nasceu? '))
    idade = 2024 - ano
    if idade >= 18:
        maior += 1
    else:
        menor += 1

print('No total, {} pessoas ja sao de maior, e {} de menor'.format(maior, menor))

# Guanabara

atual = date.today().year
totmaior = 0
totmenor = 0
for pess in range(1, 8):
    nasci = int(input('Em que ano a pessoas nasceu? '))
    ida = atual - nasci
    if ida >= 21:
        totmaior += 1
    else:
        totmenor += 1
print('Ao todo tivemos {} pessoas maiores de idade'.format(totmaior))
print('Ao todo tivemos {} pessoas menores de idade'.format(totmenor))
