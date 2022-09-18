#Faça um Programa que leia três números e mostre o maior e o menor deles.
primeiro = int(input('Primeiro numero: '))
segundo  = int(input('Segundo numero : '))
terceiro = int(input('Terceiro numero: '))

maior = primeiro
if (segundo > maior):
        maior = segundo

if (terceiro > maior):
        maior = terceiro
print('Maior: ',maior)

menor=primeiro
if(segundo<primeiro):
    menor=segundo

if(terceiro<menor):
    menor=terceiro
print("Menor: ", menor)