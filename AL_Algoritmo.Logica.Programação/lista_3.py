print("Lista 3 de Python")


print("Exercício 1")


nota = float(input("De uma nota entre 0 e 10: "))

while nota < 0 or nota > 10:
    print("Valor inválido")
    nota = float(input("De uma nota entre 0 e 10: "))

print("Obrigad@ pela nota!")




print("Exercício 2")


nome = str(input("Crie um nome de usuário: "))
senha = str(input("Crie uma senha: "))

while nome == senha:
    print("O nome de usuário e a senha não podem ser iguais! Tente novamente...")
    nome = str(input("Crie um nome de usuário: "))
    senha = str(input("Crie uma senha: "))

print("Login criado com sucesso!!!")




print("Exercício 3")


a = 80000
b = 200000
anos = 0

while a < b:
    a = a + (a*0.03)
    b = b + (b*0.015)
    anos = anos + 1

print("Seriam necessários ", anos, " anos para isso")




print("Exercício 4")


num = int(input("Digite o número de uma posição na sequencia de Fibonacci: "))

x = 1
a = 0
b = 1

while x <= num:
    a, b = b, a
    nFib = a + b
    a = nFib
    x = x + 1

print("O número nesta posição é: ", nFib)




print("Exercício 5")


a = int(input("Digite um número: "))
b = int(input("Digite outro número: "))

n1 = a
n2 = b

if n2 > n1:
    n1, n2 = n2, n1

r = n1 % n2

while r != 0:
    n1, n2 = n2, r
    r = n1 % n2


if b > a:
    a, b = b, a

print(f"MDC({a}, {b}) = {n2} ")