# pustil 学习

`psutil`是是一个基于`python`的跨平台系统和进程实用信息包，可用于在`Python`程序中检索系统信息，如CPU, 内存, 磁盘的使用情况、网络, 设备相关信息等，该包实现了由Unix命令行工具提供的许多功能，如`ps`, `top`, `lsof`, `netstat`, `ifconfig`, `who`, `df`, `kill`, `free`, `nice`, `ionice`, `iostat`, `iotop`, `uptime`, `pidof`, `tty`, `taskset`, `pmap`等，`psutil`目前支持`Linux`、`Windows`、`macOS`以及`Sun Solaris`、`AIX`、`BSD`等平台。

```
pip install psutil
```

## 一、系统

### 1.cpu

### 2.磁盘

### 3.网络

#### （1）网络统计信息

```
psutil.net_io_counters(pernic=False, nowrap=True)
```

获取系统范畴内网络 I/O 的统计信息，结果以命名元组返回，具体包括：

| 名称           | 说明           | 名称      | 说明                 |
| -------------- | -------------- | --------- | -------------------- |
| `bytes_sent`   | 发送的字节数   | `errin`   | 接收时的错误总数     |
| `bytes_recv`   | 接收的字节数   | `errout`  | 发送时的错误总数     |
| `packets_sent` | 发送的数据包数 | `dropin`  | 丢弃的传入数据包总数 |
| `packets_recv` | 收到的数据包数 | `dropout` | 丢弃的传出数据包总数 |

> `dropout`在 `macOS` 和 `BSD` 上始终为 0。

参数`pernic`控制网络接口信息是否以字典返回，其中网络接口名称为键，命名元组为值，在没有网络接口的机器上，如果 `pernic` 为 `True` ，此函数将返回 `None` 或` {}`。

在某些系统（例如 `Linux`）上，内核返回的数字可能会溢出并换行（从零开始）。如果 `nowrap `为 `True` ，`psutil `将在函数调用中检测并调整这些数字，并将“旧值”添加到“新值”，以便返回的数字始终增加或保持不变，但永远不会减少。`net_io_counters.cache_clear()` 可用于使 `nowrap` 缓存无效。 

#### （2）网络连接信息

```
psutil.net_connections(kind='inet')
```

以命名元组列表的形式返回系统范围的套接字连接。 每个命名元组提供 7 个属性：

| 名称     | 说明                                                         |
| -------- | ------------------------------------------------------------ |
| `fd`     | 套接字文件描述符， 若连接指向当前进程，则可以将其传递给 `socket.fromfd` 以获得可用的套接字对象。在 `Windows` 和 `SunOS` 上，这始终设置为 `-1`。 |
| `family` | 地址族，`AF_INET`、`AF_INET6` 或` AF_UNIX`。                 |
| `type`   | 地址类型，`SOCK_STREAMSOCK_STREAM`、`SOCK_DGRAM` 或 `SOCK_SEQPACKET`。 |
| `laddr`  | 对于`AF_UNIX` 套接字，本地地址作为`(ip, port)`命名元组或路径`(path)`。 |
| `raddr`  | 对于`AF_UNIX` 套接字，远程地址作为`(ip, port)`命名元组或绝对路径`(path)`。当远程端点未连接时，将获得一个空元组 `(AF_INET*)` 或 `"" (AF_UNIX)` |
| `status` | `TCP` 连接的状态。返回值是 `psutil.CONN_* `常量之一（字符串）。 对于 `UDP `和 `UNIX` 套接字，这始终是` psutil.CONN_NONE`。 |
| `pid`    | 如果可检索打开套接字的进程的`PID`，否则为`None`。在Linux上，此字段的可用性根据进程权限（需要 root）而变化。 |

参数`kind`接受一个字符串，用于过滤：

