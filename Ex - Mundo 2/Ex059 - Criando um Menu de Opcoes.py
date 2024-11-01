from time import sleep
n1 = float(input('Primeiro valor: '))
n2 = float(input('Segundo valor: '))
somar = False

while not somar:
    opcao = int(input('[ 1 ] Somar\n[ 2 ] Multiplicar\n[ 3 ] Maior\n[ 4 ] Novos numeros\n[ 5 ] Sair do Programa\n>>>>> Qual é sua opcao? '))
    print('=-=' * 15)
    if opcao == 1:
        soma = n1 + n2
        print('A soma de {} e {} resulta em {}'.format(n1, n2, soma))
    elif opcao == 2:
        produto = n1 * n2
        print('O produto de {} e {} é {}'.format(n1, n2, produto))
    elif opcao == 3:
        maior = n1
        if n2 > maior:
            maior = n2
        print('O maior numero entre {} e {} é {}'.format(n1, n2, maior))
    elif opcao == 4:
        n1 = float(input('Primeiro valor: '))
        n2 = float(input('Segundo valor: '))
    elif opcao == 5:
        print('Finalizando...')
        somar = True
    else:
        print('Valor Invalido')
    print('=-=' * 15)
    sleep(2)
print('Programa Encerrado')

# Guanabara

nu1 = int(input('Primeiro valor: '))
nu2 = int(input('Segundo valor: '))
opcao = 0
while opcao != 5:
    print('''    [ 1 ] somar
    [ 2 ] multiplicar
    [ 3 ] maior
    [ 4 ] novos numeros
    [ 5 ] sair do programa''')
    opcao = int(input('Qual é a sua opcao? '))
    if opcao == 1:
        soma1 = nu1 + nu2
        print('A soma entre {} + {} é {}'.format(nu1, nu2, soma1))
    elif opcao == 2:
        produto1 = nu1 * nu2
        print('O resultado de {} x {} é {}'.format(nu1, nu2, produto1))
    elif opcao == 3:
        if nu1 > nu2:
            maior = nu1
        else:
            maior = nu2
        print('Entre {} e {} o maior valor é {}'.format(nu1, nu2, maior))
    elif opcao == 4:
        print('Informe os numeros novamente: ')
        nu1 = int(input('Primeiro valor: '))
        nu2 = int(input('Segundo valor: '))
    elif opcao == 5:
        print('Finalizando...')
    else:
        print('Opcao invalida. Tente novamente')
print('Fim do programa! Volte sempre!')