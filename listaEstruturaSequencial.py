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

#15 Faça um Programa que pergunte quanto você ganha por hora e o número de horas trabalhadas no mês. Calcule e mostre o total do seu salário no referido mês, sabendo-se que são descontados
#  11% para o Imposto de Renda,
# 8% para o INSS e 5% para o sindicato,
#  faça um programa que nos dê:
# a)salário bruto.
print("Quanto você ganha por hora?")
valorHora=float(input())
print("Quantas horas você trabalhou esse mês?")
horasTrabalhadas=int(input())
salarioBruto=valorHora*horasTrabalhadas
print("Seu salário bruto é de R$ "+ str(salarioBruto)+ " reais.")
# b)quanto pagou ao INSS.
quantiaINSS=0.08*salarioBruto
print("A quantia devida ao INSS é de R$ "+str(quantiaINSS)+ " reais")
# c)quanto pagou ao sindicato.
quantiaSindicato=salarioBruto*0.05
print("A quantia devida ao sindicato é de R$ "+ str(quantiaSindicato)+ " reais")
# d)o salário líquido.Obs.: Salário Bruto - Descontos = Salário Líquido
quantiaIR=0.11*salarioBruto
# print("A quantia devida ao Imposto de Renda é de R$ "+ str(quantiaIR)+ " reais")

# salarioLiquido=salarioBruto-quantiaINSS-quantiaSindicato-quantiaIR
print("Seu salário líquido é de R$ "+str(salarioLiquido)+" reais.")

# 16 Faça um programa para uma loja de tintas. O programa deverá pedir o tamanho em metros quadrados da área a ser pintada. 
# Considere que a cobertura da tinta é de 1 litro para cada 3 metros quadrados e que a tinta é vendida em latas de 18 litros, 
# que custam R$ 80,00.
#  Informe ao usuário a quantidades de latas de tinta a serem compradas e o preço total.
import math
print("Informe em metros quadrados o tamanho da área a ser pintada ")
areaPintada=float(input())
quantidadeTintaNecessaria=areaPintada/3
quantidadeLatas= math.ceil(areaPintada/3)
valor=quantidadeLatas*80
print("Para cobrir "+ str(areaPintada)+" metros quadrados você precisará de "+ str(quantidadeLatas)+" latas. Isso custará "+ str(valor)+ " reais.")

#17 Faça um Programa para uma loja de tintas. O programa deverá pedir o tamanho em metros quadrados da área a ser pintada. 
# Considere que a cobertura da tinta é de 1 litro para cada 6 metros quadrados e que a tinta é vendida em latas de 18 litros,
# que custam R$ 80,00 ou em galões de 3,6 litros, que custam R$ 25,00.
# Informe ao usuário as quantidades de tinta a serem compradas e os respectivos preços em 3 situações:
# comprar apenas latas de 18 litros;
# comprar apenas galões de 3,6 litros;
# misturar latas e galões, de forma que o desperdício de tinta seja menor. Acrescente 10% de folga e sempre arredonde os valores para cima, isto é, considere latas cheias.

import math


area=int(input("Informe o tamanho em metros quadrados daárea que deseja pintar: "))

litros=(area/6)*1.1
latas=math.ceil(litros/18)
valorLata=latas*80
galao=math.ceil(litros/3.6)
valorGalao=galao*25

mixLatas=round(litros/18)
mixGaloes=round((litros-mixLatas *18)/3.6)

if((litros-(mixLatas*18)%3.6 !=0)):
    mixGaloes+=1
    totalMix=(mixLatas*80)+(mixGaloes*25)


print(f'Caso compre só latas de 18 litros, irá precisar de {latas} latas e irá custar {valorLata:.2f}')
print(f'Caso compre só galões de 3,6 litros, irá precisar de {galao} latas e irá custar {valorGalao:.2f}')
print(f'Se deseja mesclar latas e galões, serão necessárias {mixLatas} e {mixGaloes}. Iá custar {totalMix:.2f} reais')

#18 Faça um programa que peça o tamanho de um arquivo para download (em MB) e a velocidade de um link de Internet (em Mbps), 
# calcule e informe o tempo aproximado de download do arquivo usando este link (em minutos).

mb=float(input("Informe em MB o tamanho do arquivo que deseja baixar: "))
link=float(input("Informe a velocidade da internet em Mbps"))
tempo=(mb/(link/8))/60

print(f'Para efetuar um download de {mb} MB com a velocidade de {link} Mps, irá demorar {tempo:.0f} minutos')

