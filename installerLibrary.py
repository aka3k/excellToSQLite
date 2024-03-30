import subprocess
import sys

# Comandi per controllare l'installazione di Pandas e xlrd
comando_pandas = "pip show pandas"
comando_xlrd = "pip show xlrd"

# Controllo Pandas
processo_pandas = subprocess.run(comando_pandas.split(), stdout=subprocess.PIPE, stderr=subprocess.PIPE)
pandas_installato = processo_pandas.returncode == 0

# Controllo xlrd
processo_xlrd = subprocess.run(comando_xlrd.split(), stdout=subprocess.PIPE, stderr=subprocess.PIPE)
xlrd_installato = processo_xlrd.returncode == 0

# Stampa dei messaggi
if pandas_installato and xlrd_installato:
    print("Le librerie Pandas e xlrd sono già installate.")
elif pandas_installato:
    print("La libreria Pandas è già installata.")
elif xlrd_installato:
    print("La libreria xlrd è già installata.")
else:
    print("Nessuna delle librerie Pandas e xlrd è installata.")

# Installazione librerie se non presenti
if not pandas_installato or not xlrd_installato:
    print("Proseguo con l'installazione...")
    
    # Comando per installare Pandas e xlrd
    comando_installazione = "pip install pandas xlrd"
    
    # Esecuzione del comando di installazione
    subprocess.run(comando_installazione.split())
    
    print("Installazione completata!")

