grupo = list()
pessoa = list()
maior = list()
menor = list()

while True:
    pessoa.append(str(input('Nome: ')))
    pessoa.append(float(input('Peso: ')))
    r = str(input('Quer Continuar? ')).upper().strip()[0]
    grupo.append(pessoa[:])
    pessoa.clear()
    if r not in 'S':
        break

print(f'Ao todo, voce cadastrou {len(grupo)} pessoas')
n = 0
peso = list()
for p in grupo:
    peso.append(grupo[n][1])
    n += 1
    if p[1] == max(peso):
        maior.append(p[0])
    elif p[1] == min(peso):
        menor.append(p[0])

print(f'O maior peso foi {max(peso):.1f}Kg. Peso de {maior}')
print(f'O menor peso foi {min(peso):.1f}Kg. Peso de {menor}')



