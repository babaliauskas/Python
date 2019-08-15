import sqlite3

conn = sqlite3.connect('SQLite/my_friends.db')

c = conn.cursor()

people = [
    ("Ronald", "Amundsen", 5),
    ("Rosa", "Parks", 25),
    ("Henry", "Hudson", 9),
    ("Neil", "Armstrong", 11),
    ("Daniel", "Boone", 7)
]

# for person in people:
#     c.execute("INSERT INTO friends VALUES (?,?,?)", person)
#     print('Inserting!!!!)

c.executemany("INSERT INTO friends VALUES (?,?,?)", people)
conn.commit()
conn.close()
