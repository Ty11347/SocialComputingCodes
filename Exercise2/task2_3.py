# Task 2.3 Code
# Created by Tyler on 2025.Sept.22.

import sqlite3
import pandas as pd
import datetime

c = sqlite3.connect('../Exercise1/minisocial_database.sqlite')

query_first_reply = """SELECT AVG(first_diff)
                       FROM (SELECT posts.id pid,
                                    MIN(julianday(comments.created_at) - julianday(posts.created_at)) * 24 * 60
                                        AS   first_diff
                             FROM posts
                                      INNER JOIN comments ON posts.id = comments.post_id
                             GROUP BY pid);
                    """

query_last_reply = """SELECT AVG(last_diff)
                      FROM (SELECT posts.id pid,
                                   MAX(julianday(comments.created_at) - julianday(posts.created_at)) * 24 * 60
                                       AS   last_diff
                            FROM posts
                                     INNER JOIN comments ON posts.id = comments.post_id
                            GROUP BY pid);
                   """

res_first_reply = pd.read_sql_query(query_first_reply, c)['AVG(first_diff)'][0]
res_last_reply = pd.read_sql_query(query_last_reply, c)['AVG(last_diff)'][0]

print("Average Time of First Comment: " + str(datetime.timedelta(seconds=round(res_first_reply))))
print("Average Time of Last Comment: " + str(datetime.timedelta(seconds=round(res_last_reply))))