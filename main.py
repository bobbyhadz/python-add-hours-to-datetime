# Add hours to datetime in Python

from datetime import datetime, timedelta

d = '2023-11-24 09:30:00.000123'

# 👇️ convert string to datetime object
dt = datetime.strptime(d, '%Y-%m-%d %H:%M:%S.%f')

print(dt)  # 👉️ 2023-11-24 09:30:00.000123

result = dt + timedelta(hours=3)
print(result)  # 👉️ 2023-11-24 12:30:00.000123