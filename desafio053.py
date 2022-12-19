print('=-' * 30)
print('Bem-vindo ao programa para validar Palíndromos.\n'
      '(Frases que podem ser lidas igualmente de trás para frente)')
print('=-' * 30)
expressao = str(input('Digite sua palavra, frase ou expressão:\n')).strip().replace(" ", "").upper()
if expressao == (expressao[::-1]):
    print('Voce digitou {} e seu inverso é {}.\n'
          'Esta expressão é um Palíndromo!'.format(expressao, (expressao[::-1])))
else:
    print('Voce digitou {} e seu inverso é {}.\n'
          'Esta expressão não é um Palíndromo!'.format(expressao, (expressao[::-1])))