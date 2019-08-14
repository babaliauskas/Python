import sqlite3

conn = sqlite3.connect('SQLite/my_friends.db')

c = conn.cursor()

# c.execute(
# "CREATE TABLE friends (first_name TEXT, last_name TEXT, closeness INTEGER);")

# insert_query = '''INSERT INTO friends
#                   VALUES ('Lukas', 'Babaliauskas', 2)'''

# first = 'Modestas'
# query = f"INSERT INTO friends (first_name) VALUES (?)"


data = ("Zygis", "Gedrimas", 6)
query = "INSERT INTO friends VALUES (?,?,?)"
c.execute(query, data)

conn.commit()
conn.close()
