#Faça um programa que peça dois números e imprima a soma.
numero01 = int(input())
numero02 = int(input())

soma = numero01+ numero02
print(soma)

#Faça um programa que peça as 4 notas bimestrais e mostre a média
nota1=float(input())
nota2=float(input())
nota3=float(input())
nota4=float(input())

media=(nota1+nota2+nota3+nota4)/4
print(media)

#Faça um programa que converta de metros para centímetros
tamanhoMentro=float(input())
tamanhoCentimetro=tamanhoMentro*100
print(tamanhoCentimetro)

#Faça um programa que peça o raio de um cículo e calcule a área
raio=float(input())
area=3.14*raio**2
print(area)

#Faça um programa que pergunte quanto você ganha por hora e o número de horas trabalhadas por mês.Calcule e mostre o total do seu salário no referido mês.
print("Quanto você ganha por hora?")
quantiaPorHora=float(input())
print("Quantas horas você trabalha por mês?")
horasPorMes= int(input())
salario = quantiaPorHora*horasPorMes
print("Seu salário é de: "+ str(salario))