i = 1
maior = 0
#Usado para repetir pedindo as notas
while (i<=5) :
    nota = float(input("Digite a nota", i))
    #Comparação dos numeros, entre o menor e maior
    if(nota > maior):
        maior = nota
    i+=1
    print(maior)
