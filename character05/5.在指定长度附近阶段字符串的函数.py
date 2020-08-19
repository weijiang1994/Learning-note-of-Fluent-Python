"""
# coding:utf-8
@Time    : 2020/8/19
@Author  : jiangwei
@mail    : jiangwei1@kylinos.cn
@File    : 5.在指定长度附近阶段字符串的函数
@Software: PyCharm
"""
from inspect import signature


def clip(text: str, max_length: 'int>0' = 80) -> str:
    """
    在max_length前面或后面第一个空格处截断文本
    :param text: 原始文本
    :param max_length: 截断处
    :return:
    """
    end = None
    if len(text) > max_length:
        space_before = text.find(' ', 0, max_length)
        if space_before >= 0:
            end = space_before
        else:
            space_after = text.rfind(' ', max_length)
            if space_after >= 0:
                end = space_after
        if end is None:
            end = len(text)
        return text[:end].rstrip()


print(clip.__defaults__)  # (80,)
# <code object clip at 0x7f8e6659c0c0, file "/home/jiangwei/python/Learning-note-of-Fluent-Python/character05/5
# .在指定长度附近阶段字符串的函数.py", line 12>
print(clip.__code__)
print(clip.__code__.co_varnames)  # ('text', 'max_length', 'end', 'space_before', 'space_after')
print(clip.__code__.co_argcount)  # 2
print(clip.__annotations__)

# 使用inspect模块
sig = signature(clip)
print(sig)  # (text, max_length=80)
str(sig)

for name, param in sig.parameters.items():
    """
    POSITIONAL_OR_KEYWORD : text = <class 'inspect._empty'>
    POSITIONAL_OR_KEYWORD : max_length = 80 
    """
    print(param.kind, ':', name, '=', param.default)

# 注解相关信息
for param in sig.parameters.values():
    note = repr(param.annotation).ljust(13)
    print(note, ':', param.name, '=', param.default)
