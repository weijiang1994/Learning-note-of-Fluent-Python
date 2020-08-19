"""
# coding:utf-8
@Time    : 2020/8/18
@Author  : jiangwei
@mail    : jiangwei1@kylinos.cn
@File    : 3.编码字节序列错误处理
@Software: PyCharm
"""
city = 'São Paulo'
city.encode('utf-8')
city.encode('utf-16')
city.encode('iso8859_1')

# 忽略不可编码字符错误
city.encode('cp437', errors='ignore')
# 不可编码字符替换为?
city.encode('cp437', errors='replace')
# 不可编码的字符替换为xml实体
city.encode('cp437', errors='xmlcharrefreplace')
