#Faça um programa que o usuário digite diversos números positivos. Quando o usuário digita um número negativo, o programa termina.
numeroA=int(input("Digite um número: "))

while (numeroA >0):
    numeroA=int(input("Digite um número: "))

#Faça um programa em que um usuário informa a quantidade de alunos que terão suas médias calculadas. Em seguida, calcula-se todas as médias
# quantidadeAlunos=int(input("Digite a quantidade de alunos: ",))
i=1
while(i<=quantidadeAlunos):
    nota1=float(input("Digite a primeira nota: "))
    nota2=float(input("Digite a segunda nota: "))
    somaNotas=nota1+nota2
    mediaAlunos=somaNotas/2
    print(mediaAlunos)
    i+=1

#Faça um programa que verifique o login e a senha informados pelo usuário.
#Enquanto o usuário e senha não for admin e admin, o algoritmo deve apresentar a mensagem "Login ou senha incorretos"
login = input("Digite o login: ")
senha = input("Digite a senha: ")

while(login!="admin" or senha !="admin"):
    print("Login ou senha incorretos")
    break
else:
    print("Login efetuado com sucesso!")


