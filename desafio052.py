print('Bem-vindo ao validador de números primos.')
print('=-' * 20)
tot = 0
n = int(input('Digite o número que deseja verificar:\n'))
for c in range(1, n + 1):
    if n % c == 0:
        print('\033[33m', end='')
        tot += 1
    else:
        print('\033[31m', end='')
    print('{}'.format(c), end='')
if tot <= 2:
    print('\n\033[mO número {} É primo!\n'
          'Foi divisível {} vezes.'.format(n, tot))
else:
    print('\n\033[mO número {} NÃO é primo!\n'
          'Foi divisível {} vezes.'.format(n, tot))
