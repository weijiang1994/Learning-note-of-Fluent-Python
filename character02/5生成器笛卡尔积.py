"""
@Time    : 2020/6/11 14:47
@Author  : weijiang
@Site    : 
@File    : 5生成器笛卡尔积.py
@Software: PyCharm
"""
colors = ['black', 'white']
sizes = ['S', 'M', 'L']

for tshirt in ((color, size) for size in sizes for color in colors):
    print(tshirt)
