import datetime
print('Para calcularmos a possibilidade de alistamento, por favor, preencha os campos abaixo:')
diaIDADE = int(input('Digite o dia de seu nascimento:\n'))
mesIDADE = int(input('Digite o mês de seu nascimento:\n'))
anoNasc = int(input('Digite o ano de seu nascimento:\n'))
anoVIGENTE = int(datetime.date.today().year)
#mesagora = (int(str(datetime.date.today()).split('-')[1]))
#diaagora = (int(str(datetime.date.today()).split('-')[2]))
idade = anoVIGENTE - anoNasc
print('Você nasceu em {} do {} de {} e está com {} anos'.format(diaIDADE, mesIDADE, anoNasc, idade))
alist = str(input('Se alistou?\n (Digite S ou N)\n'))
if idade > 18 and alist.upper() == 'S':
    print('Parabéns por ter se alistado no tempo correto!')
elif idade > 18 and alist.upper() == 'N':
    print('Você deveria ter se alistado em {:.0f}'.format(anoNasc + 17))
elif idade < 18:
    print('Você deve procurar a junta para se alistar em {:.0f}'.format(anoNasc + 17))
elif idade == 18:
    print('\033[1:33mVocê deve procurar a junta para se alistar ainda em {}!\033[m\n'
          '\033[1:34mCuidado para não perder o prazo!\033[m'.format(anoVIGENTE))




#print(str(datetime.date.today()).split('-'))
#print(int(str(datetime.date.today()).split('-')[0]))
#print(int(datetime.date.today()).split)
