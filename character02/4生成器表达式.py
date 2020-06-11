"""
@Time    : 2020/6/11 13:51
@Author  : weijiang
@Site    : 
@File    : sample2-1.py
@Software: PyCharm
"""
import array
symbols = '$¢£¥€¤'

codes = (ord(symbol) for symbol in symbols)
print('通过生成器表达式:', tuple(codes))

codes = array.array('I', (ord(symbol) for symbol in symbols))
print('通过生成器表达式:', codes)
