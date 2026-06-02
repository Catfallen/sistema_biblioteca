import sqlite3

# Arquivo SQLite de origem
db_file = "biblioteca.db"

# Arquivo SQL de saída
sql_file = "biblioteca.sql"

conn = sqlite3.connect(db_file)

with open(sql_file, "w", encoding="utf-8") as f:
    for linha in conn.iterdump():
        f.write(linha + "\n")

conn.close()

print(f"Backup SQL gerado com sucesso: {sql_file}")