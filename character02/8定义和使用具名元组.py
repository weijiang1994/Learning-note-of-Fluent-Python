"""
@Time    : 2020/6/11 15:50
@Author  : weijiang
@Site    : 
@File    : 8定义和使用具名元组.py
@Software: PyCharm
"""
from collections import namedtuple

City = namedtuple('City', 'name country population coordinates')
tokyo = City('Tokyo', 'JP', 36.933, (35.689722, 139.691667))

print(tokyo)

print(City._fields)  # 获取类中的属性

LatLong = namedtuple('LatLong', 'lat long')
delhi_data = ('Delhi NCR', 'IN', 21.935, LatLong(28.613889, 77.208889))

delhi = City._make(delhi_data)  # 通过一个可迭代对象来生成这个类的实例,它的作用跟City(*delhi_data)一样
print(delhi._asdict())
for key, value in delhi._asdict().items():
    print(key + ':', value)


Man = namedtuple('Man', 'name age gender three_circle')
ym = Man('YangMi', 34, 'female', (36, 78, 45))
print(ym)

print(Man._fields)

ThrCir = namedtuple('ThrCir', 'xw, yw, tw')
lzl_data = ('Linzhiling', 45, 'female', ThrCir(36, 68, 43))
lzl = Man._make(lzl_data)
print(lzl._asdict())
for key, value in lzl._asdict().items():
    print(key + ':' + str(value))
