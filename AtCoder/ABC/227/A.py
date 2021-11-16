import sqlite3
N, K, A = map(int, input().split())
dbname = 'main.db'
conn = sqlite3.connect(dbname)
cur = conn.cursor()
a = ""
sql = [
    "select '' || ",
    "case when ({} + {}) % {} = 0 then {} ".format(A, K - 1, N,N),
    "else ({} + {}) % {} end".format(A, K - 1, N)

]
for i in sql:
    a += i
cur.execute(a)
for i in cur:
    print(i[0])
