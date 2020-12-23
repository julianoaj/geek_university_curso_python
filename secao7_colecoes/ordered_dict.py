"""
Modulo Collections - Ordered Dict

https://docs.python.org/3/library/collections.html#collections.OrderedDict

Em um dicionário a ordem de inserção dos elementos não é garantida

dicionario = {'a': 1, 'b': 2, 'c': 3, 'd': 4, 'e': 5}

for chave, valor in dicionario.items():
    print(f'Chave = {chave} e valor={valor}')

OrderedDict -> É um dicionário que nos garante a ordem de inserção dos elementos

from collections import OrderedDict

dicionario = OrderedDict({'a': 1, 'b': 2, 'c': 3, 'd': 4, 'e': 5})

for chave, valor in dicionario.items():
    print(f'Chave = {chave} e valor={valor}')

"""
from collections import OrderedDict

# Entendo a diferença entre dict e OrderedDict

# Dicionários comuns
dict1 = {'a': 1, 'b': 2}
dict2 = {'b': 2, 'a': 1}
print(dict1 == dict2)  # True -> Ja que a ordem dos elementos não importa para o dicionário

# OrderedDict
odict1 = OrderedDict({'a': 1, 'b': 2})
odict2 = OrderedDict({'b': 2, 'a': 1})
print(odict1 == odict2)  # False -> Ja que a ordem dos elementos importa para OrderedDict
