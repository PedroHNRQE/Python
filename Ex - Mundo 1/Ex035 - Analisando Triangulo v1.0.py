print('-=-' * 20)
print('Analisador de Triangulo')
print('-=-' * 20)
a = float(input('Primeiro Triangulo: '))
b = float(input('Segundo Triangulo: '))
c = float(input('Terceiro Triangulo: '))

if a + b > c and a + c > b and b + c > b:
    print("Triangulo")
else:
    print('Nao Triangulo')