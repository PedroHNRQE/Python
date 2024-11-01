import math

a = (float(input('Digite o angulo que voce deseja: ')))

aRadius = math.radians(a)

seno = math.sin(aRadius)
cosseno = math.cos(aRadius)
tangente = math.tan(aRadius)

print('O angulo de {} tem o SENO de {:.2f}'.format(a, seno))
print('O angulo de {} tem o COSSENO de {:.2f}'.format(a, cosseno))
print('O angulo de {} tem o TANGENTE de {:.2f}'.format(a, tangente))
