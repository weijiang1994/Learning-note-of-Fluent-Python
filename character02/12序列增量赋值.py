"""
@Time    : 2020/6/16 10:46
@Author  : weijiang
@Site    : 
@File    : 序列增量赋值.py
@Software: PyCharm
"""
l = [1, 2, 3]
print(id(l))


l *= 2
print(l)
print(id(l))


t = (1, 2, 3)
print(id(t))


t *= 2
print(t)
print(id(t))
