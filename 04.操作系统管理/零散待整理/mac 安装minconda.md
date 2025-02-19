Mac-下安装：

下载地址：https://docs.anaconda.com/miniconda/

下载完毕后，在下载区打开终端输入：

```shell
# 文件名是自己下载的sh文件，-p后面填安装路径，默认装到user下
# -b 表示将环境变量自动写入到～/.bash文件中
sh Miniconda3-py39_24.3.0-0-MacOSX-arm64.sh -b
```

初始化可以使用内部命令或直接修改`.zshrc`文件

```shell
# 命令行初始化
~/miniconda3/bin/conda init zsh
~/miniconda3/bin/conda init  # 需要修改PATH环境变量

# 修改配置文件
vim ~/.zshrc

# ~/miniconda3/etc/profile.d/conda.sh
export PATH="~/miniconda3/bin:$PATH"
#激活配置文件
source ~/.zshrc

# 测试
conda --version
```

mac安装minconda后终端默认使用conda，会一直在base环境下

```shell
conda config --set auto_activate_base false
```

