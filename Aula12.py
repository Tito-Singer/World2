nome = str(input('Qual seu nome? '))
if nome.upper == 'TITO':
    print('Que nome bonito!')
elif nome.upper() == 'PEDRO' or nome.upper() == 'MARIA' or nome.upper() == 'PAULO':
    print('Seu nome é bem popular no Brasil')
elif nome.upper() in 'ANA CLAUDIA JESSICA JULIANA':
    print('Belo nome feminino')
else:
    print('Seu nome é bem normal')
print('Tenha um bom dia, {}'.format(nome))