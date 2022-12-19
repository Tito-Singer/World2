print('Bem-vindo ao programa de soma de numeros pares.\n'
      'Qualquer número ímpar será desconsiderado.')
s = 0
cont = 0
for c in range(0, 6):
    n = int(input('Digite um número:\n'))
    if n % 2 == 0:
        s += n
        cont += 1
print('Você informou {} números pares e sua soma foi {}'.format(cont, s))