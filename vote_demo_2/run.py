import redis
import sqlite3

#表姐Redis类
Redis = redis.Redis

def getVotes(dbname=""):
    conn = sqlite3.connect(dbname)

    c = conn.cursor()
    sql = "select * from votes"
    c.execute(sql)
    res = c.fetchall()

    return res


def getRedis():
    rd = redis.Redis(host="localhost",port="6379",decode_responses=True)

    # redis 类
    # redis.Redis()

    #投票的基本结构：
    #初始化:name -> rank
    #人物 排名 库
    RANK_PREFIX = "RANK"  
       
    for row in res:
        name = row[1]
        rank = row[3]
        rd.set(RANK_PREFIX+name,rank)
    #人物 投票数 库
    VOTE_PREFIX = "VOTE"
    for row in res:
        name = row[1]
        vote = row[2]
        rd.set(VOTE_PREFIX+name,vote)

    #初始化:name -> score 
    #利用 zset 进行排序
    HSETNAME = "votesDB"
    for row in res:
        name = row[1]
        score = row[2]
        r = rd.zadd(HSETNAME,{name:score})
        print(r)

    rest = rd.zrangebyscore(HSETNAME,0,1000)

    print(rest)

    return rd





dbname = "./sqliteDB/votesDB.db"
res = getVotes(dbname)
# for row in res:
    # print(type(row))
    # print(row)
rd = getRedis()
# setDatasToRedis(res,rd)


