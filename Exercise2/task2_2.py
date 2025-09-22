# Task 2.2 Code
# Created by Tyler on 2025.Sept.22.

import sqlite3
import pandas as pd

c = sqlite3.connect('../Exercise1/minisocial_database.sqlite')

query = """
        SELECT posts.content, COUNT(comments.content)
        FROM posts
                 INNER JOIN comments ON posts.id = comments.post_id
        GROUP BY posts.content
        ORDER BY COUNT(comments.content) DESC
        LIMIT 3;
        """

res = pd.read_sql_query(query, c)
print(res)

c.close()
