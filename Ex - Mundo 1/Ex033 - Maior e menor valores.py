a = int(input('Digite o primeiro numero: '))
b = int(input('Digite o segundo numero: '))
c = int(input('Digite o terceiro numero: '))

maior = a
if b > a and b > c:
    maior = b
if c > a and c > b:
    maior = c

menor = b
if a < b and a < c:
    menor = a
if c < b and c < a:
    menor = c

print('Maior numero: {}\nMenor numero: {}'.format(maior, menor))

# Jeito Correto

"""
maior = max(a, b, c)
menor = min(a, b, c)
print('O maior é {} e o menor é {}'.format(maior, menor))
"""