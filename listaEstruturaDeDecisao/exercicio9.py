#Faça um Programa que leia três números e mostre-os em ordem decrescente.
primeiro = int(input('Primeiro numero: '))
segundo  = int(input('Segundo numero : '))
terceiro = int(input('Terceiro numero: '))

if (primeiro>segundo>terceiro):
    print(primeiro,segundo,terceiro)

if (primeiro>terceiro>segundo):
    print(primeiro,terceiro,segundo)

if(segundo>primeiro>terceiro):
    print(segundo>primeiro>terceiro)

if(segundo>terceiro>primeiro):
    print(segundo>terceiro>primeiro)

if(terceiro>segundo>primeiro):
    print(terceiro>segundo>primeiro)

if(terceiro>primeiro>segundo):
    print(terceiro>primeiro>segundo)

if (primeiro==segundo or primeiro==terceiro or segundo==terceiro):
    print("Inválido!")
