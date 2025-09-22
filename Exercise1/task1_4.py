# Task 1.4 Code
# Created by Tyler on 2025.Sept.13.
import sqlite3
# for tabulate
import pandas as pd

conn = sqlite3.connect('minisocial_database.sqlite')

query = """
        SELECT username, times
        FROM (SELECT user_id, content, COUNT(*) AS times
              From (SELECT user_id, content
                    FROM comments
                    UNION ALL
                    SELECT user_id, content
                    FROM posts) AS texts
              GROUP BY user_id, content
              HAVING COUNT(*) >= 3
              ORDER BY times DESC)
                 INNER JOIN users ON users.id = user_id
        """

res = pd.read_sql_query(query, conn)
print(res)

conn.close()
