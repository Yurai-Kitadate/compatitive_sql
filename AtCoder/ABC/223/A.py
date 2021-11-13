import sqlite3
X = int(input())
dbname = 'main.db'
conn = sqlite3.connect(dbname)
cur = conn.cursor()
a = ""
sql = [
  "SELECT '' ||",
  "CASE WHEN ({} >= 100) and  ({} % 100 = 0) THEN 'Yes' ".format(X,X),
  "ELSE  'No' ",
  "END"
]
for i in sql:
  a += i
cur.execute(a)
for i in cur:
  print(i[0])
