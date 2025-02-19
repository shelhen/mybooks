# Python 标准库之 itertools 使用指南

### 0 前言

内建模块 itertools 实现了许多迭代器构建块，受到 APL、Haskell和 SML 等的启发，标准化了一个**快速**、**高效利用内存**的核心工具集，提供了用于操作迭代对象的函数，它们一起构成了一个“**迭代器代数（iterator algebra）**”，这使得在纯Python中有可能创建简洁又高效的专用工具。

使用 `next(迭代器)` 可以取得迭代器对象下一个生成的值。

### 1 无限迭代器 infinite iterators

#### count

参数：`itertools.count(start=0, step=1)`

用途：创建一个迭代器，它从 start 值开始，返回均匀间隔的值，即生成初始值为start，公差为step的等差数列。常用于 map() 中的实参来生成连续的数据点。此外，还用于 zip() 来添加序列号。

应用：

```python
python复制代码count(10)  # 10 11 12 13 ...
count(10, 0.5)  # 10 10.5 11 11.5 ...
# 注：浮点数计数时，通过下面的方法可以获得更好的准确性
(10 + 0.5 * i for i in count())  # 10.0 10.5 11 11.5 ...
map(lambda x: 2 * x**2 + 1, count())  #  1 3 9 19 33 51 ...
zip(count(), ['a', 'b', 'c'])  # [(0, 'a'), (1, 'b'), (2, 'c')]
```

#### cycle

参数：`itertools.cycle(iterable)`

用途：创建一个迭代器，返回 iterable 中所有元素并保存一个副本。当取完 iterable 中所有元素，返回副本中的所有元素。无限重复。

应用：

```python
python复制代码cycle(['a','b','c'])  # a b c a b c a ...
cycle(range(3))  # 0 1 2 0 1 2 0 ...
```

#### repeat

参数：`itertools.repeat(object, times=None)`

用途：创建一个迭代器，不断重复 object 。除非设定参数 times ，否则将无限重复。可用于 map() 函数中的参数，被调用函数可得到一个不变参数。也可用于 zip() 的参数以在元组记录中创建一个不变的部分。

应用：

```python
python复制代码repeat('abc')  # abc abc abc ...
repeat(range(3))  # range(0, 3) range(0, 3) range(0, 3) ...
repeat(1, 3)  # 1 1 1
map(pow, range(5), repeat(2))  # 0 1 4 9 16
zip(repeat('num'), [1,2,3])  # [('num', 1), ('num', 2), ('num', 3)]
```

### 2 有限迭代器 Iterators terminating on the shortest input sequence

#### accumulate

> Python 3.8 更改：添加了可选的 \*initial\* 形参

参数：`itertools.accumulate(iterable, func=operator.add, *, initial=None)`

用途：创建一个迭代器，返回累积汇总值或其他双目运算函数的累积结果值（通过可选的 *func* 参数指定）。通常，输出的元素数量与输入的可迭代对象是一致的。 但是，如果提供了关键字参数 *initial*，则累加会以 *initial* 值开始，这样输出就比输入的可迭代对象多一个元素。

应用：

```python
python复制代码accumulate([1,2,3,4,5])  # 1 3 6 10 15
accumulate([1,2,3,4,5], operator.mul)  # 1 2 6 24 120
accumulate([1,2,3,4,5], min)  # 1 1 1 1 1
accumulate([1,2,3,4,5], max)  # 1 2 3 4 5
accumulate([2,4,5,8,10], lambda x, _: 1/x)  # 2 0.5 2.0 0.5 2.0
accumulate([2,4,5,8,10], lambda _, x: 1/x)  # 2 0.25 0.2 0.125 0.1
accumulate([2,4,5,8,10], lambda x, y: x*y)  # 2 8 40 320 3200
# 注：functools.reduce() 只获得最终累积值
reduce(lambda x, y: x*y, [2,4,5,8,10])  # 3200
accumulate([1,2,3,4,5], initial=100)  # 100 101 103 106 110 115
```

#### chain

参数：`itertools.chain(*iterables)`

用途：创建一个迭代器，它首先返回第一个可迭代对象中所有元素，接着返回下一个可迭代对象中所有元素，直到耗尽所有可迭代对象中的元素。可将多个序列处理为单个序列。

应用：

```python
python复制代码chain([1,2], [3,4], [5])  # 1 2 3 4 5
chain([[1,2], [3,4], [5]])  # [[1, 2], [3, 4], [5]]
chain(*[[1,2], [3,4], [5]])  # 1 2 3 4 5
chain(['ABC', 'DEF'])  # ABC DEF
chain(*['ABC', 'DEF'])  # A B C D E F
```

#### chain.from_iterable

参数：`itertools.chain.from_iterable(iterable)`

