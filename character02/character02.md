### 2.1 内置序列类型概览

#### 可变序列

> list、bytearray、array.array、collections.deque 和memoryview

#### 不可变序列

> tuple、str 和bytes。

下图显示了可变序列`MutableSequence`和不可变序列`Sequence`的区别，同时也可以看出前者从后者哪里继承了一些方法。

![可变与不可变序列](.\image\可变不可变序列.PNG)

### 2.2 列表推导式

> 列表推导不会再出现变量泄露的问题
>
> 在Python2.x中输入以下代码会出现如下结果

```python
# python2.x环境下
x = 'my predicous'
dummy = [x for x in 'ABC']
print(x)
>>> 'C'
```

x的值被取代了，但是这种情况不会再Python3.x中出现了。

> 列表推导、生成器表达式以及同它们很相似的集合推导和字典推导，在Python3.x之后都有了自己的局部变量作用域，就像函数似的。表达式内部的变量和赋值只在局部起作用，表达式的上下文里的同名变量还可以被正常引用，局部变量并不会影响他们。

```python
x = 'ABC'
dummy = [ord(x) for x in x]
print(x) # ABC
print(dummy) # [65, 66, 67]
```

### 2.3 生成器表达式

> 虽然也可以用列表推导来初始化元组、数组或其他序列类型，但是生成器表达式是更好的选择。这是因为生成器表达式背后遵守了迭代器协议，可以逐个地产出元素，而不是先建立一个完整的列表，然后再把这个列表传递到某个构造函数里。前面那种方式显然能够节省内存。

生成器表达式的语法跟列表推导差不多，只不过把方括号换成圆括号而已。

```python
# 列表推导式
data = 'ABCDEFG'
[data for data in datas]

# 生成器表达式
(data for data in datas)
```

**生成器表达式不会一次生成一个完整的序列。**

### 2.4 元组

> 元组其实是对数据的记录：元组中的每个元素都存放了记录中一个字段的数据，外加这个字段的位置。正是这个位置信息给数据赋予了意义。
>
> 如果只把元组理解为不可变的列表，那其他信息——它所含有的元素的总数和它们的位置——似乎就变得可有可无。但是如果把元组当作一些字段的集合，那么数量和位置信息就变得非常重要了。

```python
lax_coordinates = (33.9425, -118.408056)
city, year, pop, chg, area = ('Tokyo', 2003, 32450, 0.66, 8014)
traveler_ids = [('USA', '31195855'), ('BRA', 'CE342567'), ('ESP', 'XDA205856')]

for passport in sorted(traveler_ids):
    print('%s/%s'%passport)

for country, _ in traveler_ids:
    print(country, '-', _)
```

#### 元组拆包

```python
name, age, birthday = ('zhangsan', 25, 1994) # 平行赋值
man = ('lisi', 25, 1985)
print('name is %s, age is %s, birthday is %s' %man)
# name is lisi, age is 25, birthday is 1985
```

上述两种方式均可叫做元组的拆包。

> 实际上拆包可以使用到任何可迭代对象上，唯一的硬性要求是，被可迭代对象中的元素数量必须跟接收这些元素的元组的空档数一直。除非我们使用`*`占位符忽略多余的元素。

我们可以通过*把一个可迭代对象拆开作为一个函数的参数

```python
divmod(20, 8) # (2, 4)
v = (20, 8)
divmod(*v) # (2, 4)
```

上述代码的输出结果一致。

**在我们进行拆包时候，我们可能对序列中的所有数值不感兴趣，可以使用占位符`_`来处理这种情况。**

#### 使用*来处理剩下元素

```python
datas = range(5)
a, b *rest = datas
print(a, b, rest) # (0, 1, [2, 3, 4])
a, *rest, b = datas
print(a, rest, b) # (0, [1, 2, 3], 4)
```

\*可以出现在平行赋值任何位置，会自动匹配\*变量要占几个变量。

### 2.5 具名元组

> `collections.namedtuple`是一个工厂函数，它可以用来构建一个带字段名的元组和一个有名字的类——这个带名字的类对调试程序有很大帮助。

用`namedtuple`构建的类的实例所消耗的内存跟元组是一样的，因为字段名都被存在对应的类里面。这个实例跟普通的对象实例比起来也要小一些，因为Python 不会用`__dict__` 来存放这些实例的属性。

#### 创建具名元组的流程

1. 创建一个具名元组需要两个参数，一个是类名，另一个是类的各个字段的名字。后者可以是由数个字符串组成的可迭代对象，或者是由空格分隔开的字段名组成的字符串。

2. 存放在对应字段李的数据要以一串参数的形式传入到构造函数当中(元组的构造函数却只接受单一的可迭代对象)
3. 通过字段名或者位置来获取一个字段的信息

