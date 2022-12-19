print('Este é um programa para calcular a soma entre todos\nos números ímpares, múltiplos de 3 e entre 1-500:')
s = 0
cont = 0
for c in range(1, 501, 2):
    if c % 3 == 0:
        cont = cont + 1
        s += c
print('A soma dos {} valores solicitados é {}'.format(cont, s))
    #print(s)