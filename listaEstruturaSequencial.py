# Lista de exercícios de estrutura sequencial https://wiki.python.org.br/EstruturaSequencial

#1 Faça um Programa que mostre a mensagem "Alo mundo" na tela.
print("Alo mundo")

#2 Faça um Programa que peça um número e então mostre a mensagem O número informado foi [número].

print("Digite um número")
x=(input())
print("O número informado foi "+x)

# 3 Faça um Programa que peça dois números e imprima a soma.
print("Digite o primeiro número")
x=int(input())
print("Digite o segundo número")
y=int(input())
z=x+y
print("A soma dos números digitados é "+ str(z))

#4 Faça um Programa que peça as 4 notas bimestrais e mostre a média.
print("Digite a primeira nota")
nota1=int(input())
print("Digite a segunda nota")
nota2=int(input())
print("Digite a terceira nota")
nota3=int(input())
print("Digite a quarta nota")
nota4=int(input())

media=(nota1+nota2+nota3+nota4)/4
print("A média é "+str(media))

#5 Faça um Programa que converta metros para centímetros.
tamanhoMetro=float(input())
tamanhoCentimetro=tamanhoMetro*100
print(tamanhoCentimetro)

#6 Faça um Programa que peça o raio de um círculo, calcule e mostre sua área.
raio=float(input())
area=3.14*raio**2
print(area)

#7 Faça um Programa que calcule a área de um quadrado, em seguida mostre o dobro desta área para o usuário.
lado=float(input())
areaQuadrado=lado**2
dobroDaArea=2*areaQuadrado
print(dobroDaArea)

#8 Faça um Programa que pergunte quanto você ganha por hora e o número de horas trabalhadas no mês. Calcule e mostre o total do seu salário no referido mês.
print("Quanto você ganha por hora?")
valorHora=float(input())
print("Quantas horas foram trabalhadas no mês?")
horasTrabalhadas=int(input())
salario=valorHora*horasTrabalhadas
print(salario)

#9 Faça um Programa que peça a temperatura em graus Fahrenheit, transforme e mostre a temperatura em graus Celsius.
# C = 5 * ((F-32) / 9).

print("Digite a temperatura em graus Fahrenheit")
grausF=float(input())
grausC=5*((grausF-32)/9)
print("A temperatura em graus Celsius é "+str(grausC))

#10 Faça um Programa que peça a temperatura em graus Celsius, transforme e mostre em graus Fahrenheit.
#(0 °C × 9/5) + 32 = 32 °F

print("Digite a temperatura em Celsius")
temperaturaCelsius=float(input())
temperaturaFahrenheit=(temperaturaCelsius*(9/5))+32
print("A temperatura em Fahrenheit é "+ str(temperaturaFahrenheit))

# 11 Faça um Programa que peça 2 números inteiros e um número real. Calcule e mostre:
# a) o produto do dobro do primeiro com metade do segundo .
# b) a soma do triplo do primeiro com o terceiro.
# c) o terceiro elevado ao cubo.

print("Digite o primeiro número inteiro")
inteiro1=int(input())
print("Digite o segundo número inteiro")
inteiro2=int(input())
print("Digite um número real")
real=float(input())

a=(2*inteiro1)*(inteiro2/2)
print(a)

b=(3*inteiro1)+real
print(b)

c=real**3
print(c)

# 12 Tendo como dados de entrada a altura de uma pessoa, construa um algoritmo que calcule seu peso ideal
#  usando a seguinte fórmula: (72.7*altura) - 58

print("Digite a altura")
altura=float(input())
pesoIdeal=(72.7*altura)-58
print("O peso ideal é "+ str(pesoIdeal))

# 13 Tendo como dado de entrada a altura (h) de uma pessoa, construa um algoritmo que calcule seu peso ideal, utilizando as seguintes fórmulas:
altura=float(input())
# Para homens: (72.7*h) - 58
pesoHomem=(72.7*altura)-58
# Para mulheres: (62.1*h) - 44.7
pesoMulher=(62.1*altura)-44.7
print(pesoHomem)
print(pesoMulher)

# 14 João Papo-de-Pescador, homem de bem, comprou um microcomputador para controlar o rendimento diário de seu trabalho. 
# Toda vez que ele traz um peso de peixes maior que o estabelecido pelo regulamento de pesca do estado de São Paulo (50 quilos) 
# deve pagar uma multa de R$ 4,00 por quilo excedente. João precisa que você faça um programa que leia a variável peso (peso de peixes) 
# e calcule o excesso. Gravar na variável excesso a quantidade de quilos além do limite e na variável multa o valor da multa que João deverá pagar.
#  Imprima os dados do programa com as mensagens adequadas.

print("Digite o peso do pescado")
peso=float(input())
excesso=peso-50
print("O excesso foi de "+ str(excesso)+ " kg")
multa=4*excesso
print("A multa será de "+ str(multa)+ " reais.")