用途：从一个单独的可迭代参数中得到链式输入，该参数是延迟计算的。

应用：

```python
python复制代码chain.from_iterable([1,2], [3,4], [5])  # Error
chain.from_iterable([[1,2], [3,4], [5]])  # 1 2 3 4 5
chain.from_iterable(*[[1,2], [3,4], [5]])  # Error
chain.from_iterable(['ABC', 'DEF'])  # A B C D E F
chain.from_iterable(*['ABC', 'DEF'])  # Error
```

#### compress

参数：`itertools.compress(data, selectors)`

用途：创建一个迭代器，它返回 *data* 中经 *selectors* 真值测试为 `True` 的元素。迭代器在两者较短的长度处停止。目的在于用另一个相关序列过滤当前序列。

应用：

```python
python复制代码compress('ABCDEF', [1,0,1,0,1,1])  # A C E F
compress('ABCDEF', [1])  # A
compress('ABCDEF', [True, -1, 1, 0.5, 'C', [1]])  # A B C D E F
compress('ABCDEF', [False, 0, 0.0, '', [], None])  # (Empty)
# 注：布尔值为False的包括 [0, -0, 0.0, 0j, [], (), {}, None, ""] 等
```

#### dropwhile

参数：`itertools.dropwhile(predicate, iterable)`

用途：创建一个迭代器，如果 *predicate* 为true，迭代器丢弃这些元素，然后返回其他元素。注意，迭代器在 *predicate* 首次为false之前不会产生任何输出，所以可能需要一定长度的启动时间。目的在于跳过可迭代对象的开始部分。

应用：

```python
python复制代码dropwhile(lambda x: x<3, [1,2,3,4,5])  # 3 4 5
dropwhile(lambda line: line.startswith('#'), f)  # 读取文件时过滤文件首部以#开头的行
```

#### filterfalse

参数：`itertools.filterfalse(predicate, iterable)`

用途：创建一个迭代器，只返回 *iterable* 中 *predicate* 为 `False` 的元素。如果 *predicate* 是 `None`，返回真值测试为false的元素。

应用：

```python
python复制代码filterfalse(lambda x: x%2, range(10))  # 0 2 4 6 8
filterfalse(None, range(10))  # 0
# 注：filter() 返回 iterable 中 predicate 为 True 的元素
filter(lambda x: x%2, range(10))  # 1 3 5 7 9
filter(None, range(10))  # 1 2 3 4 5 6 7 8 9
```

#### groupby

参数：`itertools.filterfalse(iterable, key=None)`

用途：创建一个迭代器，返回 *iterable* 中连续的键和组。*key* 是一个计算元素键值函数。如果未指定或为 `None`，*key* 缺省为恒等函数（identity function），返回元素不变。一般来说，*iterable* 需用同一个键值函数预先排序。返回的组本身也是一个迭代器，它与 `groupby()` 共享底层的可迭代对象。因为源是共享的，当 `groupby()` 对象向后迭代时，前一个组将消失。

应用：

```python
python复制代码# 注：实际返回结果中value为迭代器
groupby('AABB')  # {'A': ['A', 'A'], 'B': ['B', 'B']}
groupby('AaBb', key=lambda x: x.upper())  # {'A': ['A', 'a'], 'B': ['B', 'b']}
div_size = lambda x: 'small' if x < 3 else 'medium' if x == 3 else 'big'
groupby([1,2,3,4,5], key=div_size)  # {'small': [1, 2], 'medium': [3], 'big': [4, 5]}
```

#### islice

参数：`itertools.islice(iterable, stop)` or `itertools.islice(iterable, start, stop[, step])`

用途：创建一个迭代器，返回从 *iterable* 里选中的元素。如果 *start* 不是0，跳过 *iterable* 中的元素，直到到达 *start* 这个位置。之后迭代器连续返回元素，除非 *step* 设置的值很高导致被跳过。如果 *stop* 为 `None`，迭代器耗光为止；否则，在指定的位置停止。与普通的切片不同，`islice()` 不支持将 *start* ， *stop* ，或 *step* 设为负值。

应用：

```python
python复制代码islice('ABCDEFG', 2)  # A B
islice('ABCDEFG', 2, 5)  # C D E
islice('ABCDEFG', 2, None)  # C D E F G
islice('ABCDEFG', 2, 5, 2)  # C E
islice('ABCDEFG', 2, None, 2)  # C E G
# 注：如果 start 为 None，迭代从0开始。如果 step 为 None ，步长缺省为1。
islice('ABCDEFG', None, None)  # A B C D E F G
```

#### pairwise

> Python 3.10 新特性

参数：`itertools.pairwise(iterable)`

用途：创建一个迭代器，返回从 *iterable* 获取的连续重叠对。

应用：

