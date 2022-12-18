from datetime import date
print('\033[1:34mBem-vindo ao Gererenciador de Categorias\n'
      'da Confederação Nacional de Natação\033[m\n'
      'Se quiser saber em qual categoria\n'
      'você se enquadra preencha abaixo:\n')
anoNascimento = int(input('Digite seu ano de nascimento (Ex:1990):\n'))
anoVigente = int(datetime.date.today().year)
idade = (anoVigente - anoNascimento)
if idade <= 9:
    print('\033[1:34mVocê tem {} anos e foi classificado na categoria:\033[m\n'
          'Mirim'.format(idade))
elif 9 < idade <=14:
    print('\033[1:34mVocê tem {} anos e foi classificado na categoria:\033[m\n'
          'Infantil'.format(idade))
elif 14 < idade <=19:
    print('\033[1:34mVocê tem {} anos e foi classificado na categoria:\033[m\n'
          'Junior'.format(idade))
elif 19 < idade <=20:
    print('\033[1:34mVocê tem {} anos e foi classificado na categoria:\033[m\n'
          'Sênior'.format(idade))
else:
    print('\033[1:34mVocê tem {} anos e foi classificado na categoria:\033[m\n'
          'Master'.format(idade))