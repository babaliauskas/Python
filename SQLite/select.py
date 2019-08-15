import sqlite3

conn = sqlite3.connect('SQLite/my_friends.db')
c = conn.cursor()

# c.execute("SELECT * FROM friends WHERE first_name IS 'Rosa'")
c.execute("SELECT * FROM friends WHERE closeness > 5 ORDER BY closeness")

# for result in c:
#     print(result)


print(c.fetchall())
# print(c.fetchone())

conn.commit()
conn.close()
