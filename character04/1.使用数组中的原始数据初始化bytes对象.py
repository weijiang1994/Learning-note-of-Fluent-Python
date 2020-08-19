"""
# coding:utf-8
@Time    : 2020/8/18
@Author  : jiangwei
@mail    : jiangwei1@kylinos.cn
@File    : 1.使用数组中的原始数据初始化bytes对象
@Software: PyCharm
"""
import array
# 指定类型代码h，创建一个短整数（16位）数组
numbers = array.array('h', [-2, -1, 0, 1, 2])
# octets保存组成numbers的字节序列的副本
octets = bytes(numbers)
print(octets)

# 表示5个短整数的10个字节
"""
b'\xfe\xff\xff\xff\x00\x00\x01\x00\x02\x00'
"""
