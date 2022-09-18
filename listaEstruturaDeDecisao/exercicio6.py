#Faça um Programa que leia três números e mostre o maior deles.
numeroA=float(input("Digite o primeiro número: "))
numeroB=float(input("Digite o segundo número: "))
numeroC=float(input("Digite o terceiro número: "))

if (numeroA > numeroB and numeroA>numeroC):
    print(f"O maior número é {numeroA}")
elif(numeroB> numeroA and numeroB>numeroC):
    print(f"O maio número é {numeroB}")
else:
    print(f"O maior número é {numeroC}")