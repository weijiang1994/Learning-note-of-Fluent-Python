"""
@Time    : 2020/6/17 14:02
@Author  : weijiang
@Site    : 
@File    : 16使用bisect插入新元素.py
@Software: PyCharm
"""
import bisect
import random

SIZE = 7

random.seed(1729)

my_list = []
for i in range(SIZE):
    new_item = random.randrange(SIZE * 2)
    bisect.insort(my_list, new_item)
    print('%2d ->' % new_item, my_list)
