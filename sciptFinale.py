import subprocess
import os

# Elenco script da eseguire
script_da_eseguire = ["installerLibrary.py", "excellToJSON.py", "jsonToSQLite3.py"]

# Percorso della directory corrente
directory_corrente = os.getcwd()

# Esecuzione degli script in ordine
for script in script_da_eseguire:
    comando = f"python {os.path.join(directory_corrente, script)}"
    print(f"Esecuzione script: {script}")
    subprocess.run(comando.split())

print("Tutti gli script sono stati eseguiti correttamente!")
