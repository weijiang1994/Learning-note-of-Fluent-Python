"""
@Time    : 2020/8/7
@Author  : jiangwei
@mail    : jiangwei1@kylinos.cn
@File    : 18使用memory
@Software: PyCharm
"""
from array import array
numbers = array('h', [-2, -1, 0, 1, 2])
# 创建一个含有5个有符号短整型memoryview
memv = memoryview(numbers)
print(len(memv))
print(memv[0])

# 创建一个无符号的memoryview
memv_oct = memv.cast('B')
print(memv_oct.tolist())
memv_oct[5] = 4
print(numbers)
