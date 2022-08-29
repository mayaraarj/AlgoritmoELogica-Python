# 1. Escreva um programa para ler 2 valores (considere que não serão
# informados valores iguais) e escrever o maior deles

numeroA=float(input())
numeroB=float(input())

if (numeroA>numeroB):
    print(numeroA)
else:
     print(numeroB)


# 2. Escreva um programa para ler o ano de nascimento de uma pessoa e
# escrever uma mensagem que diga se ela poderá ou não votar na
# próxima eleição (não é necessário considerar o mês em que ela nasceu)

anoNascimento = int(input())

if (2022 -anoNascimento >=18):
     print("Poderá votar")
else:
 print("Não poderá votar")

# 3. Escreva um programa que verifique a validade de uma senha fornecida
# pelo usuário. A senha válida é o número 1234. Devem ser impressas as
# seguintes mensagens:
# ACESSO PERMITIDO caso a senha seja válida
# ACESSO NEGADO caso a senha seja inválida

senha = int(input())

if (senha ==1234):
     print("ACESSO PERMITIDO")
else:
     print("ACESSO NEGADO")

# As maçãs custam R$ 0,30 cada se forem compradas menos do que uma
# dúzia, e R$ 0,25 se forem compradas pelo menos doze. Escreva um
# programa que leia o número de maçãs compradas, calcule e escreva o
# valor total da compra

qtdMacas=int(input())

if(qtdMacas>=12):
     precoMaca=0.25
else:
     precoMaca=0.30

totalCompra=qtdMacas*precoMaca
print(totalCompra)


# 5. Escreva um programa para ler 3 valores inteiros (considere que não
# serão lidos valores iguais) e escrevê-los em ordem crescente
numeroA=int(input())
numeroB=int(input())
numeroC=int(input())

if(numeroA>numeroB and numeroA>numeroC):
    maiorNumero=numeroA
elif(numeroB>numeroA and numeroB>numeroC):
    maiorNumero=numeroB
else:
    maiorNumero=numeroC



# 6. Escreva um programa para ler 3 valores inteiros e escrever o maior
# deles. Considere que o usuário não informará valores iguais

numeroA=int(input())
numeroB=int(input())
numeroC=int(input())

if (numeroA >numeroB and numeroA>numeroC):
         print(numeroA)
elif(numeroB>numeroA and numeroB>numeroC):
    print(numeroB)
else:
    print(numeroC)
