import sqlite3

# Collegati al database SQLite
conn = sqlite3.connect('studenti.db')

# Ottieni una lista di tutte le tabelle nel database
cursor = conn.cursor()
cursor.execute('SELECT name FROM sqlite_master WHERE type="table"')
table_names = [name[0] for name in cursor.fetchall()]

# Elimina tutte le tabelle
for table_name in table_names:
    cursor.execute(f'DROP TABLE IF EXISTS {table_name}')

# Chiudi la connessione al database
conn.close()
print("dati eliminati correttamente")