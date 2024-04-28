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

    # Stampa della lista nomi_celle filtrata
    print(nomi_celle_filtrati)
    print()
