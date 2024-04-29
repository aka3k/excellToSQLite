import sqlite3

# Connessione al database
connessione = sqlite3.connect('studenti.db')
cursore = connessione.cursor()

# Esecuzione della query per studenti con sospensione del giudizio
cursore.execute("""
SELECT Alunno, Classe, Media, Esito, id
FROM studenti
WHERE Esito = "Sospensione del giudizio";
""")

# Recupero dei risultati
risultati = cursore.fetchall()

# Stampa dei risultati e salvataggio degli ID
for studente in risultati:
    id_studente = studente[4]
    # Esecuzione della query per le materie insufficienti
    cursore.execute("""
        SELECT Materia, Voto
        FROM valutazione
        WHERE idStudente = ? AND Voto < 6;
    """, (id_studente,))

    materie_insufficienti = cursore.fetchall()
    
    print(f"Nome: {studente[0]}")
    print(f"Classe: {studente[1]}")
    print(f"Media: {studente[2]}")
    print(f"Esito: {studente[3]}")
    # Stampa delle materie insufficienti
    if materie_insufficienti:
        print("Materie insufficienti:")
        for materia, voto in materie_insufficienti:
            print(f"- {materia} ({voto})")
        print()
            
# Chiusura della connessione
cursore.close()
connessione.close()
