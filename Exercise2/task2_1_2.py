# Task 2.1 Code Version 2
# Created by Tyler on 2025.Sept.22.

import math
import sqlite3

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression

c = sqlite3.connect('../Exercise1/minisocial_database.sqlite')

# predict time interval 0 = year, 1 = month, 2 = day
mode = 2

time_unit = {
    0: "Year",
    1: "Month",
    2: "Day",
}

timestamp_formats = {
    0: "'%Y'",
    1: "'%Y-%m'",
    2: "'%Y-%m-%d'"
}

timestamp = timestamp_formats.get(mode, "%Y")

query = f"""SELECT STRFTIME({timestamp}, created_at) AS date,  
               SUM(COUNT(*)) OVER (ORDER BY STRFTIME({timestamp}, created_at)) AS c_count
           FROM comments
           GROUP BY date
           ORDER BY date;
        """

res = pd.read_sql_query(query, c)
# print(res)

# calculate how many comments can a server handles
single_server_capacity = res.tail(1)['c_count'].values[0] / 16
# prepare the data
res['date'] = pd.to_datetime(res['date'])
x = np.arange(len(res)).reshape(-1, 1)
y = res['c_count'].values.reshape(-1, 1)

# use linear regression to predict data
model = LinearRegression()
model.fit(x, y)

# predict time unit length
time_length_formats = {
    0: 3,
    1: 12 * 3,
    2: 365 * 3
}
time_length = time_length_formats.get(mode, 3)

# predict data of next three unit
future_x = np.arange(len(res), len(res) + time_length).reshape(-1, 1)
future_y = model.predict(future_x)

# prediction the amount of comments on the last time interval
prediction = future_y[-1][-1].astype(int)

# servers needed =
# current comment * 120% / processed comment per server - servers already have
server_needed = math.ceil(prediction * 1.2 / single_server_capacity) - 16
print(f"Servers needed: {server_needed}")

plt.plot(x, y, color='red', label='Current')
plt.title("Cumulative Comments Over Time")
plt.xlabel(f"Time Unit: {time_unit.get(mode)}")
plt.ylabel("Total Cumulative Comments")
plt.xticks(rotation=45)
plt.grid(True)
plt.plot(future_x, future_y, color="green", label="Predicted")
plt.legend()
plt.show()

c.close()
