from time import sleep
print('\033[1:33mBem-vindo ao sistema de aprovação de empréstimo. \nPara começarmos, preencha os campos abaixo:\033[m')
vcasa = float(input('Qual o valor da casa?\n'))
sleep(1)
s = float(input('Qual o salário do comprador?\n'))
sleep(1)
t = float(input('Em quantos anos será quitado o pagamento?\n'))
vmen = (vcasa / (t * 12))
if vmen <= (s * 0.3):
    print('Parabéns, seu empréstimo foi aprovado. \nO valor para pagamento mensal é R$ {:.2f}/mês, durante {:.0f} meses.'.format(vmen , (t * 12)))
else:
    print('Infelizmente seu empréstimo foi negado.')
