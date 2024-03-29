import xlrd
import json

# Caricare il file XLS
workbook = xlrd.open_workbook('1Sin.xls')

# Selezionare il foglio di lavoro
sheet = workbook.sheet_by_name('TABELLONE VOTI')

# Ottenere le dimensioni della matrice
nrows = sheet.nrows
ncols = sheet.ncols

# Creare una matrice vuota
matrice = [[None for i in range(ncols)] for j in range(nrows)]

# Leggere i dati dalla tabella e inserirli nella matrice
for i in range(nrows):
    for j in range(ncols):
        matrice[i][j] = sheet.cell(i, j).value

# Stampare la matrice
for i in range(nrows):
    for j in range(ncols):
        print(matrice[i][j], end=" ")
    print()

# Save matrix data into a JSON file
with open("matrix_data.json", "w") as json_file:
    json.dump(matrice, json_file, indent=4)