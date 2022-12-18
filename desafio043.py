from time import sleep
print('\033[1:34mBem-vindo à Calculadora de IMC\033[m\n'
      'Preencha abaixo para saber seu status:')
peso = float(input('\033[1:33mDigite seu peso atual:\033[m\n'))
altura = float(input('\033[1:33mDigite sua altura:\033[m\n'
                     '(Em Metros. Ex: 1.69)\n'))
imc = peso / (altura ** 2)
print('Aguarde enquanto calculamos seu IMC')
sleep(0.5)
print('...')
sleep(1)
if imc < 18.5:
    print('Seu IMC é {:.2f}: Abaixo do peso.'.format(imc))
elif 18.5 <= imc < 25:
    print('Seu IMC é {:.2f}: Peso ideal.'.format(imc))
elif 25 <= imc < 30:
    print('Seu IMC é {:.2f}: Sobrepeso.'.format(imc))
elif 30 <= imc <= 40:
    print('Seu IMC é {:.2f}: Obesidade.'.format(imc))
else:
    print('Seu IMC é {:.2f}: Obesidade Mórbida.'.format(imc))
