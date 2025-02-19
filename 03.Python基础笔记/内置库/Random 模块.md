## Random 模块的基本使用



random 模块提供了生成随机数的函数，例如生成随机整数、浮点数、序列等。这里的随机数并不是真正意义上的随机数，而是输入时间戳并进行一系列算法的函数，可以进行破解，不能用于安全加密。

### Random对象

```python
class random.Random([seed]):
    """该类实现了 random 模块所用的默认伪随机数生成器。"""
    pass
```

其中封装了以下方法，都是类方法，可以由`random.xxx()`直接调用。

#### 1.初始化函数

`random.seed(a=None)`

参数`a`可以为任意类型，其他类型将会在内部被转化为整数，若`a`被省略，则默认传入当前系统时间，该函数用于初始化随机数生成器。

#### 2.处理字节数据

`random.randbytes(n)`：生成 *n* 个随机字节。

#### 3.处理整数

`random.randrange(start, stop[, step])`：从 `range(start, stop, step) `随机选择的一个元素，`randrange(start=100) `会被解读为` randrange(0, 100, 1)`。

`random.randint(a, b)`：返回随机整数` N` 满足 `a <= N <= b`，相当于 `randrange(a, b+1)`。

`random.getrandbits(k)`：生成一个包含k个随机位的正整数。

#### 4.处理序列

`random.choice(seq)`：从非空序列 seq 返回一个随机元素。 如果 seq 为空，则引发 `IndexError`。

`random.choices(population, weights=None, *, cum_weights=None, k=1)`：从 `population` 中有重复地以相等的概率随机选取元素，返回大小为 k 的元素列表。 如果指定了 `weight` 序列，则根据相对权重进行选择，如果给出 `cum_weights` 序列，则根据累积权重进行选择。如果 `population` 为空，则引发 `IndexError`。在内部，相对权重在进行选择之前会转换为累积权重，因此提供累积权重可以节省工作量。

`random.shuffle(x)`：就地将序列 x 随机打乱位置。

`andom.sample(x, k=len(x))`：返回包含来自总体的k个元素的新列表，同时保持原始总体不变。 结果列表按选择顺序排列，因此所有子切片也将是有效的随机样本，用于无重复的随机抽样。

`random.sample(population, k, *, counts=None)`：总体成员不必是 `hashable` 或 `unique`，总体中可以包含重复，重复的元素可以一个个地直接列出，或使用可选的仅限关键字形参 `counts` 来指定。如`sample(['red', 'blue'], counts=[4, 2], k=5)` 等价于` sample(['red', 'red', 'red', 'red', 'blue', 'blue'], k=5)`。

#### 5.处理分布

`random.binomialvariate(n=1, p=0.5)`：二项式分布。 返回 n 次独立试验在每次试验的成功率为 p 时的成功次数。

`random.random()`：返回` 0.0 <= X < 1.0` 范围内的下一个随机浮点数。

`random.uniform(a, b)`：返回一个处于`a`与`b`之间的随机浮点数 `N` ，`b`可以小于`a`。

`random.triangular(low, high, mode)`：返回一个服用对称分布的随机浮点数 `N` ，其中，默认边界为`0`和`1`，`mode` 为边界之间的中点。

`random.expovariate(lambd=1.0)`：指数分布。lambd 是 1.0 除以所需的平均值，它应该是非零的。 如果 lambd 为正，则返回值的范围为 0 到正无穷大；如果 lambd 为负，则返回值从负无穷大到 0。

`random.gammavariate(alpha, beta)`：Gamma 分布。 shape 和 scale 形参，即 alpha 和 beta，必须为正值，其分布函数为:$pdf(x)=\frac{x^{(\alpha-1)}\times{e}^{-\frac{1}{\beta}}}{\gamma(\alpha)\beta^{\alpha}}$

`random.gauss(mu=0.0, sigma=1.0)`：正态分布，也称高斯分布。 mu 为平均值，而 sigma 为标准差。 此函数要稍快于下面所定义的 `normalvariate() `函数。

注意，当使用多线程时，它们有可能将获得相同的返回值，可以通过如下方法来解决，1) 让每个线程使用不同的随机数生成器实例。 2) 在所有调用外面加锁。 3) 改用速度较慢但是线程安全的 `normalvariate() `函数。

`random.normalvariate(mu=0.0, sigma=1.0)`：正态分布。 mu 是平均值，sigma 是标准差。

`random.lognormvariate(mu, sigma)`：对数正态分布。 如果你采用这个分布的自然对数，你将得到一个正态分布，平均值为 mu 和标准差为 sigma 。 mu 可以是任何值，sigma 必须大于零。

`random.vonmisesvariate(mu, kappa)`：冯·米塞斯分布。 mu 是平均角度，以弧度表示，介于0和 2*pi 之间，kappa 是浓度参数，必须大于或等于零。 如果 kappa 等于零，则该分布在 0 到 2*pi 的范围内减小到均匀的随机角度。

`random.paretovariate(alpha)`：帕累托分布。 alpha 是形状参数。

`random.weibullvariate(alpha, beta)`：威布尔分布。 alpha 是比例参数，beta 是形状参数。

