frase = str(input('Digite uma frase: ')).upper()
vezes = frase.count('A')
primeira = frase.find('A')+1
ultima = frase.rfind('A')+1
print('A letra A aparece {} vezes na frase. '.format(vezes))
print('A primeira letra A apareceu na posicao {}'.format(primeira))
print('A ultima letra A apareceu na posicao {}'.format(ultima))
