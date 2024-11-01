nome = str(input('Digite seu nome completo: '))
namelist = nome.split()
name = ''.join(namelist)

print('Seu nome em maiúsculo é: {}'.format(nome.upper()))
print('Seu nome em minúsculo é: {}'.format(nome.lower()))
print('Seu nome tem ao todo {} letras'.format(len(name)))
print('Seu primeiro nome e {} e ele tem {} letras'.format(namelist[0], len(namelist[0])))



