"""
@Time    : 2020/8/7
@Author  : jiangwei
@mail    : jiangwei1@kylinos.cn
@File    : 2.使用字典推到式
@Software: PyCharm
"""
dict_cells = [(86, 'China'), (91, 'India'), (1, 'United State'),
              (81, 'Japan'), (7, 'Russia')]

country_num = {con: code for code, con in dict_cells}
print(country_num)
