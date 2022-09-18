# Faça um programa que pergunte o preço de três produtos e informe qual produto você deve comprar, sabendo que a decisão é sempre pelo mais barato.
precoA=float(input("Digite o primeiro preço: "))
precoB=float(input("Digite o segundo preço: "))
precoC=float(input("Digite o terceiro preço: "))

if (precoA < precoB and precoA<precoC):
    print(f"O menor número é {precoA}")
elif(precoB< precoA and precoB <precoC):
    print(f"O menor número é {precoB}")
else:
    print(f"O menor número é {precoC}")