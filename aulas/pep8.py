"""
PEP8 - Python Enhanced Proposals

São propostas de melhorias gerais para a linguagem

The Zen of Python:

import this
"""

"""
A ideia da PEP8 é que escrevamos codigos PYTHONICOS.

[1] - Utilize "Camel case" para nomes de clases.

[2] - Utilize nomes em minusculo, separados em underline para funções
ou variaveis.

[3] - Utilize quatro espaços para identação.

[4] - Linhas em branco
- Separa funções e difinicões de classe em duas linhas em branco
- Metodos dentro de um classe devem ser separados com uma unica linha em branco

[5] - Imports
-Imports devem sempre ser feitos em linhas separadas

[6] - Espaços em expressões e instruções

[7] - Termine sempre uma instrução com uma nova linha
"""

"""[1]


class Calculadora:
    pass


class CalculadoraCientifica:
    pass


"[2]"


def soma():
    pass


def soma_dois():
    pass


numero = 2
numero_impar = 3

"[3]"

if 'a' in 'banana':
    print('tem')


"[5]"

import sys
import os

# Não há problema em fazer:
from types import StringType, ListType

# Caso tenha muitos imports de um mesmo pacotes, recomenda-se:

from types import(
    StringType,
    ListType,
    SetType
)

"[5]"

# Não faça:

funcao( algo[ 1 ], { outro: 2} )

#Faça
funcao(algo[1], {outro: 2})

# Faça
x = 1
z = 2
variavel_longa = 3

"[7]"
import this

"""