# Desenvolver calculadora em Python com as seguintes funçôes:
# a)Soma; b)Subtracao c)Multiplicacao d)Divisao

a = int(input("Digite o primeiro número: "))
b = int(input("Digite o segundo número: "))


def soma (a,b):
    return a +b

def subtracao(a,b):
    return a-b

def multiplicacao(a,b):
    return a*b

def divisao(a,b):
    return a/b

print("A soma entre a e b é: ",soma(a,b))
print("A diferença entre a e b é: ",subtracao(a,b))
print("A multiplicação de a e b é: ",multiplicacao(a,b))
print("A divisão dos dois números é: ", divisao(a,b))

