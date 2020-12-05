import redis
import sqlite3


Redis = redis.Redis



def getRedis():
    rd = redis.Redis(host="localhost",port="6379",decode_responses=True)
    return rd


def getVotes(dbname=""):
    conn = sqlite3.connect(dbname)

    c = conn.cursor()
    sql = "select * from votes"
    c.execute(sql)
    res = c.fetchall()

    return res


# 投支持票
def voteToUp(name:str):
    HSETNAME = "votesdb"    
    RANK_PREFIX = "RANK"
    VOTE_PREFIX = "VOTE"


    rd = getRedis()
    rank = int(rd.get(RANK_PREFIX+name)) + 1
    vote = int(rd.get(VOTE_PREFIX+name))

    
    ss = "用户" + name + "初始的票数是:"+ str(vote)  + "   投票前的排名是：" + str(rank)
    print(ss)
    # 进行投票操作
    vote += 1
    # 更新投票数据
    rd.zadd(HSETNAME,{name:vote})
    # 更新排名
    rank = rd.zrevrank(HSETNAME,name)

    # 写回rank和vote的集合库
    rd.set(RANK_PREFIX+name,rank)
    rd.set(VOTE_PREFIX+name,vote)

    
    rank = rd.get(RANK_PREFIX+name)
    vote = int(rd.get(VOTE_PREFIX+name))

    ss = "给用户" + name + "投赞成票，现在的票数是:"+ str(vote)  + "   投票的后排名是：" + str(int(rank)+1)
    print(ss)

# 投反对票
def voteToDown(name:str):
    HSETNAME = "votesdb"    
    RANK_PREFIX = "RANK"
    VOTE_PREFIX = "VOTE"


    rd = getRedis()
    rank = int(rd.get(RANK_PREFIX+name)) + 1
    vote = int(rd.get(VOTE_PREFIX+name))

    
    ss = "用户" + name + "初始的票数是:"+ str(vote)  + "   投票前的排名是：" + str(rank)
    print(ss)
    # 进行投票操作
    vote -= 1
    # 更新投票数据
    rd.zadd(HSETNAME,{name:vote})
    # 更新排名
    rank = rd.zrevrank(HSETNAME,name)

    # 写回rank和vote的集合库
    rd.set(RANK_PREFIX+name,rank)
    rd.set(VOTE_PREFIX+name,vote)

    
    rank = rd.get(RANK_PREFIX+name)
    vote = int(rd.get(VOTE_PREFIX+name))

    ss = "给用户" + name + "投反对票，现在的票数是:"+ str(vote)  + "   投票的后排名是：" + str(int(rank)+1)
    print(ss)



# voteToUp("cc")
# voteToDown("cc")

    
