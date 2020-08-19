#### 4.1 处理Unicode数据的方法

除了格式化方法外(`format`/`format_map`)和几个处理Unicode数据方法(包括`casefold、isdecimal、isidentifier、isnumeri、isprintable和encode`)之外,**str**类型的其他方法都支持`bytes`和`bytearray`类型.这就意味着,我们可以使用熟悉的字符串方法处理二进制序列,例如<kbd>endswith、replace、strip、translate、upper</kbd>等.只有少数几个方法是参数是bytes对象,而不是str对象.此外,如果正则表达式编译自二进制序列而不是字符串,re模块中的正则表达式函数也能处理二进制序列.

构建`bytes`和`bytearray`实例还可以调用各自的构造方法 ,传入下述参数

- 一个**str**对象和一个**encoding**关键字
- 一个可迭代对象,提供0-255之间的数值
- 一个整数,使用孔子杰创建对应长度的二进制序列
- 一个实现缓冲协议的对象(如bytes、bytearray、memoryview、array.array)，此时把源对象中的字节序列复制到新建的二进制序列中

<kbd>1.使用数组中的原始对象初始化bytes对象</kbd>

```python
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
```

使用缓冲类对象创建**byets**或**bytearray**对象时，始终复制源对象中的字节序列。与之相反，**memoryview**对象允许在二进制数据结构直接共享内存。如果想从二进制序列中提取结构化信息，**struct**模块是重要的工具。

#### 4.2 struct模块使用

**struct**模块提供了一些函数，把打包的字节序列转换成不同类型字段组成的元组，还有一些函数用于执行反向转换，把元祖转换成打包的字节序列。**struct**模块能处理`bytes、bytearray、memoryview`对象。

<kbd>memoryview类</kbd>

> 不是用于创建或存储字节系列的，而是共享内存，让你访问其他二进制序列、打包的数组和缓冲中的数据切片，而无需复制字节序列。例如python中的PIL模块就是这么处理图像的。

<kbd>2.使用memoryview和struct查看一个GIF图像的首部</kbd>

```python
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
```

<kbd>Note:</kbd>

> memoryview对象的切片是一个memoryview对象，而且不会复制字节序列。

#### 4.3 编码问题

虽然有一个一般性的UnicodeError异常，但是报告错误时几乎都会指明具体的异常：UnicodeError（把字符串转换成二进制序列时）或UnicodeDecodeError（把二进制序列转换成字符串时）。如果源码的编码与预期不符，加载Python模块时还可能跑出SyntaxError。

<kbd>3.编码字节序列错误处理</kbd>

```python
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
```

> 编解码器的错误处理方式是可扩展的。你可以为errors参数注册额外的字符串，方法是把一个名称和一个错误处理函数传给`codecs.register_error`函数。参见`codecs.register_error`函数的文档（http://docs.python.org/2/library/codecs.html#codecs.register_error）

<kbd>4.解码字节序列错误处理</kbd>

```python
octets = b'Montr\xe9al'
octets.decode('cp1252')
octets.decode('iso8859_7')
octets.decode('koi8_r')
octets.decode('utf-8', errors='ignore')
octets.decode('utf-8', errors='replace')
```

#### 4.4 处理文本文件

<kbd>5.读写文件编码一致性</kbd>

```python
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
```

