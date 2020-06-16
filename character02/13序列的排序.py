"""
@Time    : 2020/6/16 16:02
@Author  : weijiang
@Site    : 
@File    : 序列的排序.py
@Software: PyCharm
"""
fruits = ['grape', 'raspberry', 'apple', 'banana']
print(sorted(fruits))
print(fruits)

print(sorted(fruits, reverse=True))
print(sorted(fruits, key=len))
print(sorted(fruits, key=len, reverse=True))
fruits.sort()
print(fruits)
