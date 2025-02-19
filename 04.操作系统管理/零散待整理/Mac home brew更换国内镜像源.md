# Mac home brew管理

**[Homebrew](https://brew.sh/zh-cn/)** 是Mac OS（或 Linux）平台下软件包管理工具，拥有安装、卸载、更新、查看、搜索等功能。通过简单的指令可以实现包管理，而不用关心各种依赖和文件路径情况。

## 一、安装与换源

### 1.下载

官方推荐安装代码如下，但是国内使用一般来说会出现如下的报错，因为网络限制原因，无法链接服务器下载。

```shell
/bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"
# curl: (7) Failed to connect to raw.githubusercontent.com port 443: Connection refused
```

因此国内建议直接借助如下脚本安装与卸载：

```shell
# 安装命令
/bin/zsh -c "$(curl -fsSL https://gitee.com/cunkai/HomebrewCN/raw/master/Homebrew.sh)"
# 卸载命令
/bin/zsh -c "$(curl -fsSL https://gitee.com/cunkai/HomebrewCN/raw/master/HomebrewUninstall.sh)"

# 验证是否安装成功
brew -v
# Homebrew 4.4.6
```

执行安装命令后，按照提示一步一步往下执行，通常都可以安装成功，顺便还可以将下载源切换，安装完毕后输入如下命令验证是否安装成功。

> 我这里尝试了一下直接下载官网安装包[下载地址](https://github.com/Mortennn/Dozer/releases/)，下载后手动安装，安装完毕后需要手动添加至系统环境变量。

```shell
vim ~/.zprofile
# eval "$(/opt/homebrew/bin/brew shellenv)"

# 操作失误修改了导致所有命令不可用，可通过如下命令临时改变path改回来。
export PATH=/sbin:/bin:/usr/sbin:/usr/bin:/usr/local/bin
```

### 2.换源

如果很幸运借助糟糕的网络下载成功了，再尝试各种软件下载时却因为**国内网络原因**报错，可以尝试换源：

```shell
# 替换brew.git
cd "$(brew --repo)"
# 阿里云 ：https://mirrors.tuna.tsinghua.edu.cn/git/homebrew/brew.git
# 清华云
git remote set-url origin https://mirrors.aliyun.com/homebrew/brew.git
# 替换homebrew-core.git
cd "$(brew --repo)/Library/Taps/homebrew/homebrew-core"
# 阿里云：https://mirrors.tuna.tsinghua.edu.cn/git/homebrew/homebrew-core.git
# 清华云
git remote set-url origin https://mirrors.aliyun.com/homebrew/homebrew-core.git
# 刷新源
brew update

# 重置为官方源：
cd "$(brew --repo)"
git remote set-url origin https://github.com/Homebrew/brew.git
```







### Redis 桌面管理器 - Redis 桌面管理工具

![rdm.jpg](imgs/BkLcS9qsTd5UPCpz.jpg)

[Redis Desktop Manager](https://redisdesktop.com/)（也叫 RDM）是一款快速的开源 Redis 数据库管理应用，它提供 Windows, Linux 和 MacOS 版本。这个工具提供了简单易用的界面来访问你的 redis 数据库并执行一些基本的操作：包括树形结构查看，增删改查操作，通过 shell 执行命令。RDM 支持 SSL/TLS 加密，SSH 隧道和云实例，如：Amazon ElastiCache, Microsoft Azure Redis Cache 和 Redis Labs。

### Robo 3T - MongoDB 桌面管理工具

![robomongo.jpg](imgs/BkL5tNlzNJDzQxMF.jpg)

Robo 3T（原名 Robomongo)是一款免费的轻量级 MongoDB 管理工具，内建 shell。另外一款专业版本 MongoDB 管理工具 Studio 3T，它支持更丰富的特性，包括可视化查询创建器、就地编辑、自动完成IntelliShell、SQL查询、导入/导出SQL等。