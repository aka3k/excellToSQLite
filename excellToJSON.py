import pandas as pd

# Installare pandas e xlrd 

# Carica il file Excel in un DataFrame
path_excel = '1Sin.xls'
df = pd.read_excel(path_excel, engine='xlrd', usecols=['Pr.', 'Alunno', 'RELIGIONE', 
                    'LINGUA E LETT.IT', 'LINGUA INGLESE', 'STORIA', 'EDUCAZIONE CIVICA',
                    'MATEMATICA', 'DIRITTO ED ECONOMIA', 'FISICA', 'CHIMICA', 'Tecn.informatiche',
                    'Tecn.e Tecn.di rappr','SC.DELLA TERRA/GEO', 'SCIENZE MOT. E SPORT', 'COMPORTAMENTO', 
                    'Media', 'Esito'], skiprows=3)# Seleziona le colonne che hanno questo nome

# Trova l'indice della prima riga con tutti i valori nulli
for i, row in df.iterrows():
    if all(pd.isnull(row)):
        break

# Crea un nuovo DataFrame con solo le righe fino all'indice trovato
df_filtered = df.iloc[:i]

# Converti il DataFrame in JSON
json_data = df_filtered.to_json(orient='records', indent=4)

# Scrivi i dati JSON su un file
path_json = 'final_result.json'
with open(path_json, 'w') as json_file:
    json_file.write(json_data)

print("Conversione completata con successo.")
