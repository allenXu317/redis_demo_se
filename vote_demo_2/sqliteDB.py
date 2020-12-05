import sqlite3

#创建数据库
conn = sqlite3.connect("./sqliteDB/votesDB.db")

c = conn.cursor()

sql = "CREATE TABLE votes (\
    id   INTEGER PRIMARY KEY AUTOINCREMENT\
                 UNIQUE,\
    name VARCHAR,\
    vote BIGINT,\
    rank BIGINT\
);"

#执行sql语句创建
# c.execute(sql)

sql = "INSERT INTO votes (name,vote,rank) VALUES ('cc',5,3)"
c.execute(sql)
conn.commit()

sql = "select * from votes"
c.execute(sql)

res = c.fetchall()
print(res)