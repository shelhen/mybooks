计量经济学python包econtools

文档：http://www.danielmsullivan.com/econtools/

### 安装与依赖

```
pip install econtools
```

依赖：

- python3.6+
- Scipy and its dependencies
- Pytables (可选,需要处理HDF5文档)



数据导入

read()：根据文件名后缀来使用正确的方法读取数据。

write()：和read类似

```python
from econtools import read

df = read('my_data.csv')    # uses pandas.read_csv
df = read('my_data.dta')    # uses pandas.read_stata
df = read('my_data.pkl')    # uses pandas.read_pickle
```

save_cli()

这允许您在不覆盖磁盘上的任何表或数字的情况下运行脚本，并避免注释/取消注释进行保存的代码行。

confirmer()

http://www.danielmsullivan.com/econtools/io.html#id4



stata_merge（）

封装了pandas.merge，并添加了一些类似stata的细节，通过一个标记来指示观察结果是否存在于左侧、右侧或两个数据集中（stata中的cf _merge变量）。
group_id（）可以很容易地根据其他变量的列表生成自己的任意id号。

econtools.metrics.reg：OLS回归

econtools.metrics.ivreg：工具变量回归

Results.Ftest：基于回归结果的假设检验

econtools.metrics.f_test：标准的假设检验

econtools.metrics.kdensity：核密度估计

econtools.metrics.llr：局部回归

outreg（）将回归结果以LaTeX表片段返回
table_statrow（）创建回归表和汇总统计表的底行。

http://www.danielmsullivan.com/econtools/to_latex.html#tolatex

绘图工具

binscatter()

binscatter 散点图

legend_below：在主轴下方创建图例

模块：linearmodels

