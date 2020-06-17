"""
@Time    : 2020/6/17 10:37
@Author  : weijiang
@Site    : 
@File    : 15根据分数找到对应成绩.py
@Software: PyCharm
"""
from bisect import bisect


def grade(score, breakpoints=[60, 70, 80, 90], grades='FDCBA'):
    i = bisect(breakpoints, score)
    return grades[i]


grade_level = [grade(score) for score in [89, 23, 78, 87, 91, 65]]
print(grade_level)
