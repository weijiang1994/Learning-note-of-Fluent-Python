"""
@Time    : 2020/6/11 14:17
@Author  : weijiang
@Site    : 
@File    : 3笛卡尔积.py
@Software: PyCharm
"""
colors = ['black', 'white']
sizes = ['S', 'M', 'L']

tshirts = [(color, size) for color in colors for size in sizes]
print('按照颜色尺码排序:', tshirts)

tshirts = [(color, size) for size in sizes for color in colors]
print('按照尺码颜色排序:', tshirts)
