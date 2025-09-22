# Task 1.2 Code
# Created by Tyler on 2025.Sept.13.
import sqlite3

conn = sqlite3.connect('minisocial_database.sqlite')
c = conn.cursor()

query = """SELECT COUNT(*) FROM users 
           WHERE users.id NOT IN (SELECT posts.user_id FROM posts) 
             AND users.id NOT IN (SELECT comments.user_id FROM comments) 
             AND users.id NOT IN (SELECT reactions.user_id FROM reactions);
        """

c.execute(query)
res = c.fetchall()
print(res[0][0])

conn.close()