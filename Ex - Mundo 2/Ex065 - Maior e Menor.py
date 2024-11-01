continuar = 'S'
cont = soma = maior = menor = 0
while continuar != 'N':
# while continuar in 'Ss:' Tambem serve, previne bug
    n = float(input('Digite um numero: '))
    continuar = str(input('Quer continuar? [S/N] ')).upper()
    cont += 1
    soma += n
    if cont == 1:
        maior = menor = n
    else:
        if n > maior:
            maior = n
        if n < menor:
            menor = n
print('Voce digitou {} numeros e a media foi {}'.format(cont, soma/cont))
print('O maior valor foi {} e o menor foi {}'.format(maior, menor))