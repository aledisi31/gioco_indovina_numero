#Importa libreria random
import random


gioca_ancora = "s"

while gioca_ancora.lower() == "s":
    #genera un numero segreto
    numero_segreto = random.randint(1, 100)
    tentativo = 0
    tentativi_massimi = 5

    #Stampa un messaggio di benvenuto e chiedi all'utente di indovinare il numero segreto
    print("Benvenuto al gioco del numero segreto!")
    contatore = tentativi_massimi

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
            print(f"Troppo basso! Riprova. Hai {contatore} tentativi rimasti.")
        elif tentativo > numero_segreto:
            print(f"Troppo alto! Riprova. Hai {contatore} tentativi rimasti.")

    if tentativo == numero_segreto:
            print(f"Hai indovinato in {5 - contatore} tentativi.")
    else:        print(f"Hai esaurito i tentativi! Il numero segreto era {numero_segreto}")

    #Chiedi all'utente se vuole giocare ancora
    gioca_ancora = input("Vuoi giocare ancora? (s/n): ")
print("Grazie per aver giocato! Arrivederci!")