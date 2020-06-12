"""
@Time    : 2020/6/12 16:13
@Author  : weijiang
@Site    : 
@File    : 10给切片赋值.py
@Software: PyCharm
"""
l = list(range(10))

print('原始序列:', l)
l[2:5] = [20, 30]

print('切片赋值操作之后的序列:', l)

del l[5:7]
print('del 操作之后的序列:', l)

l[3::2] = [11, 33]
print('切片赋值操作之后的序列:', l)