| Kind 值             | 连接使用            |                   |                            |
| ------------------- | ------------------- | ----------------- | -------------------------- |
| `"inet"`            | `IPv4` 和 `IPv6`    | `"udp"`           | `UDP`                      |
| `"inet4"`/`"inet6"` | `IPv4` 或` IPv6`    | `"udp4"`/`"udp6"` | `UDP`（基于 `IPvn`）       |
| `"tcp"`             | TCP                 | `"unix"`          | `UNIX` 套接字(`udp`/`tcp`) |
| `"tcp4"`/`"tcp6"`   | TCP （基于 `IPvn`） | `"all"`           | 所有可能的协议             |

#### （3）网卡地址信息

```
psutil.net_if_addrs()
```

返回与系统上安装的每个 `NIC`（网络接口卡）关联的地址作为字典，其键是 `NIC `名称，值是分配给 `NIC` 的每个地址的命名元组列表。 每个命名元组包括 5 个字段：

| 属性        | 说明                                                         |
| ----------- | ------------------------------------------------------------ |
| `family`    | 地址族，`AF_INET `或 `AF_INET6` 或` psutil.AF_LINK`，指的是 `MAC` 地址。 |
| `address`   | 主 `NIC` 地址（始终设置）。                                  |
| `netmask`   | 网络掩码地址（可能是 `None` ）。                             |
| `broadcast` | 广播地址（可能是 `None` ）。                                 |
| `ptp`       | 点对点接口（通常是`VPN`）上的目标地址，与广播地址互斥， 可能为 `None`。 |

#### （4）网卡状态

```
psutil.net_if_stats()
```

以字典形式返回系统上安装的每个 `NIC`（网络接口卡）的信息，其键是 `NIC` 名称，值是具有以下字段的命名元组：

| 属性     | 说明                                                         |
| -------- | ------------------------------------------------------------ |
| `isup`   | 指示 `NIC `是否已启用并正在运行（意味着以太网电缆或 `Wi-Fi `已连接）。 |
| `duplex` | 双工通信类型，可以是`NIC_DUPLEX_FULL`或`NIC_DUPLEX_HALF`或`NIC_DUPLEX_UNKNOWN`。 |
| `speed`  | 以兆位`(MB)`为单位的`NIC` 速度，如果无法确定（例如“本地主机”），它将设置为 0。 |
| `mtu`    | 以字节为单位 的`NIC` 最大传输单位。                          |

### 4.传感器

### 5.其他系统信息

## 二、进程

### 1.函数

### 2.异常

### 3.进程类



## 三、windows服务

### 1.迭代服务

### 2.根据名称获取服务

### 3.win服务类

## 四、常量

### 1.操作系统

### 2.进程状态

### 3.进程优先级

### 4.进程资源

### 5.网络连接

```
psutil.CONN_ESTABLISHED
psutil.CONN_SYN_SENT
psutil.CONN_SYN_RECV
psutil.CONN_FIN_WAIT1
psutil.CONN_FIN_WAIT2
psutil.CONN_TIME_WAIT
psutil.CONN_CLOSE
psutil.CONN_CLOSE_WAIT
psutil.CONN_LAST_ACK
psutil.CONN_LISTEN
psutil.CONN_CLOSING
psutil.CONN_NONE
psutil.CONN_DELETE_TCB(Windows)
psutil.CONN_IDLE(Solaris)
psutil.CONN_BOUND(Solaris)
```

### 6.硬件

## 五、工具函数

### 1.按名称查进程

### 2.终止进程树

### 3.过滤和排序进程

### 4.字节转换

## 六、其他问题

### 1.FAQ

```
Q: 为什么某些进程我会无权限?
A: 当你查询其他用户拥有的进程时可能会发生这种情况，尤其是在 macOS (参考问题 #883) 和 Windows 上。不幸的是，除了以更高的权限运行 Python 进程之外，对此无能为力。 在 Unix 上，你可以以 root 身份运行 Python 进程或使用 SUID 位（ps 和 netstat 执行此操作）。 在 Windows 上，你可以将 Python 进程作为 NT AUTHORITY\SYSTEM 运行，或者将 Python 脚本安装为 Windows 服务（ProcessHacker 执行此操作）。
Q: 支持在windows系统的MinGW上运行吗?
A: 不支持, 你应该使用 Visual Studio (参阅 开发指南).
```

### 2.测试

### 3.安全

### 4.开发指南

