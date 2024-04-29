import sqlite3

# Connessione al database
connessione = sqlite3.connect("studenti.db")
cursor = connessione.cursor()

# Pulizia della tabella 'studenti'
cursor.execute("DELETE FROM studenti;")

# Pulizia della tabella 'valutazione'
cursor.execute("DELETE FROM valutazione;")

# Reset sequenza
cursor.execute("DELETE FROM sqlite_sequence")

# Salvataggio delle modifiche al database
connessione.commit()

# Chiusura della connessione al database
connessione.close()

# Messaggio di conferma
print("i dati in studenti e valutazioni sono stati eliminati!")