"""
for item in iteravel:
    //execução do loop

Utilizamos loops para iterara sobre sequencias ou sobre valores iteraveis    

Exemplo de iteraveis

- String
    nome = 'Teste'
- Lista
    lista = [1, 2, 3, 4, 5]
- Range
    numeros = range(1, 10)
"""

nome = 'Teste Iteravel'
lista = [1, 2, 3, 4, 5]
numeros = range(1, 10)

for letra in nome:
    print(letra)

for numero in lista:
    print(numero)

for numero in numeros:
    print(numero)

for v, l in enumerate(nome):
    print(v, l)

for valor in enumerate(nome):
    print(valor)


qtd = int(input('Quantas vezes esse loop deve rodar'))

for n in range(1, qtd+1):
    print('Imprimindo ', n)

for letra in nome:
    print(letra, end='')
