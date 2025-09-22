# Task 1.1 Code
# Created by Tyler on 2025.Sept.10.
import sqlite3

conn = sqlite3.connect('minisocial_database.sqlite')

c = conn.cursor()
# c.execute("SHOW TABLES;")
c.execute("SELECT name FROM sqlite_master WHERE type='table';")
# print(c.fetchall())

# A better visualize way
res = c.fetchall()
table_names = [r[0] for r in res]
print(table_names)

for table_name in table_names:
    c.execute(f"SELECT * FROM ({table_name}) LIMIT 5;")
    rows = c.fetchall()
    c.execute(f"PRAGMA table_info({table_name});")
    cols = c.fetchall()
    print(f"{table_name}" + " table")
    print(len(rows), "records found")
    col_name = ""
    for col in cols:
        # print(f"{col[1]}")
        col_name += (col[1] + "(" + col[2] + ") ")

    print(col_name)
    for row in rows:
        print(row)

    print("________________")

    conn.close()

# ---------------------------------------
# res = c.execute("SELECT * FROM follows")

# c.execute("SELECT * FROM follows LIMIT 5;")
# c.execute("SELECT * FROM users;")
# rows = c.fetchall()
# print(len(rows))
# for row in rows:
#     print(row)

# c.execute(f"PRAGMA table_info(follows);")
# columns = c.fetchall()
# for col in columns:
#     print(col)
# print(res.fetchall())
