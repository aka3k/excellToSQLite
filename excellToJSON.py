import pandas as pd
#installare pandas e xlrd

# Carica il file Excel in un DataFrame
path_excel = '1Sin.xls'
df = pd.read_excel(path_excel, engine='xlrd', usecols=['Pr.', 'Alunno', 'RELIGIONE', 
                'LINGUA E LETT.IT', 'LINGUA INGLESE', 'STORIA', 'EDUCAZIONE CIVICA',
                'MATEMATICA', 'DIRITTO ED ECONOMIA', 'FISICA', 'CHIMICA', 'Tecn.informatiche',
                'Tecn.e Tecn.di rappr','SC.DELLA TERRA/GEO', 'SCIENZE MOT. E SPORT', 'COMPORTAMENTO', 
                'Media', 'Esito'], skiprows=3)# Select columns 1 to 18 (0-based indexing)



# Converti il DataFrame in JSON
json_data = df.to_json(orient='records', indent=4)

# Scrivi i dati JSON su un file
path_json = 'final_result.json'
with open(path_json, 'w') as json_file:
    json_file.write(json_data)


print("Conversione completata con successo.")
