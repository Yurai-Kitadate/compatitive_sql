import sqlite3
A, B, C = map(int, input().split())
dbname = 'main.db'
conn = sqlite3.connect(dbname)
cur = conn.cursor()
a = ""
sql = [
    "SELECT '' || ",
    "CASE WHEN ({} / {} = {} / {}) AND ({} <= ({} / {}) * {}) and (({} / {}) * {} <= {}) THEN ({} / {}) * {} ".format(A,
                                                                                                                                                   C, B, C, A, A, C, C, A, C, C, B, A, C, C),
    "WHEN ({} <= (({} / {}) + 1) * {}) and ((({} / {}) + 1) * {} <= {}) THEN (({} / {}) + 1) * {} ".format(A,
                                                                                                                          A, C, C, A, C, C, B, A, C, C),
    "ELSE -1 ",
    "END ",
]
for i in sql:
    a += i
cur.execute(a)
for i in cur:
    print(i[0])
