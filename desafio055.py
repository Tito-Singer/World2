maiorp = 0
menorp = 0
for p in range(1, 6):
    peso = float(input('Peso da {}ª pessoa: '.format(p)))
    if p == 1:
        maiorp = peso
        menorp = peso
    else:
        if peso > maiorp:
            maiorp = peso
        elif peso < menorp:
            menorp = peso
print('O maior peso lido foi de {} Kg.'.format(maiorp))
print('O menor peso lido foi de {}'.format(menorp))