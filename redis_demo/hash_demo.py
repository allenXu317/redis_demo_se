import redis
from time import sleep
import os


rd = redis.Redis(host="localhost",port="6379",decode_responses=True)

# 建立一个名为  listDemo 的列表
HASHTABLE = "hashtest"

splash = "---------------------------------------------------" + "\n"


# hset
alter = "HSET 在hash表里添加对应的 k-v 值"
print(alter)
cmd = "HSET %s name tom"%(HASHTABLE)
print(cmd)
rd.hset(HASHTABLE,"name","tom")
alter = "HGET 找到hash表里对应k的value值"
print(alter)
cmd = "HGET %s name"%(HASHTABLE)
print(cmd)
res = rd.hget(HASHTABLE,"name")
print(res)
print(splash)
# os.system("pause")
os.system("pause")


# HEXISTS 判断一个key值是否存在于一个hash表中
alter = "HEXISTS 判断一个key值是否存在于一个hash表中"
print(alter)
cmd = "HEXISTS %s name"%(HASHTABLE)
print(cmd)
res = rd.hexists(HASHTABLE,"name")
print(res)
alter = "当key不存在时"
cmd = "HEXISTS %s age"%(HASHTABLE)
print(cmd)
res = rd.hexists(HASHTABLE,"age")
print(res)
print(splash)
os.system("pause")


# HDEL 删除hash表中对应的k-v
alter = "HDEL 删除hash表中对应的k-v"
print(alter)
cmd = "HDEL %s name"%(HASHTABLE)
print(cmd)
rd.hdel(HASHTABLE,"name")
cmd = "HEXISTS %s name"%(HASHTABLE)
print(cmd)
res = rd.hexists(HASHTABLE,"name")
print(res)
print(splash)
os.system("pause")


# HLEN  hash表中保存的key的数量
alter = "HLEN  hash表中保存的key的数量"
print(alter)
cmd = "HSET %s name tom"%(HASHTABLE)
print(cmd)
cmd = "HSET %s age 18"%(HASHTABLE)
print(cmd)
cmd = "HSET %s sex female"%(HASHTABLE)
print(cmd)
rd.hset(HASHTABLE,"name","tom")
rd.hset(HASHTABLE,"age",18)
rd.hset(HASHTABLE,"sex","female")
cmd = "HLEN %s"%(HASHTABLE)
res = rd.hlen(HASHTABLE)
print(res)
print(splash)
os.system("pause")


# HKEYS 获得hash表中的所有key值
alter = "HKEYS 获得hash表中的所有key值"
print(alter)
cmd = "HKEYS %s"%(HASHTABLE)
print(cmd)
res = rd.hkeys(HASHTABLE)
print(res)
alter = "HVALS 获得hash表中的所有values值"
print(alter)
cmd = "HVALS %s"%(HASHTABLE)
print(cmd)
res = rd.hvals(HASHTABLE)
print(res)
print(splash)
os.system("pause")



# HGETALLS 获得hash中所有的K-v对
alter = "HGETALL 获得hash中所有的K-v对"
print(alter)
cmd = "HGETALL %s"%(HASHTABLE)
print(cmd)
res = rd.hgetall(HASHTABLE)
print(res)
print(splash)
os.system("pause")

print("哈希表演示完毕！")









