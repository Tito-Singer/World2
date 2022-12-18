import random
from time import sleep
itens = ('Pedra', 'Papel', 'Tesoura')
print('\033[1:30:43mBem-vindo ao jogo de Jokenpô\033[m\n')
sleep(0.5)
escolhaHumano = int(input('\033[1:30:42mPara jogar comigo, escolha uma das opções abaixo:\033[m\n'
                          '0 - Pedra\n'
                          '1 - Papel\n'
                          '2 - Tesoura\n'
                          '\033[1:30:42mDigite o número escolhido:\033[m '))
if escolhaHumano == (0 or 1 or 2):
    sleep(0.5)
    print('Escolheu?! Beleza!')
    sleep(0.5)
    print('...')
    sleep(0.5)
    print('Agora é a minha vez...')
    sleep(0.5)
    print('...')
    sleep(0.5)
    print('JO')
    sleep(0.5)
    print('KEN')
    sleep(0.5)
    print('PO!')
    sleep(0.5)
    escolhaPc = random.randint(0, 2)
    print('=-' * 20)
    print('Você escolheu {}'.format(itens[escolhaHumano]))
    print('O computador escolheu {}'.format(itens[escolhaPc]))
    print('=-' * 20)
    if escolhaPc == 0:  # computador jogou PEDRA
        if escolhaHumano == 0:
            print('Assim não dá! Empatamos')
        elif escolhaHumano == 1:
            print('Tudo bem, dessa vez eu perdi!')
        elif escolhaHumano == 2:
            print('Te peguei nessa! Ganhei!')
        else:
            print('Jogada inválida. Tente novamente.')
    elif escolhaPc == 1:  # computador jogou PAPEL
        if escolhaHumano == 0:
            print('Te peguei nessa! Ganhei!')
        elif escolhaHumano == 1:
            print('Assim não dá! Empatamos')
        elif escolhaHumano == 2:
            print('Tudo bem, dessa vez eu perdi!')
        else:
            print('Jogada inválida. Tente novamente.')
    elif escolhaPc == 2:  # computador jogou TESOURA
        if escolhaHumano == 0:
            print('Tudo bem, dessa vez eu perdi!')
        elif escolhaHumano == 1:
            print('Te peguei nessa! Ganhei!')
        elif escolhaHumano == 2:
            print('Assim não dá! Empatamos')
        else:
            print('Jogada inválida. Tente novamente.')
else:
    print('Jogada inválida. Tente novamente.')