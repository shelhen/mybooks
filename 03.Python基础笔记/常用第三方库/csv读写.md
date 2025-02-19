# Python处理csv文件

`CSV (Comma Separated Values) `格式是电子表格和数据库中最常见的输入、输出文件格式。`csv`格式使用历史悠久，目前标准还有待完善，因此不同应用程序读写的数据会存在细微的差别。这种差别让处理多个来源的 `CSV `文件变得困难。

csv 模块实现了 CSV 格式表单数据的读写。其提供了诸如“以兼容 Excel 的方式输出数据文件”或“读取 Excel 程序输出的数据文件”的功能，程序员无需知道 Excel 所采用 CSV 格式的细节。此模块同样可以用于定义其他应用程序可用的 CSV 格式或定义特定需求的 CSV 格式。

处理`csv`格式的数据的模块有很多，比较常见的是`pandas`和内置的`csv`模块，这里以`csv`模块为例。

[csv模块官方文档](https://docs.python.org/zh-cn/3/library/csv.html)











```python
csv 模块中的 reader 类和 writer 类可用于读写序列化的数据。也可使用 DictReader 类和 DictWriter 类以字典的形式读写数据。
```

