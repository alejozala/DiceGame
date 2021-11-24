from Random_Numbers import random_numbers
import time

def game(jogadas,nDados,soma1,soma2):

    fim = False
    contador = 0
    

    while not fim:
        somaT = 0
        contador += 1
        print("JOGADA",contador,":")
        numeros = random_numbers(nDados)
        for i in range(len(numeros)):
            print("Face",i+1,":",numeros[i])
            somaT = numeros[i] + somaT

        print("Jogada atual:", somaT,"\n\n")
        time.sleep(2)

        if somaT == soma1 or somaT == soma2:
            print("Você ganhou!!!")
            fim = True
        elif contador >= jogadas:
            print("Você perdeu")
            fim = True



