#Importa libreria random
import random

#genera un numero segreto
numero_segreto = random.randint(1, 100)
tentativo = 0
tentativi_massimi = 5

#Stampa un messaggio di benvenuto e chiedi all'utente di indovinare il numero segreto
print("Benvenuto al gioco del numero segreto!")
contatore = 5

#Ciclo finché l'utente non indovina il numero segreto
while tentativo != numero_segreto and contatore > 0:
    risposta = input("Indovina il numero segreto (tra 1 e 100): ")
    try:
        tentativo = int(risposta)
        contatore -= 1
    except ValueError:
        #Se l'input non è un numero valido, stampa un messaggio di errore e continua il ciclo
        print("Inserisci un numero valido, non una lettera!")
        continue #ricomincia il ciclo dal via senza eseguire il resto del codice
    

  

    if tentativo < numero_segreto:
        print("Troppo basso! Riprova. Hai", contatore, "tentativi rimasti.")
    elif tentativo > numero_segreto:
        print("Troppo alto! Riprova. Hai", contatore, "tentativi rimasti.")

if tentativo == numero_segreto:
        print("Hai indovinato in", 5 - contatore, "tentativi.")
else:        print("Hai esaurito i tentativi! Il numero segreto era", numero_segreto)