```python
from collections import nametuple
Man = namedtuple('Man', 'name age gender three_circle')
ym = Man('YangMi', 34, 'female', (36, 78, 45))
# 通过字段名来获取字段信息
print(ym.name) # YangMi
# 通过索引来获取字段信息
print(ym[0]) # YangMi
# 支持迭代的方式获取信息
for info in ym:
    print(info)
```

#### 属性与方法

> 除了从普通元组那里继承来的属性之外，具名元组还有一些自己专有的属性。就展示了几个最有用的：`_fields` 类属性、类方法`_make(iterable)` 和实例方法`_asdict()`。

```python
# 接上一段代码
print(Man._fileds) # ('name', 'age', 'gender', 'three_circle')
ThrCir = namedtuple('ThrCir', 'xw, yw, tw')
lzl_data = ('Linzhiling', 45, 'female', ThrCir(36, 68, 43))
lzl = Man._make(lzl_data)
print(lzl._asdict()) 
'''
OrderedDict([('name', 'Linzhiling'), ('age', 45), ('gender', 'female'), ('three_circle', ThrCir(xw=36, yw=68, tw=43))])
'''
for key, value in lzl._asdict().items():
    print(key + ':' + str(value))
'''
name:Linzhiling
age:45
gender:female
three_circle:ThrCir(xw=36, yw=68, tw=43)
'''
```

1. `_fields`是一个包含这个类的所有字段名称的元组
2. `_make()`方法接受一个可迭代对象来生成这个类的实例,它的作用跟`Man(*lzl_data)`一样
3. `_asdict()`把具名元组以`collections.OrderDict`的形式返回，我们可以利用它来把元组里的信息友好地呈现出来。

### 2.6 切片

#### 切片忽略最后一个元素的好处

1. 只有最后一个位置信息，我们可以快速看出切片和区间有几个元素
2. 当起始位置信息都可见时，可以快速计算出切片区间长度`(start-stop)`
3. 我们可以使用任意index将序列分割为不重叠的两部分`data[:x]` `data[x:]`

#### 对对象进行切片

> 除了使用`s[a:b]`进行切片外，我们还可以使用`s[a:b:c]`对于序列s在a到b之间，间隔c取值。

```python
s = 'bicycle'
s[::3]  # 'bye'
s[::-1] # 'elcycib'
s[::-2] # eccb
```

#### 给切片赋值

> 如果把切片放在赋值语句的左边，或把它作为del操作的对象，我们就可以对序列进行嫁接、切除或就地修改操作。

```python
l = list(range(10))

print('原始序列:', l) # 原始序列: [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

l[2:5] = [20, 30]
print('切片赋值操作之后的序列:', l) # 切片赋值操作之后的序列: [0, 1, 20, 30, 5, 6, 7, 8, 9]

del l[5:7]
print('del 操作之后的序列:', l) # del 操作之后的序列: [0, 1, 20, 30, 5, 8, 9]

l[3::2] = [11, 33]
print('切片赋值操作之后的序列:', l) # 切片赋值操作之后的序列: [0, 1, 20, 11, 5, 33, 9]
```

<kbd>note:</kbd>

> 需要注意的是，在给切片进行赋值操作的时候，等号右边必须是一个可迭代序列。

### 2.7 +和*的注意事项

> \+和\*都不会改变原有的操作对象，而是构建一个全新的序列。
>
> 在使用 `a*n`时需要注意，当a中的元素是对其他可变对象的引用的话，你得到的n个元素其实是三个索引，都同时指向一个列表。

```python
a = [[1,2,3]]
a = a * 3 # [[1,2,3],[1,2,3],[1,2,3]]

a[1].extend([4,5,6])
print(a)  # [[1,2,3,4,5,6],[1,2,3,4,5,6],[1,2,3,4,5,6]]
```

当我们需要建立嵌套着几个列表的列表，我们最好选择使用列表推导

譬如生成一个井字板方块：

```python
# 采用列表推导生成正确的井字板
board = [['_']*3 for i in range(3)]
print(board) # [['_', '_', '_'], ['_', '_', '_'], ['_', '_', '_']]
board[1][2] = 'X'
print(board) # [['_', '_', '_'], ['_', '_', 'X'], ['_', '_', '_']]

# 采用*生成错误的井字板
board = [['_']*3]*3
print(board) # [['_', '_', '_'], ['_', '_', '_'], ['_', '_', '_']]
board[1][2] = 'X'
print(board) # [['_', '_', 'X'], ['_', '_', 'X'], ['_', '_', 'X']]
```

**如果采用了*去生成，因为嵌套列表中的列表都指向一个列表，所以更改一个，全盘都更改了。**

### 2.8 序列的增量赋值

> 增量赋值运算符 `+=` `*=`取决于它们的第一个操作对象。

