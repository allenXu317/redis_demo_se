import redis
from time import sleep


# 连接redis
rd = redis.Redis(host="localhost",port="6379",decode_responses=True)
SETNAME = "testSDS"
splash = "---------------------------------------------------" + "\n"

# 字符串  set get strlen
alter = "用 set 存储一个键值对"
print(alter)
cmd = "SET %s a"%(SETNAME)
print(cmd)
rd.set(SETNAME,"abc")
alter = "get查看是否添加了键值对"
print(alter)
cmd = "GET %s"%(SETNAME)
print(cmd)
res = rd.get(SETNAME)
print("key为%s的值为:"%(SETNAME))
print(res)
alter = "strlen 查看存储的字符串的长度"
cmd = "STRLEN %s"%(SETNAME)
print(cmd)
res = rd.strlen(SETNAME)
print("存储字符串的长度为:%d"%(res))
print(splash)
sleep(10)



# append 追加
alter = "append 在 k-v 的v值后面追加内容"
print(alter)
cmd = "APPEND %s def"%(SETNAME)
print(cmd)
rd.append(SETNAME,"def")
alter = "追加操作后的结果:"
print(alter)
res = rd.get(SETNAME)
print(res)
print(splash)
sleep(10)


# incr incrby
alter = "INCR 将key对应的value解释成数字型并加一，如果解释失败，则返回一个错误"
print(alter)
cmd = "INCR %s"%(SETNAME)
print(cmd)
print("%s的值不能被解释为数字型，所以返回一个错误"%(SETNAME))
try:    
    res = rd.incr(SETNAME,1)
except redis.exceptions.ResponseError:
    print("incr 错误")
alter = "设置一个可以被解释成为数字的k-v对"
cmd = "SET %s 1"%(SETNAME+"num")
rd.set(SETNAME+"num","1")
cmd = "GET %s"%(SETNAME+"num")
print(cmd)
res = rd.get(SETNAME+"num")
print(res)
cmd = "INCR %s"%(SETNAME+"num")
print(cmd)
rd.incr(SETNAME+"num",1)
alter = "%s增加后的结果为:"%(SETNAME+"num")
print(alter)
cmd = "GET %s"%(SETNAME+"num")
print(cmd)
res = rd.get(SETNAME+"num")
print(res)
print(splash)
sleep(10)

# incrby 
alter = "incrby  可以增加指定的长度"
print(alter)
cmd = "INCRBY %s 2"%(SETNAME+"num")
print(cmd)
rd.incrby(SETNAME+"num",2)
cmd = "GET %s"%(SETNAME+"num")
res = rd.get(SETNAME+"num")
print(res)
print(splash)
sleep(10)

#decr  decrby 
alter = "decr decrby 也与 incr incrby 类似"
print(alter)
cmd = "DECR %s"%(SETNAME+"num")
print(cmd)
rd.decr(SETNAME+"num")
res = rd.get(SETNAME+"num")
print(res) 
cmd = "DECRBY %s 2"%(SETNAME+"num")
print(cmd)
rd.decrby(SETNAME+"num",2)
res = rd.get(SETNAME+"num")
print(res)
print(splash)
sleep(10)















