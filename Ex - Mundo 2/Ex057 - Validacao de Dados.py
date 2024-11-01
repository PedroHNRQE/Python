s = str(input('Informe seu sexo: [M/F] ')).upper()

while s not in ['F', 'M']:
    s = str(input('Valor invalido, informe seu sexo: ')).upper()

print('Sexo {} registrado com sucesso'.format(s))

# Guanabara

sexo = str(input('Informe seu sexo: [M/F] ')).strip().upper()[0]  # Esse '[0]', vai pegar a primeira letra, ou seja, se for digitado 'feminino', ele pega so o 'f'

while s not in 'FfMm':
    sexo = str(input('Dados invalidos. Por favor, informe seu sexo: ')).strip().upper()[0]

print('Sexo {} registrado com sucesso'.format(sexo))