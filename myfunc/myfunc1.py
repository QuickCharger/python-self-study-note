#!/usr/bin/evn python3
# -*- coding: utf-8 -*-

' a test module'

__author__ = "bdgboss"

def my_abs(x):
	if x >= 0:
		return x
	else:
		return 0 - x


def calc(*numbers):
	sum = 0
	for n in numbers:
		sum = sum + n * n;
	return sum


#标准测试代码
if __name__ == "__main__":
	import sys
	print("module", sys.argv[0], "begin")
	print(my_abs(-1))
	print(calc(*(1,2,3,4)))
	print("module", sys.argv[0], "end")
