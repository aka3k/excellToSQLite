import pandas as pd
import os
import json

# Ottieni la directory di lavoro corrente (dove viene eseguito il programma)
cwd = os.getcwd()

# Imposta il percorso della cartella contenente i file Excel
directory_excel = os.path.join(cwd, "file_excell")  # percorso completo della cartella Excel

# Recupera un elenco di tutti i file Excel nella cartella
nomi_file_excel = [f for f in os.listdir(directory_excel) if f.endswith('.xls')]  # lista di nomi file Excel

# Cicla su ogni file Excel
for nome_file_excel in nomi_file_excel:
    # Ottieni il percorso completo del file Excel corrente
    percorso_excel = os.path.join(directory_excel, nome_file_excel)

    # Estrai il nome del file senza estensione
    nome_file_senza_estensione, _ = os.path.splitext(nome_file_excel)
    
    
    # Codice che mi va a prendere i valori presenti nelle celle della riga 4 (materie ecc)
    # Lettura del file Excel come DataFrame
    df = pd.read_excel(percorso_excel)

    # Estrazione della riga 4
    riga4 = df.iloc[2]  # Assuming row 4 is indexed at 2

    # Conversione della riga 4 in un dizionario
    riga4_dict = riga4.to_dict()

    # Creazione della lista nomi_celle
    nomi_celle = []

    # Ciclo sui valori del dizionario (le celle della riga 4)
    for valore in riga4_dict.values():
        # Aggiungi il valore alla lista
        nomi_celle.append(valore)

    # Rimozione dei valori NaN dalla lista nomi_celle
    nomi_celle_filtrati = [valore for valore in nomi_celle if not pd.isna(valore)]



    # Leggi il file Excel in un DataFrame di Pandas
    df = pd.read_excel(percorso_excel, engine='xlrd', usecols=nomi_celle_filtrati, skiprows=3)

    # Trova l'indice della prima riga con tutti i valori nulli
    for i, row in df.iterrows():
        if all(pd.isnull(row)):
            break

    # Aggiungi la classe come un nuovo campo nel DataFrame
    df['Classe'] = nome_file_senza_estensione
    
    # Crea un nuovo DataFrame con solo le righe fino all'indice trovato
    df_filtrato = df.iloc[:i]

    # Converti il DataFrame in formato JSON
    dati_json = df_filtrato.to_json(orient='records', indent=4)

    # Imposta il percorso del file JSON utilizzando il nome del file estratto e la directory di lavoro corrente
    percorso_json = os.path.join(cwd, "file_json", f"{nome_file_senza_estensione}.json")

    # Crea la cartella "file_json" se non esiste (nella directory di lavoro corrente)
    os.makedirs(os.path.dirname(percorso_json), exist_ok=True)

    # Scrivi i dati JSON nel file
    with open(percorso_json, 'w') as json_file:
        json_file.write(dati_json)

    # Stampa un messaggio di conversione riuscita per il file corrente
    print(f"File convertito: {nome_file_excel}")

print("Conversione di tutti i file Excel nella cartella 'file_excell' completata.")