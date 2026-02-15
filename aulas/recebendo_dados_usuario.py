"""
Recebendo dados do usuario
"""

# Entrada de dados
print("Qual seu nome?")
nome = input()
print("Qual sua idade?")
idade = input()

"""Atenção, todo dado recebido via input() é do tipo String"""

# Processamento

# Saida de dados
# print('Seja bem vindo(a) %s', % nome), versão 2.x
# print('Seja bem vindo(a) {0}', .format(nome)), versão 3.x
print(f'Seja bem vindo(a) {nome} \nSua idade é: {idade}')  # Versão atual
# nome = input('Qual seu nome?') versão simplificada
# idade = input('Qual sua idade?') versão simplificada
