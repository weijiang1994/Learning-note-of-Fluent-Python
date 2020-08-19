"""
# coding:utf-8
@Time    : 2020/8/18
@Author  : jiangwei
@mail    : jiangwei1@kylinos.cn
@File    : 3.__dict__的用法
@Software: PyCharm
"""


class Student:
    def __init__(self):
        self.age = None
        self.name = None
        self.gender = None


stu = Student()
print(stu.__dict__)
