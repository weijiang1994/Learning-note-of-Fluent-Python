"""
@Time    : 2020/6/11 9:59
@Author  : weijiang
@Site    : 
@File    : sample1-2.py
@Software: PyCharm
"""
from math import hypot


class Vector:

    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y

    # print类实例不在以<class object --- at --->的形式输出,而已字符串进行输出,称作为'字符串表示形式'
    def __repr__(self):
        return 'Vector({},{})'.format(self.x, self.y)

    def __abs__(self):
        return hypot(self.x, self.y)

    def __bool__(self):
        return bool(abs(self))

    def __add__(self, other):
        x = self.x + other.x
        y = self.y + other.y
        return Vector(x, y)

    def __mul__(self, scalar):
        return Vector(self.x*scalar, self.y*scalar)


v1 = Vector(1, 2)
v2 = Vector(2, 2)

print('v1 + v2 = ', v1+v2)
print('v2 * 3 = ', v1*3)
print('abs(v1) = ', abs(v1+v2))
