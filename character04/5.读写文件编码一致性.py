"""
# coding:utf-8
@Time    : 2020/8/18
@Author  : jiangwei
@mail    : jiangwei1@kylinos.cn
@File    : 5.读写文件编码一致性
@Software: PyCharm
"""
import os
fp = open('./src/cafe.txt', 'w', encoding='utf8')
print(fp)
fp.write('café')
fp.close()
print(os.stat('./src/cafe.txt').st_size)

fp2 = open('./src/cafe.txt', encoding='1252')
print(fp2)
print(fp2.encoding)
print(fp2.read())

fp3 = open('./src/cafe.txt', encoding='utf-8')
print(fp3.encoding)
print(fp3)
print(fp3.read())

fp4 = open('./src/cafe.txt', 'rb')
print(fp4)
print(fp4.read())
