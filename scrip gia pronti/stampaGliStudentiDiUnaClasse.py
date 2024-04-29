import sqlite3

# Connessione al database
connessione = sqlite3.connect('studenti.db')
cursore = connessione.cursor()

# Richiesta della classe all'utente
classe_ricercata = input("Inserisci la classe da ricercare: ")

# Esecuzione della query
cursore.execute("""
    SELECT pr, alunno, media, esito, classe
    FROM studenti
    WHERE classe = ?;
""", (classe_ricercata,))

# Recupero dei risultati
risultati = cursore.fetchall()

# Controllo sulla presenza di studenti
if risultati:
    # Stampa dei risultati
    for studente in risultati:
        print(f"Pr: {studente[0]}")
        print(f"Nome: {studente[1]}")
        print(f"Media: {studente[2]}")
        print(f"Esito: {studente[3]}")
        print(f"Classe: {studente[4]}\n")
else:
    # Stampa messaggio di assenza
    print(f"Non ci sono studenti nella classe '{classe_ricercata}'.")

# Chiusura della connessione
cursore.close()
connessione.close()
