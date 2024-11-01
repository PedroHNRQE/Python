import math


numeroInteiro = int(input('Digite um numero inteiro: '))
opcao = int(input('[ 1 ] converter para BINARIO\n[ 2 ] converter para OCTAL\n[ 3 ] converter para HEXADECIMAL\nSua opcao: '))

if opcao == 1:
    binario = bin(numeroInteiro)[2:]
    print(binario)
elif opcao == 2:
    octal = oct(numeroInteiro)[2:]
    print(octal)
elif opcao == 3:
    hexa = hex(numeroInteiro)[2:]
    print(hexa)
else:
    print('Opcao Invalida!!')






