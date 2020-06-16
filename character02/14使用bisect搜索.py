"""
@Time    : 2020/6/16 16:28
@Author  : weijiang
@Site    : 
@File    : 14使用bisect搜索.py
@Software: PyCharm
"""
import bisect
import sys

HAYSTACK = [1, 4, 5, 6, 8, 12, 15, 20, 21, 23, 23, 26, 29, 30]
NEEDLES = [0, 1, 2, 5, 8, 10, 22, 23, 29, 30, 31]
ROW_FMT = '{0:2d} @ {1:2d}  {2}{0:<2d}'


def demo(bisect_fn):
    for needle in reversed(NEEDLES):
        position = bisect_fn(HAYSTACK, needle)  # 计算needle插入的位置
        offset = position * '  |'
        print(ROW_FMT.format(needle, position, offset))  # 按格式输出


if __name__ == '__main__':
    if sys.argv[-1] == 'left':
        fn = bisect.bisect_left
    else:
        fn = bisect.bisect

    print('DEMO:', fn.__name__)
    print('haystack ->', ' '.join('%2d' % n for n in HAYSTACK))
    demo(fn)
