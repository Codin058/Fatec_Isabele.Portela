print("Lista 2 de Python")




print("Exercício 1")


a = int(input("Informe o 1º lado do triangulo: "))
b = int(input("Informe o 2º lado do triangulo: "))
c = int(input("Informe o 3º lado do triangulo: "))

if a+b > c and b+c > a and a+c > b:
    
    print("É um triângulo!")

    if a != b and b != c and a != c:

        print("Tipo: escaleno")

    if (a == b and a != c) or (a == c and a != b) or (b == c and b != a):

        print("Tipo: isoceles")

    if a == b and a == c:

        print("Tipo: equilátero")
                                                    
else:
    
    print("Esses valores não formam um triângulo")




print("Exercício 2")


ano = int(input("Que ano você quer saber se é bissexto?: "))

if (ano % 4 == 0 and ano % 100 != 0) or (ano % 400 == 0):

    print("É um ano bissexto!!!")

else:

    print("Não é um ano bissexto :(")




print("Exercício 3")


kgPeixe = float(input("Quilo de peixes pescados: "))

if kgPeixe > 50:

    excesso = kgPeixe - 50
    multa = excesso*4

    print("Pegou peixes de mais!")

else:

    excesso = 0
    multa = 0

    print("Não excedeu na quantidade de peixes")

print("Excesso: ", excesso, "kg")
print("Valor da Multa: R$", multa)




print("Exercício 4")


n1 = float(input("Informe 1 número: "))
n2 = float(input("Informe outro números: "))
n3 = float(input("Informe só mais um: "))

if n1 == n2 and n1 == n3:
    
    print("Todos são iguais")
    
elif n1 >= n2 and n1 >= n3:

    print(n1, " é o maior deles")

elif n2 >= n3:

    print(n2, " é o maior deles")

else:

    print(n3, " é o maior deles")




print("Exercício 5")


n1 = float(input("Informe 1 número: "))
n2 = float(input("Informe outro números: "))
n3 = float(input("Informe só mais um: "))

if n1 == n2 and n1 == n3:
    
    print("Todos são iguais")

else:
    
    if n1 >= n2 and n1 >= n3:

        print(n1, " é o maior deles")

    elif n2 >= n3:

        print(n2, " é o maior deles")

    else:

        print(n3, " é o maior deles")

    if n1 <= n2 and n1 <= n3:

        print(n1, " é o menor deles")

    elif n2 <= n3:

        print(n2, " é o menor deles")

    else:

        print(n3, " é o menor deles")




print("Exercício 6")


porHora = float(input("Quanto você ganha por hora?: "))
hTrabalhada = int(input("Quantas horas você trabalhou esse mês?: "))

saBruto = porHora*hTrabalhada

descIR = saBruto*0.11
descINSS = saBruto*0.08
descSind = saBruto*0.05

saLiquido = saBruto - descIR - descINSS - descSind

print("+ Salário Bruto: R$", saBruto)
print("- IR (11%): R$", descIR)
print("- INSS (8%): R$", descINSS)
print("- Sindicato (5%): R$", descSind)
print("= Salário Líquido: R$", saLiquido)




print("Exercício 7")


area = float(input("Qual a área que vc vai pinta (m²)?: "))

if (area/3) % 18 != 0:

    nLatas = (area/3)/18 + 1

else:

    nLatas = (area/3)/18

valor = nLatas*80

print("Nº de latas necessárias: ", nLatas)
print("Preço total: R$80,00 x ", nLatas, " === R$", valor)