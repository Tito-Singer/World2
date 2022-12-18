n1 = int(input('Insira o primeiro número:\n'))
n2 = int(input('Insira o segundo número:\n'))
if n1 > n2:
    print('O primeiro valor é maior.')
elif n2 > n1:
    print('O segundo valor é maior')
else:
    print('Não existe valor maior, os dois são iguais.')