import sqlite3

# Connetti al database
connessione = sqlite3.connect('studenti.db')
cursore = connessione.cursor()

# Esegui la query
cursore.execute("SELECT * FROM studenti")

# Controlla se sono stati trovati risultati
righe = cursore.fetchall()

if righe:
    # Ottieni i nomi delle colonne
    colonne = [colonna[0] for colonna in cursore.description]

    # Stampa i nomi delle colonne
    print(" ".join(colonne))

    # Stampa i dati
    for riga in righe:
        print(" ".join(str(dato) for dato in riga))
else:
    print("No data found in the table!")

connessione.close()
