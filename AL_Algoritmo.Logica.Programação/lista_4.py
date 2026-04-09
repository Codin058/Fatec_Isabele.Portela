print("Lista 4")

print("Isabele Camargo Portela 1º ADS")

print("Exercício 1")

import random

lista = random.sample(range(1,101), 10)

mai = lista[0]
men = lista[0]

for c in range(10):
    if lista[c] >= mai:
        mai = lista[c]
    elif lista[c] <= men:
        men = lista [c]

print(lista)
print("Maior: ", mai)
print("Menor: ", men)


print("Exercício 2")

import random

lista = random.sample(range(1,101), 20)

lista_par = []
lista_imp = []

for c in range(20):
    if lista[c] % 2 == 0:
        lista_par.append(lista[c])
    else:
        lista_imp.append(lista[c])

print("Lista: ", lista)
print("Lista de pares: ", lista_par)
print("Lista de ímpares: ", lista_imp)


print("Exercício 3")

import random

lista_1 = random.sample(range(1,101), 10)
lista_2 = random.sample(range(1,101), 10)
lista_3 = []

for c in range(10):
    lista_3.append(lista_1[c])
    lista_3.append(lista_2[c])

print(lista_1)
print(lista_2)
print(lista_3)



print("Exercício 4")

texto = '''The Python Software Foundation and the global Python
community welcome and encourage participation by everyone. Our community is based on
mutual respect, tolerance, and encouragement, and we are working to help each other live up
to these principles. We want our community to be more diverse: whoever you are, and
whatever your background, we welcome you.'''

# tratamento do texto
texto = texto.lower()
texto = texto.replace(',', ' ')
texto = texto.replace('.', ' ')
texto = texto.replace(':', ' ')

lista = texto.split()

palavra = 'python'

def palavras(x):
    lista_pl = []

    for palavra_lista in x:
        if palavra_lista[0] in palavra or palavra_lista[-1] in palavra:
            lista_pl.append(palavra_lista)
    return lista_pl

lista_python = palavras(lista)

print(lista_python)


print("Exercício 5")

texto = '''The Python Software Foundation and the global Python
community welcome and encourage participation by everyone. Our community is based on
mutual respect, tolerance, and encouragement, and we are working to help each other live up
to these principles. We want our community to be more diverse: whoever you are, and
whatever your background, we welcome you.'''

# tratamento do texto
texto = texto.lower()
texto = texto.replace(',', ' ')
texto = texto.replace('.', ' ')
texto = texto.replace(':', ' ')

lista = texto.split()

palavra = 'python'

def contar(x):
    c = 0

    for palavra_lista in x:
        if len(palavra_lista) > 4:
            for letra in palavra_lista:
                if letra in palavra:
                    c = c + 1
    return c

contar_python = contar(lista)

print(contar_python)