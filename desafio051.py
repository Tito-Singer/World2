print('Bem-vindo ao programa que mostra os 10 primeiros termos de uma PA')
inicio = int(input('Digite o Número que deseja consultar:\n'))
r = int(input('Digite a Razão a ser consultada:\n'))
for c in range(inicio, inicio+(r * 10), r):
    print(c, end=' ➝ ')
print('Fim!')