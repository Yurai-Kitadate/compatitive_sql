import sqlite3
A, B = map(int, input().split())
dbname = 'main.db'
conn = sqlite3.connect(dbname)
cur = conn.cursor()
a = ""
sql = [
    "SELECT '' || ",
    "CASE WHEN {} <= {} THEN {} - {} + 1 ELSE 0 END".format(A, B,B,A)

]
for i in sql:
    a += i
cur.execute(a)
for i in cur:
    print(i[0])
