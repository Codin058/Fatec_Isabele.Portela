print("Lista 3 Desafio")


print("Exercício 1")


num = int(input("Digite um número natural para descobri se ele é triangular: "))

while num < 0:
    num = int(input("Digite um número natural para descobri se ele é triangular: "))

d = 3

while d*(d-1)*(d-2) < num:
    d = d + 1

if d*(d-1)*(d-2) == num:
    print(f"Esse número é triângular. Números consecutivos: {d-2}.{d-1}.{d}") 
else:
    print("Esse número não é triangular")




print("Exercício 2")


conta = int(input("Valor da conta: "))
pagamento = int(input("Seu pagamento: "))

troco = pagamento - conta

c50 = c20 = c10 = c5 = c2 = c1 = 0

while troco < 0:
     pagamento = int(input("Você pagou a menos, pague de  novo: ")) 
     troco = pagamento - conta

if troco >= 1:
    if troco >= 50:
        c50 = troco // 50
        troco = troco - (50*c50)
    if troco >= 20:
        c20 = troco // 20
        troco = troco - (20*c20)
    if troco >= 10:
        c10 = troco // 10
        troco = troco - (10*c10)
    if troco >= 5:
        c5 = troco // 5
        troco = troco - (5*c5)
    if troco >= 2:
        c2 = troco // 2
        troco = troco - (2*c2)
    if troco >= 1:
        c1 = troco // 1
        troco = troco - (1*c1)

    print("Troco total: ", pagamento - conta)
    print(f"50x{c50}, 20x{c20}, 10x{c10}, 5x{c5}, 2x{c2}, 1x{c1}")

else:
    print("Sem troco")




print("Exercício 3")


num = int(input("Digite um número para descobrir se ele é primo: "))

while num < 2:
    print("Este número não pode ser primo, pq os primos começam no 2.")
    num = int(input("Digite um positivo: "))

d = 2
ehPrimo = True

while d < num:
    if num % d == 0:
        ehPrimo = False
        break
    else:
        d = d + 1

if ehPrimo == True:
    print(f"{num} é um número primo")

else:
    print(f"{num} não é um número primo")




print("Exercício 4")


num = int(input("Digite um número para fatorar: "))

nPrimos = []
d = 2

while num < 2:
    num = int(input("Esse número não é possível fatorar. Digite um número para fatorar: "))

n = num

while num > 1:
    if num % d == 0:
        nPrimos.append(d)
        num = num // d
    else:
        d = d + 1

print("Fatoração: ", n," = ", nPrimos)      




print("Exercício 5")


num = int(input("Digite um número: "))

print("Ele invertido é assim: ", str(num)[::-1])