# logging日志

记录日志非常重要，python程序可以使用**logging**记录程序在运行时所产生的日志信息，日志信息记录有助于方便的了解程序的运行情况和开发人员检查bug，有助于分析用户的操作行为、喜好等信息，

## 一、日志记录级别

日志等级可以分为5个，从低到高分别是:

| 日志等级   | 说明                                                         |
| ---------- | ------------------------------------------------------------ |
| `DEBUG`    | 程序调试bug时使用                                            |
| `INFO`     | 程序正常运行时使用                                           |
| `WARNING`  | 程序未按预期运行时使用，但并不是错误，如:用户登录密码错误    |
| `ERROR`    | 程序出错误时使用，如:IO操作失败                              |
| `CRITICAL` | 特别严重的问题，导致程序不能再继续运行时使用，如:磁盘空间为空，一般很少使用 |

> 默认是`WARNING`等级，当在`WARNING`或`WARNING`之上等级的才记录日志信息。

## 二、基本使用

在 logging 包中记录日志的方式有两种:**输出到控制台**和**保存到日志文件**。

### 1.日志信息输出到控制台

```py
import logging

logging.debug('这是一个debug级别的日志信息')
logging.info('这是一个info级别的日志信息')
logging.warning('这是一个warning级别的日志信息')
logging.error('这是一个error级别的日志信息')
logging.critical('这是一个critical级别的日志信息')
```

日志信息只显示了大于等于WARNING级别的日志，这说明默认的日志级别设置为WARNING

**logging日志等级和输出格式的设置:**

```py
import logging

# 设置日志等级和输出日志格式
logging.basicConfig(level=logging.DEBUG,
                    format='%(asctime)s - %(filename)s[line:%(lineno)d] - %(levelname)s: %(message)s')

logging.debug('这是一个debug级别的日志信息')
logging.info('这是一个info级别的日志信息')
logging.warning('这是一个warning级别的日志信息')
logging.error('这是一个error级别的日志信息')
logging.critical('这是一个critical级别的日志信息')
```

**代码说明:**

```python
basicConfig(
	level 表示设置的日志等级
    format 表示日志的输出格式, 参数说明:
    	- %(levelname)s: 打印日志级别名称
    	- %(filename)s: 打印当前执行程序名
    	- %(lineno)d: 打印日志的当前行号
    	- %(asctime)s: 打印日志的时间
    	- %(message)s: 打印日志信息
)
```

### 2.日志信息保存到日志文件

```py
import logging

logging.basicConfig(level=logging.DEBUG,
                    format='%(asctime)s - %(filename)s[line:%(lineno)d] - %(levelname)s: %(message)s',
                    filename="log.txt",
                    filemode="w")

logging.debug('这是一个debug级别的日志信息')
logging.info('这是一个info级别的日志信息')
logging.warning('这是一个warning级别的日志信息')
logging.error('这是一个error级别的日志信息')
logging.critical('这是一个critical级别的日志信息')
```

