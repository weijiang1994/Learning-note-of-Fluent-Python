"""
# coding:utf-8
@Time    : 2020/8/18
@Author  : jiangwei
@mail    : jiangwei1@kylinos.cn
@File    : 1.高阶函数示例
@Software: PyCharm
"""
fruits = ['strawberry', 'fig', 'apple', 'cherry', 'raspberry', 'banana']
res = sorted(fruits, key=len)
print(res)


def reverse(word):
    return word[::-1]


res = sorted(fruits, key=reverse)
print(res)
