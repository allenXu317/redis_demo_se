import redis
from time import sleep



rd = redis.Redis(host="localhost",port="6379",decode_responses=True)

# 建立一个名为  listDemo 的列表
LISTNAME = "listDemo"

splash = "---------------------------------------------------" + "\n"

# 利用 LPUSH 从列表头部插入a,b,c,d,e,f,g
alert = "利用 LPUSH 从列表头部插入a,b,c,d,e,f,g"
cmd = "LPSUH listDemo a b c d e f g"
print(splash)
print(alert)
print(cmd)
rd.lpush(LISTNAME,"a","b","c","d","e","f","g")
alert = "利用 LRANGE 来查看结果"
print(alert)
print("LRANGE listDemo 0 1000")
test = rd.lrange(LISTNAME,0,1000)
print(test)
print(splash)
sleep(10)

# LLEN 获得列表长度
alert = "测试 LLEN 获得列表长度"
print(alert)
cmd = "LLEN listDemo"
res = rd.llen(LISTNAME)
print("列表"+LISTNAME+"的长度是: "+str(res))
print(splash)
sleep(5)


# 测试 LPUSHX  若指定的列表不存在则返回错误
alert = "测试 LPUSHX 向列表中插入 h "
print(alert)
print("此时测试的列表是:"+LISTNAME+"k")
cmd = "LPUSHX listDemok h"
print(cmd)
res = rd.lpushx(LISTNAME+"k","h")
print("此时测试的列表是:"+LISTNAME+"k"+" 结果是: "+ str(res))
print("此时测试的列表是:"+LISTNAME)
cmd = "LPUSHX listDemo h"
print(cmd)
res = rd.lpushx(LISTNAME,"h")
print("此时测试的列表是:"+LISTNAME+" 结果是: "+ str(res))
cmd = "LRANGE listDemo 0 1000"
print(cmd)
test = rd.lrange(LISTNAME,0,10000)
print(test)
print(splash)
sleep(10)

# 测试 RPUSH 
alert = "测试 RPUSH 向列表中插入 a b c d e f g"
cmd = "RPUSH listDemo a b c d e f g"
print(cmd)
rd.rpush(LISTNAME,"a","b","c","d","e","f","g")
cmd = "LRANGE listDemo 0 10000"
print(cmd)
res = rd.lrange(LISTNAME,0,10000)
print(res)
alert = "RPUSHX 与 LPUSHX 同理"
print(splash)

#测试 xPOP 命令
alert = "LPOP获得队列头部的元素:"
res = rd.lrange(LISTNAME,0,10000)
cmd = "LRANGE listDemo 0 10000"
print(cmd)
print(res)
print("此时的队列头部的元素是: "+res[0])
cmd = "LPOP listDemo"
print(cmd)
res = rd.lpop(LISTNAME)
print("弹出元素: "+res)
res = rd.lrange(LISTNAME,0,10000)
cmd = "LRANGE listDemo 0 10000"
print(cmd)
print("弹出后的结果为:")
print(res)
print(splash)
sleep(10)

alert = "RPOP获得队列头部的元素:"
res = rd.lrange(LISTNAME,0,10000)
cmd = "LRANGE listDemo 0 10000"
print(cmd)
print(res)
print("此时的队列尾部的元素是: "+res[len(res)-1])
cmd = "RPOP listDemo"
print(cmd)
res = rd.rpop(LISTNAME)
print("弹出元素: "+res)
res = rd.lrange(LISTNAME,0,10000)
cmd = "LRANGE listDemo 0 10000"
print(cmd)
print("弹出后的结果为:")
print(res)
print(splash)
sleep(10)


# RPOPLPUSH 测试
alert = "RPOPLPUSH 将列表元素从尾部移除，并放到列表头部"
cmd = "LRANGE listDemo 0 10000"
print(cmd)
res = rd.lrange(LISTNAME,0,10000)
print(res)
cmd = "RPOPLPUSH listDemo listDemonew"
print(cmd)
rd.rpoplpush(LISTNAME,LISTNAME)
cmd = "LRANGE listDemo 0 10000"
print(cmd)
res = rd.lrange(LISTNAME,0,10000)
print(res)
print(splash)
sleep(10)


# LREM 删除元素:
alter = "LREM 从列表的队头开始，最多找到count个value为止，并将他们移除出队列"
cmd = "LRANGE listDemo 0 10000"
print(cmd)
res = rd.lrange(LISTNAME,0,10000)
print(res)
cmd = "LREM listDemo 5 a"
print(cmd)
rd.lrem(LISTNAME,5,"a")
cmd = "LRANGE listDemo 0 10000"
print(cmd)
res = rd.lrange(LISTNAME,0,10000)
print(res)
print(splash)
sleep(10)

# LSET 插入元素
alert = "LSET 将value插入到key列表中索引为index的位置，超出范围或key列表为空则均返回错误"
print(alert)
cmd = "LSET lisTDemo 'INSERT'"
print(cmd)
rd.lset(LISTNAME,5,"INSERT")
cmd = "LRANGE listDemo 0 10000"
print(cmd)
res = rd.lrange(LISTNAME,0,10000)
print(res)
print(splash)
sleep(10)

print("列表演示完毕！")