* `+=`其背后的特殊方法是 `__iadd__`,如果一个类没有实现该方法，那么会自动去调用`__add__`方法
* `*=`其背后的特殊方法是`__imul__`, 如果一个类没有实现该方法，那么会自动去调用`__mul__`方法
* 一般来说可变序列都实现了`__iadd__`方法

```python
l = [1, 2, 3]
print(id(l))  # 2199257719944

l *= 2
print(l)	  # [1, 2, 3, 1, 2, 3]
print(id(l))  # 2199257719944


t = (1, 2, 3)
print(id(t))  # 2199257662376

t *= 2	
print(t) 	  # (1, 2, 3, 1, 2, 3)
print(id(t))  # 2199255258984
```

**对于不可变序列进行重复的拼接操作，效率会很低，因为每次都有一个新对象，而解释器需要把原来对象中的元素先复制到新的对象里，然后再追加新的元素。因此两次的id不一致。**

####  关于 += 的谜题

```python
t=(1, 2, [30, 40])
t[2] += [50, 60]
```

<kbd>思考？</kbd>

上述代码会出现哪种结果呢？

a.t变成 `(1, 2, [30, 40, 50, 60])`

b.因为tuple不支持对它的元素赋值，所以会抛出异常

c.以上两个都不是

d.a和b都对

> 答案为d，两个都是对的？为什么抛出异常了，还会进行赋值呢？

我们可以通过`dis`查看`s[a] += b`的字节码，如下图所示

![查看s[a]+=b的字节码](.\image\s[a]+=b字节码查看.PNG)

1. `BINARY_SUBSCR`将s[a]的值存入栈顶
2. `INPLACE_ADD`执行加法操作，这一步可以完成，因为栈顶指向的是一个可变对象
3. `STORE_SUBSCR`这一步无法执行，因为元组是不可变的

<kbd>经验</kbd>

* 不要把可变对象放在元组里面
* 增量赋值不是一个原子操作，就如上面的代码虽然抛出了异常，但是还是完成了赋值操作
* 查看Python的字节码并不难，而且它对我们了解代码背后的运行原理机制十分有帮助

### 2.9 list.sort与sorted()

> `sort()`函数就地对序列进行修改返回值为`None`
>
> `sorted()`函数会创建一个新的序列作为返回值，不管传入的是可变还是不可变的，都会以列表的形式进行返回，不会修改原序列

我们在两个函数中都可以使用关键字`reverse`来表示升序或降序，当为`True`时候，会以降序进行结果输出。

**在`reverse`函数中，还可以使用`key`关键字参数，该参数为只接受一个参数的函数。**

```python
fruits = ['grape', 'raspberry', 'apple', 'banana']
print(sorted(fruits))  #1 ['apple', 'banana', 'grape', 'raspberry']
print(fruits) #2 ['grape', 'raspberry', 'apple', 'banana']

print(sorted(fruits, reverse=True)) #3 ['raspberry', 'grape', 'banana', 'apple']
print(sorted(fruits, key=len)) #4 ['grape', 'apple', 'banana', 'raspberry']
print(sorted(fruits, key=len, reverse=True)) 
#5 ['raspberry', 'banana', 'grape', 'apple']
fruits.sort()
print(fruits) #6 ['apple', 'banana', 'grape', 'raspberry']
```

1. `sorted()`会直接返回一个新的列表，根据字母升序排列方式
2. 由于采用的`sorted()`函数，原始序列不会发生改变
3. 根据字母降序排列
4. 根据长度进行升序排列
5. 根据长度进行降序排列
6. `sort()`函数会修改原始序列

### 2.10 bisect使用

> bisect模块主要包含有两个函数`bisect`和`insort`，两个函数都是利用二分查找算法在有序序列中查找或插入元素。

#### 使用bisect来搜索

```python
import bisect
import sys

HAYSTACK = [1, 4, 5, 6, 8, 12, 15, 20, 21, 23, 23, 26, 29, 30]
NEEDLES = [0, 1, 2, 5, 8, 10, 22, 23, 29, 30, 31]
ROW_FMT = '{0:2d} @ {1:2d}  {2}{0:<2d}'


def demo(bisect_fn):
    for needle in reversed(NEEDLES):
        position = bisect_fn(HAYSTACK, needle)  # 计算needle插入的位置
        offset = position * '  |'
        print(ROW_FMT.format(needle, position, offset))  # 按格式输出


if __name__ == '__main__':
    if sys.argv[-1] == 'left':
        fn = bisect.bisect_left
    else:
        fn = bisect.bisect

    print('DEMO:', fn.__name__)
    print('haystack ->', ' '.join('%2d' % n for n in HAYSTACK))
    demo(fn)
```

上述代码的输出结果如下图所示:

![](.\image\bisect搜索.png)

