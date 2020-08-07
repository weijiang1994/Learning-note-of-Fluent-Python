"""
@Time    : 2020/8/7
@Author  : jiangwei
@mail    : jiangwei1@kylinos.cn
@File    : 17使用数组
@Software: PyCharm
"""

from array import array
from random import random

floats = array('d', (random() for i in range(10**7)))

fp = open('./file/floats.bin', 'wb')
print(floats[-1])
floats.tofile(fp)
fp.close()

floats2 = array('d')
fr = open('./file/floats.bin', 'rb')
floats2.fromfile(fr, 10**7)
fr.close()
print(floats2[-1])
