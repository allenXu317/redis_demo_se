import redis
from time import sleep


rd = redis.Redis(host="localhost",port="6379",decode_responses=True)
SETNAME = "testSET"
SETNAME_2 = "ssss"
splash = "---------------------------------------------------" + "\n"



# sadd
alter = "sadd 将元素保存到集合key 中，若元素已存在则不会重复添加"
print(alter)
cmd = "SADD SETNAME item1 item2 item3"
print(cmd)
rd.sadd("SETNAME","item1","item2","item3")
alter = "SMEMBERS 返回key集合的全部成员"
cmd = "SMEMBERS SETNAME"
print(cmd)
res = rd.smembers("SETNAME")
print(res)
print(splash)
sleep(10)

# srem ----  移除元素
alter = "从集合中删除 item3 元素"
print(alter)
cmd = "SREM SETNAME item3"
print(cmd)
rd.srem("SETNAME","item3")
cmd = "SMEMBERS SETNAME"
print(cmd)
res = rd.smembers("SETNAME")
print(res)
print(splash)
sleep(10)


# 集合的交集
alter = "SINTER 寻找多个集合之间的交集"
print(alter)
cmd = "SADD SETNAME_2 item1 item2 item3 item4"
print(cmd)
rd.sadd("SETNAME_2","item1","item2","item3","item4")
cmd = "SEMEBERS SETNAME_2"
print(cmd)
res = rd.smembers("SETNAME_2")
print(res)
cmd = "SMEMBERS SETNAME"
print(cmd)
res = rd.smembers("SETNAME")
print(res)
alter = "找到 SETNAME 和 SETNAME_2 集合之间的交集"
print(alter)
cmd = "SINTER SETNAME SETNAME_2"
res = rd.sinter("SETNAME","SETNAME_2")
print(res)
print(splash)
sleep(10)


# 集合的差集
alter = "SDIFF key1 key2 key3 可以找到key1 集合中的独有元素"
print(alter)
cmd = "SDIFF SETNAME SETNAME_2"
print(cmd)
res = rd.sdiff("SETNAME","SETNAME_2")
print(res)
sleep(5)
cmd = "SDIFF SETNAME_2 SETNAME"
print(cmd)
res = rd.sdiff("SETNAME_2","SETNAME")
print(res)
print(splash)
sleep(10)

# 集合的并集
alter = "SUNION 可以找到多个集合之间的并集"
print(alter)
cmd = "SUNION SETNAME SETNAME_2"
print(cmd)
res = rd.sunion("SETNAME","SETNAME_2")
print(res)
print(splash)
sleep(10)


print("集合演示完毕")


