```python
python复制代码# 注：输出迭代器中 2-tuples 的数量将比输入的数量少一个。
pairwise('ABCDEFG')  # AB BC CD DE EF FG
# 注：如果输入的可迭代对象小于两个值，则该值为空。
pairwise('A')  # (Empty)
```

#### takewhile

参数：`itertools.takewhile(predicate, iterable)`

用途：创建一个迭代器，只要 predicate 为真就从可迭代对象中返回元素。

应用：

```python
python复制代码takewhile(lambda x: x<5, [1,2,3,4,5])  # 1 2
takewhile(lambda x: x.isdigit(), '123abc456')  # 1 2 3
```

#### tee

参数：`itertools.tee(iterable, n=2)`

用途：从一个可迭代对象中返回 *n* 个独立的迭代器。一旦 tee() 实施了一次分裂，原有的 iterable 不应再被使用；否则tee对象无法得知 iterable 可能已向后迭代。`tee` 迭代器不是线程安全的。

应用：

```python
python复制代码# 注：实际返回结果为迭代器
tee(range(3))  # [0, 1, 2] [0, 1, 2]
```

#### zip_longest

参数：`itertools.zip_longest(*iterables, fillvalue=None)`

用途：创建一个迭代器，从每个可迭代对象中收集元素。如果可迭代对象的长度未对齐，将根据 *fillvalue* 填充缺失值。迭代持续到耗光最长的可迭代对象。

应用：

```python
python复制代码zip_longest('ABCD', 'xy')  # ('A','x') ('B','y'), ('C',None) ('D',None)
zip_longest('ABCD', 'xy', fillvalue='-')  # ('A','x') ('B','y'), ('C','-') ('D','-')
```

### 3 组合迭代器 Combinatoric iterators

#### product

参数：`itertools.product(*iterables, repeat=1)`

用途：创建一个迭代器，返回可迭代对象输入的**笛卡儿积**。

应用：

```python
python复制代码product('AB', range(3))  # ('A',0) ('A',1) ('A',2) ('B',0) ('B',1) ('B',2)
product(range(2), repeat=3)  # (0,0) (0,1) (1,0) (1,1)
```

#### permutations

参数：`itertools.permutations(iterable, r=None)`

用途：创建一个迭代器，连续返回由 *iterable* 元素生成长度为 *r* 的**排列**。如果 *r* 未指定或为 `None` ，*r* 默认设置为 *iterable* 的长度，这种情况下，生成所有全长排列。

应用：

```python
python复制代码permutations(range(3))  # (0,1,2) (0,2,1) (1,0,2) (1,2,0) (2,0,1) (2,1,0)
permutations('ABC')  # ('A','B','C') ('A','C','B') ('B','A','C') ('B','C','A') ('C','A','B') ('C','B','A')
permutations('ABC', 2)  # ('A','B') ('A','C') ('B','A') ('B','C') ('C','A') ('C','B')
```

#### combinations

参数：`itertools.combinations(iterable, r)`

用途：创建一个迭代器，返回由输入 *iterable* 中元素组成长度为 *r* 的子序列（**组合**）。

应用：

```python
python复制代码combinations(range(3), 2)  # (0,1) (0,2) (1,2)
combinations('ABC', 3)  # ('A','B','C')
combinations('ABC', 2)  # ('A','B') ('A','C') ('B','C')
```

#### combinations_with_replacement

参数：`itertools.combinations_with_replacement(iterable, r)`

用途：创建一个迭代器，返回由输入 *iterable* 中元素组成的长度为 *r* 的子序列（组合），允许每个元素可重复出现。

应用：

```python
python复制代码# 注：combinations 相当于不可放回，combinations_with_replacement 相当于可放回
combinations_with_replacement(range(3), 2)  # (0,0) (0,1) (0,2) (1,1) (1,2) (2,2)
combinations_with_replacement('ABC', 2)  # ('A','A') ('A','B') ('A','C') ('B','B') ('B','C') ('C','C')
```

### 4 itertools 配方 Recipes

itertools 配方使用现有的 itertools 作为基础构件来创建扩展的工具集。

```python
python
复制代码pip install more-itertools
```

扩展的工具提供了与底层工具集相同的高性能。保持了超棒的内存利用率，因为一次只处理一个元素，而不是将整个可迭代对象加载到内存。代码量保持得很小，以函数式风格将这些工具连接在一起，有助于消除临时变量。速度依然很快，因为倾向于使用“矢量化”构件来取代解释器开销大的 for 循环和 generator 。

详细内容可参看 Python Package Index 上的 [more-itertools 项目](https://link.juejin.cn?target=https%3A%2F%2Fpypi.org%2Fproject%2Fmore-itertools%2F) 。

注：PyPI = Python Package Index

参考链接：https://juejin.cn/post/7040138701518831652