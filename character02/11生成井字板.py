"""
@Time    : 2020/6/12 16:50
@Author  : weijiang
@Site    : 
@File    : 11生成井字板.py
@Software: PyCharm
"""
# 采用列表推导生成正确的井字板
board = [['_']*3 for i in range(3)]
print(board)
board[1][2] = 'X'
print(board)

# 采用*生成错误的井字板
board = [['_']*3]*3
print(board)
board[1][2] = 'X'
print(board)
