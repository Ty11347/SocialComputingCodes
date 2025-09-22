# Task 2.4 Code
# Created by Tyler on 2025.Sept.22.

import sqlite3
import pandas as pd

c = sqlite3.connect('../Exercise1/minisocial_database.sqlite')

# query = """
#         SELECT puid, cuid, COUNT(puid)
#         FROM (SELECT posts.user_id puid, comments.user_id cuid
#               FROM posts
#                        INNER JOIN comments ON posts.id = comments.post_id
#               WHERE puid != cuid
#               GROUP BY puid, cuid)
#             GROUP BY puid
#             ORDER BY COUNT(puid) DESC
#         """

query = """SELECT CASE
                      WHEN posts.user_id < comments.user_id
                          THEN posts.user_id
                      ELSE comments.user_id END AS user1,
                  CASE
                      WHEN posts.user_id < comments.user_id
                          THEN comments.user_id
                      ELSE posts.user_id END    AS user2,
                  COUNT(*)                      AS count
           FROM posts
                    JOIN comments ON posts.id = comments.post_id
           WHERE posts.user_id != comments.user_id
           GROUP BY user1, user2
           ORDER BY count DESC
           LIMIT 3;
        """


res = pd.read_sql_query(query, c)
print(res)

c.close()