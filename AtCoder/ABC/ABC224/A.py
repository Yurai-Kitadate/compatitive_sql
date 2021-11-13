import sqlite3
n = input()
dbname = 'main.db'
conn = sqlite3.connect(dbname)
cur = conn.cursor()
a = ""
sql = [
  "SELECT '' ||",
  "CASE WHEN '{}' LIKE '%er' THEN 'er' ".format(n,n),
  "ELSE  'ist' ",
  "END"
]
for i in sql:
  a += i
cur.execute(a)
for i in cur:
  print(i[0])
