# Task 1.3 Code
# Created by Tyler on 2025.Sept.13.
import sqlite3
# for tabulate
import pandas as pd

conn = sqlite3.connect('minisocial_database.sqlite')

# 5 users have most followers
query_most_followers = """SELECT username, COUNT(followed_id) AS followers
                          FROM users
                                   INNER JOIN follows ON users.id = follows.followed_id
                          GROUP BY users.id, followed_id
                          ORDER BY followers DESC
                          LIMIT 5"""
res1 = pd.read_sql_query(query_most_followers, conn)
print(res1)

# 5 users have most likes
query_most_likes = """SELECT username, COUNT(reactions.reaction_type) AS likes
                      FROM users
                               INNER JOIN posts ON users.id = posts.user_id
                               INNER JOIN reactions ON posts.id = reactions.post_id
                      WHERE reactions.reaction_type IN ('like', 'love')
                      GROUP BY users.id
                      ORDER BY likes DESC
                      LIMIT 5"""

res2 = pd.read_sql_query(query_most_likes, conn)
# print(res2)

conn.close()
