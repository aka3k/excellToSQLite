import sqlite3
# Establish connection to the database
connection = sqlite3.connect("studenti.db")
cursor = connection.cursor()

# Truncate the 'studenti' table
cursor.execute("DELETE FROM studenti;")

# Truncate the 'valutazione' table
cursor.execute("DELETE FROM valutazione;")

cursor.execute("DELETE FROM sqlite_sequence")
# Commit changes to the database
connection.commit()

# Close the database connection
connection.close()

print("Tables 'studenti' and 'valutazione' successfully truncated!")
