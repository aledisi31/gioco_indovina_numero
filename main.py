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
    try:
        tentativo = int(risposta)
    except ValueError:
        #Se l'input non è un numero valido, stampa un messaggio di errore e continua il ciclo
        print("Inserisci un numero valido, non una lettera!")
        continue #ricomincia il ciclo dal via senza eseguire il resto del codice

    if tentativo < numero_segreto:
        print("Troppo basso! Riprova.")
    elif tentativo > numero_segreto:
        print("Troppo alto! Riprova.")
    else:
        print("Congratulazioni! Hai indovinato il numero segreto!")