from time import sleep
n = int(input('Digite um número:\n'))
sleep(0.5)
base = int(input('Agora escolha a base de conversão: \n'
      '\033[1:33mDigite o número correspondente à base\033[m \n'
      '1 - Binário\n'
      '2 - Octal\n'
      '3 - Hexadecimal\n'
     '\033[1:33mDigite sua opção:\033[m  '))
if base == 1:
    print(bin(n)[2:])
elif base == 2:
    print(oct(n)[2:])
elif base == 3:
    print(hex(n)[2:])
else:
    print('Este valor não consta no menu.')