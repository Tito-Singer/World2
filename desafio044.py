from time import sleep
print('{:=^40}'.format(' LOJAS TITO '))
print('\033[1:30:43mBem-vindo à calculadora de descontos\033[m\n'
      '\033[1:33mPreencha os campos abaixo para saber suas condições:\033[m\n')
valorProduto = float(input('\033[1:30:45mDigite o valor de suas compras:\033[m\n'
                           'R$ '))
sleep(0.5)
formaPgto = int(input('\033[1:30:42mDigite o número correspondente\033[m\n'
                      '\033[1:30:42mà forma de pagamento:\033[m\n'
                      '1 - À vista (Dinheiro/Cheque)\n'
                      '2 - À vista (Cartão)\n'
                      '3 - Parcelado em até 2x no Cartão\n'
                      '4 - Parcelado em 3x ou mais no Cartão\n'
                      '\033[1:30:42mDigite o número:\033[m '))
if formaPgto == 1:
    print('A forma de pagamento escolhida foi:\n'
          '\033[1:30:43m1 - À vista (Dinheiro/Cheque)\033[m\n'
          'sua compra custou {} e o valor a ser pago é:\n'
          '\033[1:30:43mR$ {:.2f}.\033[m'.format(valorProduto, valorProduto*0.9))
elif formaPgto == 2:
    print('A forma de pagamento escolhida foi:\n'
          '\033[1:30:43m2 - À vista (Cartão)\033[m\n'
          'sua compra custou {} e o valor a ser pago é:\n'
          '\033[1:30:43mR$ {:.2f}.\033[m'.format(valorProduto, valorProduto*0.95))
elif formaPgto == 3:
    print('A forma de pagamento escolhida foi:\n'
          '\033[1:30:43m3 - Parcelado em até 2x no Cartão\033[m\n'
          'sua compra custou {} e o valor a ser pago é:\n'
          '\033[1:30:43m 2 x R${:.2f}.\033[m'.format(valorProduto, (valorProduto/2)))
elif formaPgto == 4:
    print('A forma de pagamento escolhida foi:\n'
          '\033[1:30:43m4 - Parcelado em 3x ou mais no Cartão\033[m\n'
          'sua compra custou {} e o valor a ser pago é:\n'
          '\033[1:30:43mR$ 3 x R${:.2f}.\033[m'.format(valorProduto, (valorProduto*1.2/3)))
else:
    print('Forma de pagamento não reconhecida.')