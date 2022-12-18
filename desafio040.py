from time import sleep
print('\033[1:33mBem-vindo à calculadora de média escolar!\033[m\n'
      'Para começarmos, preencha o que for solicitado abaixo:')
sleep(1)
nota1 = float(input('\033[1:34mDigite aqui sua nota da AV1:\033[m\n'))
sleep(0.5)
nota2 = float(input('\033[1:34mDigite aqui sua nota da AV2:\033[m\n'))
mediaNOTAS = (nota1 + nota2)/2
print('Por favor aguarde enquanto calculamos sua média\n'
      '(...)')
sleep(2)
if mediaNOTAS <= 5:
    print('Sentimos muito. Você foi Reprovado com a média {:.2f}.'.format(mediaNOTAS))
elif 5 >= mediaNOTAS >= 6.9:
    print('Você está em Recuperação com a média {:.2f}.\n'
          'Se dedique para não perder o ano letivo.'.format(mediaNOTAS))
elif mediaNOTAS >= 7:
    print('\033[1:33mParabéns! Você foi Aprovado com a média {:.2f}!\033[m'.format(mediaNOTAS))