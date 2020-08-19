"""
# coding:utf-8
@Time    : 2020/8/18
@Author  : jiangwei
@mail    : jiangwei1@kylinos.cn
@File    : 2.使用memoryview和struct查看gif图像的首部
@Software: PyCharm
"""
import struct
# 解包格式化，<表示小端，3s3s是两个3字节序列，HH是两个16位位二进制整数。
fmt = '<3s3sHH'
# 使用内存中的文件内容创建一个memoryview对象
with open('./src/test.gif', 'rb') as fp:
    img = memoryview(fp.read())
# 切换转换成一个memoryview对象
header = img[:10]
# 转换成字节序列，这里复制了10个字节
print(bytes(header))
# 拆包memoryview对象，得到一个元组
un_pack = struct.unpack(fmt, header)
print(un_pack)
# 释放memoryview所占用的内存
del header
del img
