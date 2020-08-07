"""
@Time    : 2020/8/7
@Author  : jiangwei
@mail    : jiangwei1@kylinos.cn
@File    : 19使用双向队列
@Software: PyCharm
"""
from collections import deque

# 创建一个队列,maxlen表示该队列最大长度,可以不设置,一旦设置不可改变
dq = deque(range(10), maxlen=10)
print('dq ', dq)

# 队列旋转操作,接受一个参数n,当n>0时,队列的最右边的n个元素会被移动到队列的最左边,
# 当n<0时,队列最左边的n个元素会被移动到最左边
dq.rotate(3)
print('dq rotate 3 ', dq)
dq.rotate(-4)
print('dq rotate -4 ', dq)

# 在队列的左边添加一个元素,队列的头部(末尾)元素会被删除掉
dq.appendleft(-1)
print('dq append left -1 ', dq)

# 扩展队列元素,会删除掉队列的尾部(最前面)元素
dq.extend([11, 22, 33])
print('dq extend [11, 22, 33] ', dq)

# 将迭代器里的元素逐个添加到双向队列的坐标,因此迭代器里的元素会逆序出现在队列里面
dq.extendleft([10, 20, 30, 40])
print('dq extend left [10, 20, 30, 40] ', dq)
