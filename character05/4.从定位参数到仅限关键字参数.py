"""
# coding:utf-8
@Time    : 2020/8/18
@Author  : jiangwei
@mail    : jiangwei1@kylinos.cn
@File    : 4.从定位参数到仅限关键字参数
@Software: PyCharm
"""
import inspect


def tag(name, *content, cls=None, **attrs):
    if cls is not None:
        attrs['class'] = cls

    if attrs:
        attr_str = ''.join('%s="%s"' % (attr, value)
                           for attr, value in sorted(attrs.items()))
    else:
        attr_str = ''
    if content:
        return '\n'.join(
            '<%s %s>%s</%s>' %
            (name, attr_str, c, name) for c in content)
    else:
        return '<%s %s/>' % (name, attr_str)


print(tag('p', 'hello'))
print(tag('p', 'hello', 'world'))
print(tag('p', 'hello', id=33))
print(tag('p', 'hello', 'world', cls='sidebar', id='sidebar'))

sig = inspect.signature(tag)
my_tag = {'name': 'img', 'title': 'Sunset Boulevard', 'src': 'sunset.jpg', 'cls': 'framed'}
bound_args = sig.bind(**my_tag)
print(bound_args)

del my_tag['name']

for name, value in bound_args.arguments.items():
    print(name, '=', value)

