import sqlite3
import json
import os

# Funzione per estrarre un campo da una posizione in un dizionario o lista
def estrai_campo_per_posizione(data, posizione):
    if isinstance(data, dict):
        if posizione < len(data) :
            return list(data.items())[posizione]  # Estrai coppia nome-valore in base alla posizione
        else:
            raise IndexError("Indice fuori dal range per il dizionario")
    elif isinstance(data, list):
        if posizione < len(data):
            return data[posizione]  # Estrai valore in base alla posizione nella lista
        else:
            return False

    else:
        raise TypeError("Tipo di dato non supportato")

# Nome del database
db_name = "studenti.db"

# Creazione connessione e cursore
connection = sqlite3.connect(db_name)
cursor = connection.cursor()
cursor2 = connection.cursor()

# Creazione tabella studenti (se non esiste)
cursor.execute("""
CREATE TABLE IF NOT EXISTS studenti (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    pr REAL,
    alunno TEXT,
    media REAL,
    esito TEXT,
    classe TEXT
);
""")

# Creazione tabella valutazione (se non esiste)
cursor.execute("""
CREATE TABLE IF NOT EXISTS valutazione (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    idStudente INTEGER,
    materia TEXT,
    voto REAL,
    FOREIGN KEY (idStudente) REFERENCES studenti(id)
);
""")

# Cartella dei file JSON
data_folder = "file_json"

duplicated_data=False
# Popolamento tabelle da file JSON
for filename in os.listdir(data_folder):
    if filename.endswith(".json"):
        file_path = os.path.join(data_folder, filename)

        with open(file_path, "r") as file:
            student_data = json.load(file)

        # Inserimento dati studente nella tabella studenti
        for materie in student_data:
            cursor.execute("""
            SELECT pr, alunno, media, esito, classe
            FROM studenti
            WHERE pr =? AND alunno =? AND media =? AND esito =? AND classe =?
            """, (
                str(materie["Pr."]),
                materie["Alunno"],
                str(materie["Media"]),
                materie["Esito"],
                materie["Classe"],
            ))

            # Fetch del risultato come singola riga
            duplicate = cursor.fetchone()
            if(duplicate):
                if(duplicated_data==False):
                    print("Sono stati trovati dei dati duplicati che non verranno inseriti")
                    duplicated_data=True
            else:
                cursor.execute("""
                INSERT INTO studenti (pr, alunno, media, esito, classe)
                VALUES (?,?,?,?,?);
                """, (
                    materie["Pr."],
                    materie["Alunno"],
                    materie["Media"],
                    materie["Esito"],
                    materie["Classe"],
                ))
                for field_name, field_value in materie.items():
                    if field_name!= "Pr." and field_name!= "Media" and field_name!= "Esito" and field_name!= "Classe" and field_name!= "Alunno":
                        cursor.execute("SELECT MAX(id) AS max_student_id FROM studenti;")

                        # Fetch del risultato come singola riga
                        max_student_id_row = cursor.fetchone()

                        # Estrazione dell'ID studente massimo dalla riga
                        max_student_id = max_student_id_row[0] if max_student_id_row else None

                        cursor2.execute("""
                        INSERT INTO valutazione (idStudente, materia, voto)
                        VALUES (?,?,?);
                        """, (max_student_id, field_name, field_value))

# Commit delle modifiche e chiusura della connessione
connection.commit()
connection.close()

print("Il database è stato riempito con i dati!")