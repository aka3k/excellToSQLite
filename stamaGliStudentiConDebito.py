import sqlite3

# Connessione al database
connessione = sqlite3.connect('studenti.db')
cursore = connessione.cursor()

# Esecuzione della query
cursore.execute("""
SELECT Alunno, Media, Esito
FROM studenti
WHERE Esito = "Sospensione del giudizio";
""")

# Recupero dei risultati
risultati = cursore.fetchall()

# Stampa dei risultati
for studente in risultati:
    print(f"Nome: {studente[0]}")
    print(f"Media: {studente[1]}")
    print(f"Esito: {studente[2]}\n")

# Chiusura della connessione
cursore.close()
connessione.close()
