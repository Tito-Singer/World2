print('Bem-vindo ao programa que mostra a tabuada do número digitado!')
print('=-' * 32)
n = int(input('Digite o número que deseja conhecer a tabuada:\n'
              'Número: '))
for c in range(1, 11):
        print('{} x {} = {}'.format(n, c, (n * c)))
