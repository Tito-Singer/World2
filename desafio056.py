somaidade = 0
médiaidade = 0
maiorIdadeHomem = 0
nomeVelho = ''
totMulher20 = 0
for p in range(1, 5):
    print('------- {}ª PESSOA -------'.format(p))
    nome = str(input('Nome: ')).strip()
    idade = int(input('Idade: '))
    sexo = str(input('Sexo [M/F]: '))
    somaidade += idade
    if p == 1 and sexo in 'Mm':
        maiorIdadeHomem = idade
        nomeVelho = nome
    if sexo in 'Mm' and idade > maiorIdadeHomem:
        maiorIdadeHomem = idade
        nomeVelho = nome
    if sexo in 'Ff' and idade < 20:
            totMulher20 += 1

médiaidade = somaidade / p
print('A média de idade do grupo é de {} anos'.format(médiaidade))
print('O homem mais velho tem {} anos e se chama {}.'.format(maiorIdadeHomem, nomeVelho))
print('Ao todo, são {} mulheres com menos de 20 anos.'.format(totMulher20))