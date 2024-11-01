soma = 0

for c in range(1, 7):
    num = int(input('Digite um numero: '))
    if num % 2 == 0:
        soma += num
print(soma)

# Guanabara

soma1 = 0
cont = 0

for c in range(1, 7):
    num1 = int(input('Digite o {}° valor: '.format(c)))
    soma1 += num1
    cont += 1
print('Voce informou {} numeros e a soma foi {}'.format(cont, soma))