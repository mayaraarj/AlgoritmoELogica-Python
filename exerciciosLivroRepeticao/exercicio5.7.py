# Modifique o programa anterior de forma que o usuário também
# digite o início e o fim da tabuada, em vez de começar com 1 e 10.

n=int(input("Tabuada de: "))
i=int(input("Digite o início da tabuada: "))
f=int(input("Digite o fim da tabuada: "))
x=i

while x<=f:
    print(f"{i} * {f} = {n*x}")
    x = x+1
