print("Lista 1 de Python")


print("Exercício 1")


v1 = int(input("Insira um valor: "))
v2 = int(input("Insira outro valor: "))
print("Esses valores somados são igual a:", v1+v2)




print("Exercício 2")


v1 = float(input("Um valor pra converter: "))
print(v1*1000)




print("Exercício 3")


vDias = int(input("Digite uma quantidade de dias: "))
vHors = int(input("Digite uma quantidade de horas: "))
vMins = int(input("Digie uma quantidade de minutos:"))
vSegs = int(input("Digite uma quantidade de segundos: "))

vTSeg = (vDias*86400) + (vHors*3600) + (vMins*60) + vSegs

print("Isso equivale á ", vTSeg, " segundos")

 


print("Exercício 4")


vSal = float(input("Informe seu salário atual: R$"))
vAum = float(input("Informe a porcentagem(%) de aumento: "))

vNSa = vSal + (vSal*(vAum/100))

print("Seu novo salário será de: R$", vNSa)




print("Exercício 5")


vPdt = float(input("Qual seria o valor do produto?: "))
vDes = float(input("E o valor do cupom de desconto?: "))

vNPd = vPdt - (vPdt*(vDes/100))

print("seu produto vai sair por: R$", vNPd)




print("Exercício 6")


vDist = float(input("Qual a distância(km) da sua viagem?: "))
vVelo = float(input("Qual vai ser a velocidade média(km/h) do carro?: "))

vTemp = vDist/vVelo

print("O tempo estimado da viagem é de: ", vTemp, " horas")




print("Exercício 7")


vCel = float(input("Digituma temperatura em celsius para converter em Fahrenheit: "))

vFah = 9*vCel/5 + 32

print("isso dá ", vFah, "º fahrenheint")




print("Exercício 8")


vFah = float(input("Digituma temperatura em fahrenheint para converter em Celsius: "))

vCel = (vFah - 32)*5/9

print("isso dá ", vCel, "º Celsius")




print("Exercício 9")


vKms = int(input("Quantos km você percorreu?: "))
vDia =  int(input("e por quantos dias alugou o carro?: "))

vPrc = (vDia*60) + (vKms*0.15)

print("Sua conta fica no valor de: R$", vPrc)




print("Exercício 10")


vQCig = int(input("Quantos cigarros vc fuma por dia?: "))
vAnos = int(input("Há quantos anos fuma?: "))

vDias = (((vAnos*365)*vQCig)*10)/1440

print("Você perdeu ", vDias, " dias de vida")



print("Exercício 11")


print(len(str(2**10000)))



