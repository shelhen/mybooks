# linux运行模式

## 学习目标

1. 清楚什么是运行模式
2. 能够永久的修改系统的运行模式
3. 知道每种运行模式的含义

## 一、什么是运行模式

运行模式也叫做运行级别(在centos7里叫target)。在linux进入系统时会运行第一支程序，这个程序运行时会从5种模式中选择一种运行，这里的5种模式，就是运行模式。

> 第一支程序说明：
>
> 在centos6叫做 systemV
>
> 在centos7叫做systemd
>
> 因此在centos6和centos7里面的运行级别也发生了一些变化

## 二、运行级别说明

| SystemV（centos6） | systemd（centos7）                  | 含义                   |
| ------------------ | ----------------------------------- | ---------------------- |
| init0              | systemctl poweroff                  | 关机                   |
| Init1              | systemctl rescue                    | 单用户模式（用于维护） |
| Init[234]          | systemctl isolate multi-user.target | 命令行模式             |
| Init5              | systemctl isolate graphical.target  | 图形界面模式           |
| init6              | systemctl reboot                    | 重启                   |

## 三、运行模式管理

### 1. 获取当前运行模式

```shell
[root@itcast ~]# systemctl get-default
graphical.target
```

### 2. 临时设置运行模式

```shell
# 切换为命令行模式
[root@itcast ~]# systemctl isolate multi-user.target
# 兼容centos6命令(和上面命令效果相同)
[root@itcast ~]# init 3   

# 切换为图形界面模式
[root@itcast ~]# systemctl isolate graphical.target
[root@itcast ~]# init 5

根据上面2个模式，可以练习下模式0和模式6
```

### 2. 设定系统默认运行模式(永久设置)

```shell
# 设定默认运行模式为命令行模式
[root@itcast ~]# systemctl set-default multi-user.target

# 设定默认运行模式为图形界面模式
[root@itcast ~]# systemctl set-default graphical.target
```

> 注意：
>
> 1. 设定之后，系统以后就会以该模式运行
> 2. 切记不要设置为poweroff 和 reboot模式

