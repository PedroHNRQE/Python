n = 1
soma = 0
cont = 0

while n != 999:
    n = int(input('Digite um numero [999 para parar]: '))
    cont += 1
    soma += n
    if n == 999:
        soma -= 999
        cont -= 1
print('Voce digitou {} numeros e a soma entre eles foi {}'.format(cont, soma))