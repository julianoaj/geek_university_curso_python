"""
Entendendo o *args

- O *args é um parâmetro como outro qualquer. Isso significa que você podera chamar de qualquer coisa, desde que comece
com * (asterisco)

Exemplo:
*xis

Mas por convenção, utilizamos o *args para defini-lo

O que é o *args

O parâmetro *args utilizado em uma função, coloca os valores extras informados como entrada em uma tupla. Então desde ja
lembre-se que tuplas são imutaveis
///////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
                                          =-=-=-=-=-=-=-=-=-=-=-=-=-=-=

# Exemplo
def soma_todos_numeros(num1=1, num2=2, num3=3, num4=4):
    return num1 + num2 + num3


print(soma_todos_numeros(4, 6, 9))
print(soma_todos_numeros(4, 6))
print(soma_todos_numeros(4, 6, 9, 10))
///////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
                                          =-=-=-=-=-=-=-=-=-=-=-=-=-=-=
# Entendendo o *args


def soma_todos_numeros(nome, sobrenome, *args):
    return sum(args)


print(soma_todos_numeros('Angelina', 'Jolie'))
print(soma_todos_numeros('Angelina', 'Jolie', 1))
print(soma_todos_numeros('Angelina', 'Jolie', 1, 2))
print(soma_todos_numeros('Angelina', 'Jolie', 1, 2, 3))
print(soma_todos_numeros('Angelina', 'Jolie', 1, 2, 3, 4))


///////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
                                          =-=-=-=-=-=-=-=-=-=-=-=-=-=-=
# Outro exemplo de utilização de *args


def verifica_info(*args):
    if 'Geek' in args and 'University' in args:
        return 'Bem Vindo Geek'
    return 'Eu não tenho certeza de quem você é'


print(verifica_info())
print(verifica_info(1, True, 'University', 'Geek'))
print(verifica_info(1, 'University', 3.145))
///////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
                                          =-=-=-=-=-=-=-=-=-=-=-=-=-=-=
///////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
                                          =-=-=-=-=-=-=-=-=-=-=-=-=-=-=
///////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
                                          =-=-=-=-=-=-=-=-=-=-=-=-=-=-=

"""

def soma_todos_numeros(*args):
    return sum(args)


# print(soma_todos_numeros())
# print(soma_todos_numeros(3, 4, 5, 6))
lista = [1, 2, 3, 4, 5]

# Desempacotador
print(soma_todos_numeros(*lista))

# OBS: O *(asterisco) serve para que informemos ao Python que estamos passando como argumento uma coleção de dados.
# Desta forma ele saberá quer precisará desempacotar os dados
