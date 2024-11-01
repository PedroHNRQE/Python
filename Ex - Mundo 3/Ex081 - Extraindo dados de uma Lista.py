numeros = list()

while True:
    n = int(input('Digite um valor: '))
    o = str(input('Quer continuar? ')).upper().strip()[0]
    if n not in numeros:
        numeros.append(n)
    else:
        print("Valor duplicado! ")
    if o not in 'S':
        break
print(f'Voce digitou {len(numeros)} elementos. ')
numeros.sort(reverse=True)
print(f'Os valores em ordem decrescente sao {numeros}')
if 5 in numeros:
    print('O valor 5 faz parte da lista!')
else:
    print('O valor 5 nao faz parte da lista!')