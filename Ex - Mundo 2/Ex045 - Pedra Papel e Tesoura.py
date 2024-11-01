import random
opcao = int(input(' Suas opcoes: \n [ 1 ] PEDRA\n [ 2 ] PAPEL\n [ 3 ] TESOURA\nQual e a sua jogada? '))
pedra = 'PEDRA'
papel = "PAPEL"
tesoura = 'TESOURA'
opcaoPc = [pedra, papel, tesoura]
pc = random.choice(opcaoPc)

if opcao == 1:
    opcao = 'PEDRA'
elif opcao == 2:
    opcao = 'PAPEL'
elif opcao == 3:
    opcao = 'TESOURA'

print('-=' * 20)
print('PC jogou {}'.format(pc))
print('Jogador jogou {}'.format(opcao))
print('-=' * 20)

if opcao == pc:
    print('EMPATE!!')
elif opcao == 'PAPEL' and pc == 'TESOURA':
    print('PC GANHOU!!')
elif opcao == 'PAPEL' and pc == 'PEDRA':
    print('VOCE GANHOU!!')
elif opcao == 'TESOURA' and pc == 'PAPEL':
    print('VOCE GANHOU!!')
elif opcao == 'TESOURA' and pc == 'PEDRA':
    print('PC GANHOU!!')
elif opcao == 'PEDRA' and pc == 'PAPEL':
    print('PC GANHOU!!')
elif opcao == 'PEDRA' and pc == 'TESOURA':
    print('VOCE GANHOU!!')
