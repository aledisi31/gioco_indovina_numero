#Importa libreria random
import random

#genera un numero segreto
numero_segreto = random.randint(1, 100)
tentativo = 0

#Stampa un messaggio di benvenuto e chiedi all'utente di indovinare il numero segreto
print("Benvenuto al gioco del numero segreto!")

#Ciclo finché l'utente non indovina il numero segreto
while tentativo != numero_segreto:
    risposta = input("Indovina il numero segreto (tra 1 e 100): ")
    tentativo = int(risposta)

    if tentativo < numero_segreto:
        print("Troppo basso! Riprova.")
    elif tentativo > numero_segreto:
        print("Troppo alto! Riprova.")
    else:
        print("Congratulazioni! Hai indovinato il numero segreto!")