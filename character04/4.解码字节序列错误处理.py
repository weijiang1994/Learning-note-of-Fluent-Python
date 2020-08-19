"""
# coding:utf-8
@Time    : 2020/8/18
@Author  : jiangwei
@mail    : jiangwei1@kylinos.cn
@File    : 4.解码字节序列错误处理
@Software: PyCharm
"""
octets = b'Montr\xe9al'
octets.decode('cp1252')
octets.decode('iso8859_7')
octets.decode('koi8_r')
octets.decode('utf-8', errors='ignore')
octets.decode('utf-8', errors='replace')
