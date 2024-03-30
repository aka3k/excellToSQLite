import sqlite3
import json

# Connect to SQLite3 database or create it if it doesn't exist
conn = sqlite3.connect('studenti.db')
c = conn.cursor()

# Create studenti table
c.execute('''CREATE TABLE IF NOT EXISTS studenti
             (Pr REAL, Alunno TEXT, RELIGIONE TEXT, LINGUA_E_LETT_IT REAL,
              LINGUA_INGLESE REAL, STORIA REAL, EDUCAZIONE_CIVICA REAL,
              MATEMATICA REAL, DIRITTO_ED_ECONOMIA REAL, FISICA REAL,
              CHIMICA REAL, TECN_INFORMATICHE REAL, TECN_E_TECN_DI_RAPPR REAL,
              SC_DELLA_TERRA_GEO REAL, SCIENZE_MOT_E_SPORT REAL, COMPORTAMENTO REAL,
              Media REAL, Esito TEXT)''')

# Load data from JSON file
with open('final_result.json') as f:
    data = json.load(f)

# Insert data into studenti table
for student in data:
    c.execute('''SELECT COUNT(*) FROM studenti WHERE Alunno=?''', (student['Alunno'],))
    if c.fetchone()[0] == 0:
        c.execute('''INSERT INTO studenti VALUES (?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?)''',
                  (student['Pr.'], student['Alunno'], student['RELIGIONE'],
                   student['LINGUA E LETT.IT'], student['LINGUA INGLESE'],
                   student['STORIA'], student['EDUCAZIONE CIVICA'],
                   student['MATEMATICA'], student['DIRITTO ED ECONOMIA'],
                   student['FISICA'], student['CHIMICA'], student['Tecn.informatiche'],
                   student['Tecn.e Tecn.di rappr'], student['SC.DELLA TERRA/GEO'],
                   student['SCIENZE MOT. E SPORT'], student['COMPORTAMENTO'],
                   student['Media'], student['Esito']))

# Commit changes and close connection
conn.commit()
conn.close()

if c.rowcount > 0:
    print("Dati aggiunti con successo.")
else:
    print("Nessun dato aggiunto, tutti i dati erano già presenti nel database.")