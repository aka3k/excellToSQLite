import sqlite3
import json
import os

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
# Database name
db_name = "studenti.db"

# Create connection and cursor
connection = sqlite3.connect(db_name)
cursor = connection.cursor()
cursor2 = connection.cursor()

# Create 'studenti' table (if it doesn't exist)
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

# Create 'valutazione' table (if it doesn't exist)
cursor.execute("""
CREATE TABLE IF NOT EXISTS valutazione (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    idStudente INTEGER,
    materia TEXT,
    voto REAL,
    FOREIGN KEY (idStudente) REFERENCES studenti(id)
);
""")

# Data folder
data_folder = "file_json"

# Populate tables from JSON files
for filename in os.listdir(data_folder):
    if filename.endswith(".json"):
        file_path = os.path.join(data_folder, filename)

        with open(file_path, "r") as file:
            student_data = json.load(file)

        # Insert student data into 'studenti' table
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


            # Fetch the result as a single row
            duplicate = cursor.fetchone()
            if(duplicate):
                print("dato duplicato")
            else:
                cursor.execute("""
                INSERT INTO studenti (pr, alunno, media, esito, classe)
                VALUES (?, ?, ?, ?, ?);
                """, (
                    materie["Pr."],
                    materie["Alunno"],
                    materie["Media"],
                    materie["Esito"],
                    materie["Classe"],
                ))
                for field_name, field_value in materie.items():
                    if field_name != "Pr." and field_name != "Media" and field_name != "Esito" and field_name != "Classe" and field_name != "Alunno":
                        cursor.execute("SELECT MAX(id) AS max_student_id FROM studenti;")

                        # Fetch the result as a single row
                        max_student_id_row = cursor.fetchone()

                        # Extract the maximum student ID from the row
                        max_student_id = max_student_id_row[0] if max_student_id_row else None

                        cursor2.execute("""
                        INSERT INTO valutazione (idStudente, materia, voto)
                        VALUES (?, ?, ?);
                        """, (max_student_id, field_name, field_value))

# Commit changes and close connection
connection.commit()
connection.close()

print("Database populated with data from JSON files!")



            