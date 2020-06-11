"""
@Time    : 2020/6/11 14:10
@Author  : weijiang
@Site    : 
@File    : 列表推导同filter和map的比较.py
@Software: PyCharm
"""
symbols = '$¢£¥€¤'
beyond_ascii = [ord(symbol) for symbol in symbols if ord(symbol) > 127]
print('通过列表推导:', beyond_ascii)

beyond_ascii = list(filter(lambda x: x > 127, map(ord, symbols)))
print('通过map、filter以及lambda表达式:', beyond_ascii)
