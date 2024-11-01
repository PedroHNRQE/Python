print('-=-' * 20)
print('Analisador de Triangulo')
print('-=-' * 20)
a = float(input('Primeiro Triangulo: '))
b = float(input('Segundo Triangulo: '))
c = float(input('Terceiro Triangulo: '))

if a + b > c and a + c > b and b + c > b:
    if a == b == c:
        print('EQUILÁTERO: todos os lados iguais')
    elif a != b == c or a != c == b or b != c == a:
        print('ISÓSCELES: dois lados iguais, um diferente')
    elif a != b != c:
        print("ESCALENO: todos os lados diferentes")
else:
    print('Nao Triangulo')