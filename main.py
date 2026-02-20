#Importa libreria random
import random

#genera un numero segreto
numero_segreto = random.randint(1, 100)

#Stampa un messaggio di benvenuto e chiedi all'utente di indovinare il numero segreto
print("Benvenuto al gioco del numero segreto!")
tentativo = input("Indovina il numero segreto tra 1 e 100: ")
#Trasforma l'input dell'utente in un numero intero
tentativo = int(tentativo)

#Mostra cosa ha inserito l'utente
print("Hai inserito:", tentativo)

#Controlla se l'utente ha indovinato il numero segreto
if tentativo == numero_segreto:
    print("Congratulazioni! Hai indovinato il numero segreto!")
else:
    print("Mi dispiace, non hai indovinato. Il numero segreto era:", numero_segreto)