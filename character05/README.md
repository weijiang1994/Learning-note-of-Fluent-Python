#### 5.1 高阶函数
> 接收函数作为参数，或者把函数做为返回值的函数就是高阶函数`map`就是属于高阶函数。

<kbd>1.高阶函数示例</kbd>

```python
fruits = ['strawberry', 'fig', 'apple', 'cherry', 'raspberry', 'banana']
res = sorted(fruits, key=len)
print(res)

def reverse(word):
    return word[::-1]

res = sorted(fruits, key=reverse)
print(res)
```

#### 5.2 all 与 any

1. all(iterable)

   如果iterable的每个元素都是真值，则返回True；特别的all([])返回True。

2. any()

   只要iterable中有元素是真值，就返回True；特别的any([])返回Fasle。

#### 5.3 函数内省

使用dir()函数可以知道函数具有哪些属性。

其中，大多数属性都是Python对象共有的。

函数可以通过\__dict__来获取赋予它的用户属性，如下示例

```python
def func():
    pass
func.short_name = 'fun'
func.__dict__
>>>{'short_name': 'fun'}
```

同样的类也可以通过\__dict__属性来获取类属性。

```python
class Student:
    def __init__(self):
        self.age = None
        self.name = None
        self.gender = None
        
stu = Student()
print(stu.__dict__)class Student:
    def __init__(self):
        self.age =language None
        self.name = None
        self.gender = None


stu = Student()
print(stu.__dict__)
```

#### 5.4从定位参数到仅限关键字参数

Python最好的特性之一就是提供了极为灵活的参数处理机制，而且Python3进一步提供了仅限关键字参数。与之密切相关的是，调用函数时使用`*`和`**`展开可迭代独享，映射到单个参数中。

<kbd>4.使用可变参数生成HTML标签</kbd>

```python
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
```

#### 5.5获取关于参数的信息

函数对象有一个`__default__`属性，它的值是一个元组，里面保存着定位参数和关键字参数的默认值。仅限关键字参数的默认在`__kwdefault__`属性中。然而，参数的名称在`__code__`属性中，它的值是一个code对象引用，自身也有很多属性。

同时可以通过`inspect`模块来获取函数确却的参数信息，示例如下代码所示：

```python
from inspect import signature


def clip(text, max_length=80):
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
```

<kbd>Note:</kbd>

> 上述代码中，`kind`属性的值是`_ParameterKind`类中五个值之一
>
> - POSITIONAL_OR_KEYWORD
>
>   可以通过定位参数和关键字参数传入的形参（多数Python函数的参数属于此类）
>
> - VAR_POSITIONAL
>
>   定位参数元组
>
> - VAR_KEYWORD
>
>   关键字参数字典
>
> - KEYWORD_ONLY
>
>   仅限关键字参数
>
> - POSITIONAL_ONLY
>
>   仅限定位参数；目前Python声明函数的语法不支持，但是有些使用C语言实现不接受关键字参数的函数（如dzhichiivmod）支持。

除了name、default和kind，inspect.Parameter对象还有一个`annotation`（注解）属性，它的值通常是`inspect._empty`，但是可能包含有Python3新的注解句法提供的函数签名元数据。

#### 5.6函数注解

由于Python属于静态类型语言，在运行时不会自动检查函数的参数类型，通过添加函数注解可以提高代码的可读性，重构更加快捷。

<kbd>Note</kbd>

```python
def test_annotation(text: str, times: int) -> None:
    print(text)
    print(int)
```

#### 5.7支持函数式编程的包

1. operator模块

   