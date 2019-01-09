#!/usr/bin/env python3
# -*- coding: utf-8 -*-

'''
	约定俗成的规定
		_name 的成员变量表示私有
		__name 的成员变量表示特殊变量会被解释为_class__name
'''
class SchoolMember:
	population = 0
	def __init__(self, name, age):
		self._name = name
		self._age = age
		SchoolMember.population += 1
	def tell(self):
		print("Name:%s  Age:%d" %(self._name,self._age))

class Teacher(SchoolMember):
	def __init__(self, name, age, salary):
		SchoolMember.__init__(self, name, age)		#self必须要加
		self._salary = salary
		self.__salary_private = 10
	def tell(self):
		SchoolMember.tell(self)
		print("Salary:%d" %(self._salary))			#调用自身成员变量时，必须要加self

class Student(SchoolMember):
	def __init__(self, name, age, marks):
		SchoolMember.__init__(self, name, age)		#self必须要加
		self._marks = marks
	def tell(self):
		SchoolMember.tell(self)
		print("marks:%d" %(self._marks))			#调用自身成员变量时，必须要加self


class Student2(object):
	@property			# 设定读属性
	def score(self):
		return self._score

	@score.setter		# 设定写属性
	def score(self, value):
		if value < 0 or value > 100:
			raise ValueError("score must between 0~100")
		self._score = value


#标准测试代码
if __name__ == "__main__":
	t = Teacher("Mrs. Shrividya", 40, 30000)
	s = Student("Swaroop", 22, 75)
	t.a = 123
	print(t._salary)								# 不建议直接访问
	print(t._Teacher__salary_private)		# 不建议直接访问
	members = [t, s]
	for member in members:
		member.tell()
	print("total members: ", s.population)

	s = Student2()
	s.score = 60
	print(s.score)

