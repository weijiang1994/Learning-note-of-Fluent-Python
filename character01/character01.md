#### 1.1 一摞Python风格的纸牌
> 我们可以通过collections模块中`namedtuple`来创建一个简单的类，该类中只包含有对象不含有方法和函数。

```python
import collections

class_name = collections.namedtuple('Card', ['rank', 'suit'])
```
##### 序列可以迭代
解释器需要迭代对象x时，会自动调用`iter(x)`方法。内置的`iter(x)`方法有以下作用

1. 检查对象是否实现了`__inter__`方法，如果实现了就调用它（也就是我们偶尔用到的特殊方法重载），获取一个迭代器。
2. 如果没有实现`iter()`方法， 但是实现了`__getitem__`方法，Python会创建一个迭代器，尝试按顺序（从索引0开始，可以看到我们刚才是通过s[0]取值）获取元素。
3. 如果尝试失败，Python抛出**TypeError**异常，通常会提示`TypeError: '***' object is not iterable`
任何Python序列都可迭代的原因是，他们都实现了`__getitem__`方法。其实，标准的序列也都实现了`__iter__`方法。

我们通过`__len__`和`__getitem__`两个特殊方法，FrenchDeck就跟Python的序列数据类一样。

##### for data in dats
当我们在对list或者元组进行迭代的时候，其内部就是使用的`iter(datas)`,而这个函数的背后就是`x.__iter__()`方法。

#### 1.2 Vector
`__repr__`它能把一个对象用字符串的形式表达出来以便辨认，这就是“字符串表示形式”。

`__repr__`与`__str__`的区别在于，后者是使用str()函数时被调用，或是在使用`print`函数进行打印一个对象的时候才被调用的，并且他返回的对终端用户更加友好。

如果你只想实现这两个特殊方法中的一个，`__repr__`是更好的选择，因为如果一个对象没有`__str__`函数，而且Python有需要调用的时候，解释器会用`__repr__`来代替。

#### 1.3 自定义的布尔值

默认情况下，我们自己定义的类的实例总被认为是真的，除非这个类对`__bool__ `或者`__len__` 函数有自己的实现。`bool(x) `的背后是调用`x.__bool__()` 的结果；如果不存在`__bool__ `方法，那么`bool(x) `会尝试调用`x.__len__()`。若返回0，则`bool `会返回**False**；否则返回**True**。

#### 1.4 特殊方法

**跟运算符无关的**

| 名称                     | 作用                                                         |
| ------------------------ | ------------------------------------------------------------ |
| 字符串\|字节序列表示形式 | `__repr__`、`__str__`、`__format__`、`__bytes__`             |
| 数值转换                 | `__abs__`、 `__bool__`、`__complex__` 、`__int__`、`__float__`、`__hash__`、`__index__` |
| 集合模拟                 | `__len__`、`__getitem__`、`__setitem__`、`__delitem__`、`__contains__` |
| 迭代枚举                 | `__iter__`、`__reversed__`、`__next__`                       |
| 可调用模拟               | `__call__`                                                   |
| 上下文管理               | `__enter__`、`__exit__`                                      |
| 实例创建和销毁           | `__new__`、`__init__`、`_del__`                              |
| 属性管理                 | `__getattr__`、`__getattribute__`、`__setattr__`、`__delattr__`、`__dir__` |
| 属性描述符               | `__get__`、`__set__`、`__delete__`                           |
| 跟类相关的服务           | `__prepare__`、`__instancecheck__`、`__subclasscheck__`      |

**跟运算符相关的**

| 名称               | 作用                                                         |
| ------------------ | ------------------------------------------------------------ |
| 一元运算符         | `__neg__` -、`__pos__`+、`__abs__`abs()                      |
| 众多比较运算符     | `__lt__` <、`__le__` <=、`__eq__` ==、`__ne__` !=、`__gt__` >、`__ge__` >= |
| 算术运算符         | `__add__` +、`__sub__` -、`__mul__` *、`__truediv__` /、`__floordiv__` //、`__mod__` %、`__divmod__` divmod()、`__pow__` ** 或pow()、`__round__` round() |
| 反向算术运算符     | `__radd__`、`__rsub__`、`__rmul__`、`__rtruediv__`、`__rfloordiv__`、`__rmod__`、<br/>`__rdivmod__`、`__rpow__` |
| 增量赋值算术运算符 | `__iadd__`、`__isub__`、`__imul__`、`__itruediv__`、`__ifloordiv__`、`__imod__`、<br/>`__ipow__` |
| 位运算符           | `__invert__` ~、`__lshift__` <<、`__rshift__` >>、`__and__` &、`__or__` |
| 反向位运算符       | `__rlshift__`、`__rrshift__`、`__rand__`、`__rxor__`、`__ror__` |
| 增量赋值位运算符   | `__ilshift__`、`__irshift__`、`__iand__`、`__ixor__`、`__ior__` |

#### 1.5 延伸阅读

对本章内容和本书主题来说，Python 语言参考手册里的“Data Model”一章（https://docs.python.org/3/reference/datamodel.html）是最符合规范的知识来源。

Alex Martelli 的《Python 技术手册（第2 版）》对数据模型的讲解很精彩。我写这本书的时候，《Python 技术手册》的最新版本是2006 年出版的，书里用的还是Python 2.5，但是Python 关于数据模型的概念并没有太大的变化，而书中Martelli 对属性访问机制的描述，应该是除了CPython 中的C 源码之外在这方面最权威的解释。Martelli 还是Stack Overflow上的高产贡献者，在他名下差不多有5000 条答案，你也可以去他的Stack Overflow 主页（http://stackoverflow.com/users/95810/alex-martelli）上看看。

David Beazley 著有两本基于Python 3 的书，其中对数据模型进行了详尽的介绍。一本是《Python 参考手册（第4 版）》8，另一本是与Brian K. Jones 合著的《Python Cookbook（第3版）中文版》。

由Gregor Kiczales、Jim des Rivieres 和Daniel G. Bobrow 合著的The Art of the Metaobject Protocol（ 又称AMOP，MIT 出版社，1991 年） 一书解释了元对象协议（metaobject protocol，MOP）的概念，而Python 数据模型便是对这一概念的一种阐释。

