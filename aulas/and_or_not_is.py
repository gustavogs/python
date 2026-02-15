"""
Estruturas logicas

AND, OR, NOT, IS

Operadores unarios
NOT

Operadores binarios
AND, OR, IS
"""
ativo = True
logado = False

if ativo and logado:
    print('Bem vindo usuario')
else:
    print('É necessario ativar sua conta')

contrario = not False
print(contrario)

print(ativo is False)
