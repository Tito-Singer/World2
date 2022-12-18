print('\033[1:34mBem-vindo à calculadora dos triângulos possíveis\033[m\n'
      'Para avaliar se um triângulo é possível e a qual tipo pertence\n'
      'preencha abaixo:')
reta1 = float(input('Insira o valor do comprimento da reta 1:\n'))
reta2 = float(input('Insira o valor do comprimento da reta 2:\n'))
reta3 = float(input('Insira o valor do comprimento da reta 3:\n'))
retasOrganizadas = (sorted((reta1, reta2, reta3)))
if (retasOrganizadas[0] + retasOrganizadas[1]) >= retasOrganizadas[2]:
    print('Este é um triângulo possível e')
    if reta1 == reta2 == reta3:
        print('pertence ao tipo Equilátero')
    elif (reta1 == reta2 != reta3) or (reta1 != reta2 == reta3) or (reta1 == reta3 != reta2):
        print('pertence ao tipo Isósceles')
    elif reta1 != reta2 != reta3 != reta1:
        print('pertence ao tipo Escaleno')
else:
    print('Infelizmente não é possível formar um triângulo com estes segmentos de reta.')
