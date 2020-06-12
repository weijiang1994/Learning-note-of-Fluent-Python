"""
@Time    : 2020/6/12 10:03
@Author  : weijiang
@Site    : 
@File    : 9对对象进行切片.py
@Software: PyCharm
"""
"""
我们可以通过s[a:b:c],对s序列从a-b间隔c来进行取值
"""

s = 'bicycle'

# 序列间隔3取值
print('s[::3]=', s[::3])

# 序列反序间隔1取值
print('s[::-1]=', s[::-1])

# 序列反序间隔2取值
print('s[::-2]=', s[::-2])
