import redis
from time import sleep


rd = redis.Redis(host="localhost",port="6379",decode_responses=True)

# 建立一个名为  listDemo 的列表
ZSETNAME = "rank"

splash = "---------------------------------------------------" + "\n"



# ZADD 向一个有序集合中加入 k-score 对应组合，zset根据score进行排序
alter = "ZADD 向一个有序集合中加入 k-score 对应组合，zset根据score进行排序"
print(alter)
cmd = "ZADD %s 10 tom 20 kim 30 jim"%(ZSETNAME)
print(cmd)
rd.zadd(ZSETNAME,{"tom":"10"})
rd.zadd(ZSETNAME,{"kim":"20"})
rd.zadd(ZSETNAME,{"jim":"30"})
alter = "ZCARD 返回有序集合的基数"
print(alter)
cmd = "ZCARD %s"%(ZSETNAME)
print(cmd)
res = rd.zcard(ZSETNAME)
print(res)
print(splash)
sleep(10)

#ZRANGE 排序   ----   score从小到大的顺序
#ZREVRANEG  排序    ----  score从大到小的顺序
alter = "ZRANGE 排序   score从小到大的顺序  显示从start 到 end的范围, end=-1代表倒数第一个,end=-2代表倒数第二个"
print(alter)
cmd = "ZRANGE %s 0 -1"%(ZSETNAME)
print(cmd)
res = rd.zrange(ZSETNAME,0,-1)
print(res)
cmd = "ZRANGE %s 0 -2"%(ZSETNAME)
print(cmd)
res = rd.zrange(ZSETNAME,0,-2)
print(res)
print(splash)
sleep(10)

alter = "ZREVRANGE 排序   score从小到大的顺序  显示从start 到 end的范围, end=-1代表倒数第一个,end=-2代表倒数第二个"
print(alter)
cmd = "ZREVRANGE %s 0 -1"%(ZSETNAME)
print(cmd)
res = rd.zrevrange(ZSETNAME,0,-1)
print(res)
cmd = "ZREVRANGE %s 0 -2"%(ZSETNAME)
print(cmd)
res = rd.zrevrange(ZSETNAME,0,-2)
print(res)
print(splash)
sleep(10)


# ZRANK 获得排名:
alter = "ZRANK 获得有序表中某个元素的具体排名,根据分数从小到大排名"
print(alter)
cmd = "ZRANK %s %s"%(ZSETNAME,"tom")
print(cmd)
res = rd.zrank(ZSETNAME,"tom")
print(res)
print(splash)
sleep(10)


# ZREVRANK 获得排名:
alter = "ZREVRANK 获得有序表中某个元素的具体排名,根据分数从大到小排名"
print(alter)
cmd = "ZREVRANK %s %s"%(ZSETNAME,"tom")
print(cmd)
res = rd.zrevrank(ZSETNAME,"tom")
print(res)
print(splash)
sleep(10)


print("有序集合演示完毕！")
