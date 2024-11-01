p1 = int(input('Primeiro Termo: '))
r = int(input('Razao: '))
p10 = 10 * r

for c in range(p1, p10, r):
    print(c, end=' -> ', )
print('Acabou')

# Guanabara

primeiro = int(input('Primeiro Termo: '))
razao = int(input('Razao: '))
decimo = primeiro + (10 - 1) * razao
for c in range(primeiro, decimo + razao, razao):
    print('{} '.format(c), end='-> ')
print('Acabou')