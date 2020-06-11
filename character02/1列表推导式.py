"""
@Time    : 2020/6/11 13:51
@Author  : weijiang
@Site    : 
@File    : sample2-1.py
@Software: PyCharm
"""
symbols = '$¢£¥€¤'
codes = []

for symbol in symbols:
    codes.append(ord(symbol))
print('原始拼接方式:', codes)


"""
不要滥用列表推导,通常原则下,只用列表推导来创建新的列表,并且尽量保持简短。
如果列表推导超过了两行,就可能需要考虑是否重新使用for循环进行重写了。
"""
codes = [ord(symbol) for symbol in symbols]
print('通过列表推导式:', codes)
