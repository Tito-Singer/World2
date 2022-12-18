import random
from time import sleep

print('\033[1:30:43mBem-vindo ao jogo de Jokenpô\033[m\n')
sleep(0.5)
escolhaHumano = int(input('\033[1:30:42mPara jogar comigo, escolha uma das opções abaixo:\033[m\n'
                          '1 - Pedra\n'
                          '2 - Papel\n'
                          '3 - Tesoura\n'
                          '\033[1:30:42mDigite o número escolhido:\033[m '))
sleep(0.5)
print('Escolheu?! Beleza! Agora é a minha vez...')
sleep(0.5)
print('...')
sleep(0.5)
print('Deixa eu pensar mais um pouco...')
sleep(0.5)
print('...')
sleep(0.5)
print('Pronto! Escolhi!')
sleep(1)
escolhaPc = random.randint(1, 3)
if escolhaHumano == 1 and escolhaPc == 3:
    print('Você escolheu Pedra e eu escolhi Tesoura!\n'
          'Tudo bem, dessa vez eu perdi!\n'
          'Vamos de novo!?')
elif escolhaHumano == 3 and escolhaPc == 1:
    print('Você escolheu Tesoura e eu escolhi Pedra!\n'
          'Te peguei nessa! Ganhei!\n'
          'Vamos de novo!?')
elif escolhaHumano == 2 and escolhaPc == 1:
    print('Você escolheu Papel e eu escolhi Pedra!\n'
          'Tudo bem, dessa vez eu perdi!\n'
          'Vamos de novo!?')
elif escolhaHumano == 1 and escolhaPc == 2:
    print('Você escolheu Pedra e eu escolhi Papel!\n'
          'Te peguei nessa! Ganhei!\n'
          'Vamos de novo!?')
elif escolhaHumano == 3 and escolhaPc == 2:
    print('Você escolheu Tesoura e eu escolhi Papel!\n'
          'Tudo bem, dessa vez eu perdi!\n'
          'Vamos de novo!?')
elif escolhaHumano == 2 and escolhaPc == 3:
    print('Você escolheu Papel e eu escolhi Tesoura!\n'
          'Te peguei nessa! Ganhei!\n'
          'Vamos de novo!?')
elif escolhaHumano == 1 and escolhaPc == 1:
    print('Você escolheu Pedra e eu escolhi Pedra!\n'
          'Assim não dá! Empatamos!\n'
          'Vamos de novo!?')
elif escolhaHumano == 2 and escolhaPc == 2:
    print('Você escolheu Papel e eu escolhi Papel!\n'
          'Assim não dá! Empatamos!\n'
          'Vamos de novo!?')
elif escolhaHumano == 3 and escolhaPc == 3:
    print('Você escolheu Tesoura e eu escolhi Tesoura!\n'
          'Assim não dá! Empatamos!\n'
          'Vamos de novo!?')
