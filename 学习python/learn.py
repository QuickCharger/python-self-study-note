#!/usr/bin/env python3
# -*- coding: utf-8 -*-


#etc.
print("\netc")
print("10/3  = ", 10/3)
print("10//3 = ", 10//3)
print("before ", b'\xe4\xb8\xad\xe6\x96\x87'.decode("utf8"), ". after", "中文".encode("utf-8"))
print("\"qwer\" is str ?", isinstance("qwer", str))		#可以判断继承关系 isinstance(父类实例, 子类名称)=>true
print("\"qwer\" is str? ", type("qwer") == str)			#不能判断继承关系
print("str has func: ", dir(str))
	#浅复制 & 深复制
print("浅复制 & 深复制")
shoplist = ['apple', 'mango', 'carrot' , 'banana' ]
shoplist2 = shoplist
shoplist3 = shoplist[:]
shoplist.pop(0)
print("after shoplist.pop(0): ", shoplist)
print("shoplist2: ", shoplist2)
print("shoplist3: ", shoplist3)
exec(r'print("hello")')			#执行字符串


#IO, file, os, dump, json
print("\nIO, file, os, dump")
print("print(\"hello\", \"world\") 输出 ", "\"hello", "world\"", "逗号会替换为空格")
print(r'这是一个不带转义输出的范例" \" \r \n')
#i = input("输入")
print("print int %d. print float %f. print string %s. print %%x %x" %(1, 2, 3, 10))

try:
	context = '''\
This is a test file
测试文档
'''
	f = open("./tmp.txt", "w", encoding = "utf-8")
	f.write(context)
finally:
	if f:
		f.close()
print("测试写文件	ok")

try:
	f = open("./tmp.txt", "r", encoding = "utf-8")
	print(f.read().strip())
	f.seek(0)
	for line in f.readlines():
		print(line.strip())		#去掉结尾换行符
finally:
	if f:
		f.close()
print("测试读文件	ok")

with open("./tmp.txt", "r", encoding = "utf-8") as f:	#此方法读写都不需要写close(), 更简易
	for line in f.readlines():
		print(line.strip())
print("测试读文件	ok")

import os
print("当前路径: ", os.path.abspath("."))
tmpPath = os.path.join(os.path.abspath("."), "tmp")	#此方法创建的路径可以正确添加不同平台下的分隔符
print("创建目录: ", tmpPath)
os.mkdir(tmpPath)
print("移除目录: ", tmpPath)
os.rmdir(tmpPath)
print("当前路径下包含目录: ", [x for x in os.listdir(".") if os.path.isdir(x)])
print("当前路径下包含py文件: ", [x for x in os.listdir(".") if os.path.isfile(x) and os.path.splitext(x)[1]==".py"])

import pickle
with open("dump.file", "wb") as f:
	pickle.dump(context,f)
	print("dump finish")
with open("dump.file", "rb") as f:
	d = pickle.load(f)
	print("load finish. context: ", d.strip())

import json
context = {"name" : "qwer", "age" : 20, "score" : 30}
jsonContext = json.dumps(context)
print("after json: ", jsonContext)
context = json.loads(jsonContext)
print("after json parsed: ", context)


# list dict
print("\nlist dict")
classmates = ["qwer", "asdf", "zxcv"]
print("classmates size: ", len(classmates), ". first mate:", classmates[0], ". last mate:", classmates[-1])
classmates.append("abc");
classmates.insert(1, "defg");
print("after \"abc\" append \"def\" insert into classmates: ", classmates)
classmates.pop(0)
print("after pop[0]. ", classmates)
classmates[1] = "hij"
print("after classmates[1]=\"hij\"", classmates)
classmates.remove("hij")
print("after remove hij classmate:", classmates)

names = {"qwer":12, "asdf":23, "zxcv":34}
print("qwer age ", names["qwer"])
names.pop("asdf")
print("after names pop asdf", names)


# 条件判断 循环
print("\n条件判断 循环")
i = "123"
if(i == "123"):
	print("i is ", i)
elif(i == "234"):
	print("i is ", "234")
else:
	print("unknown i") 

for name in classmates:
	print("classmates has ", name)

abc = {"a":"A", "b":"B", "c":"C"}
for k, v in abc.items():
	print(k, "=", v)

sum = 0
for x in [1,2,3,4,5]:
	sum = sum + x
print("sum ", sum)

	#列表生成器，内部数据立即生成
L = [x*x for x in range(1, 11)]
print(L)
L = [x*x for x in range(1, 11) if x %2 != 0]
print(L)
L = [m + n for m in "qwer" for n in "asdf"]
print(L)
L = [k + "=" + v for k, v in abc.items()]
print(L)
	#生成器，与列表生成器的语法其别在于[]替换为()，其内部数据不是立即生成
G = (x*x for x in range(1, 11))
print("next G", next(G))	#next 在超出元素范围时会出错，建议用下方的for
print("next G", next(G))
print("next G", next(G))
for n in G:
	print(n)


#func
print("\nfunc")
print("int(\"123\") = %d\tint(123.45) = %d\tstr(123.45) = " %(int("123"), int(123.45)), str(123.45))

from myfunc.myfunc1 import my_abs
print("my_abs(-1) = %d" %my_abs(-1))

from myfunc.myfunc1 import calc
print("%d" %calc(1,2,3,4))

	#lambda 只能有一个表达式, 不能写return，返回值就是该表达式的结果
f = lambda x: x * x
print("lambda test 1 ", f(5))

def build(x,y):
	return lambda: x * x + y * y
print("lambda test 2 ", build(1,3)())

	#偏函数, 第二个参数或更多参数作为默认参数传递给函数, 默认参数放在参数列表的最左侧
import functools
int2 = functools.partial(int, base=2)
	#以下调用相当于
	#kw={"base":2}
	#int("1000", **kw)
print("func partial test 1 ", int2("1000"))
	#以下调用相当于
	#kw={"base":2, "base":10}
	#int("1000", **kw)
print("func partial test 2 ", int2("1000", base=10))
	#以下调用相当于
	#kw=(10,1,2,3,4)
	#print(max(*kw))
max2 = functools.partial(max, 10)
print("func partial test 3 ", max2(1,2,3,4))


# try ... except ... finally ... & logging
print("\ntry ... except ... finally ...")
try:
	print("try ... ")
	a = 10/0
	# 错误类型可参考 https://docs.python.org/3/library/exceptions.html#exception-hierarchy
except ZeroDivisionError as e:
	print("ZeroDivisionError: ", e)
finally:
	print("try ... finish")

def testErr2():
	raise ZeroDivisionError('抛给调用者一个错误，直至被捕获')
def testErr1():
	testErr2()
try:
	testErr1()
except ZeroDivisionError as e:
	print("ZeroDivisionError: ", e)
finally:
	print("try ... finish")

import logging
logging.basicConfig(level=logging.DEBUG,	#控制台打印的日志级别
	filename='new.log',
	filemode='a',		#a追加 w覆盖，默认a
	format='%(asctime)s - %(pathname)s[line:%(lineno)d] - %(levelname)s: %(message)s'
)
n = 10
logging.debug("n = %d" %n)
logging.info("n = %d" %n)
logging.warning("n = %d" %n)
logging.error("n = %d" %n)

