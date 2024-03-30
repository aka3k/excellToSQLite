import json
import pandas as pd

# Carica il file Excel in un DataFrame
path_excel = '1Sin.xls'
df = pd.read_excel(path_excel, engine='xlrd', usecols=range(0, 28), skiprows=3) # Select columns 1 to 18 (0-based indexing)

# Rinomina le colonne
df.columns = ['Pr.', 'Alunno', 'spazioVuoto1', 'spazioVuoto2', 'spazioVuoto3', 'spazioVuoto4',
                'spazioVuoto5', 'spazioVuoto6', 'spazioVuoto7', 'spazioVuoto8','RELIGIONE', 
                'LINGUA E LETT.IT', 'LINGUA INGLESE', 'STORIA', 'EDUCAZIONE CIVICA',
                'MATEMATICA', 'DIRITTO ED ECONOMIA', 'FISICA', 'CHIMICA', 'Tecn.informatiche',
                'Tecn.e Tecn.di rappr','SC.DELLA TERRA/GEO', 'SCIENZE MOT. E SPORT', 'COMPORTAMENTO', 
                'Media', 'spazioVuoto9', 'spazioVuoto10', 'Esito']

# Crea una lista per memorizzare i dizionari
json_data = []

# Itera su ogni riga del DataFrame
for row in df.itertuples():
    # Crea un dizionario per ogni riga
    record = {}
    
    # Aggiungi solo le colonne con valori non nulli
    for col, value in zip(df.columns, row):
        if not pd.isnull(value):
            record[col] = value
    
    # Aggiungi il dizionario alla lista
    json_data.append(record)

# Scrivi i dati JSON su un file
path_json = 'final_result.json'
with open(path_json, 'w') as json_file:
    json.dump(json_data, json_file, indent=4)

print("Conversione completata con successo.")
