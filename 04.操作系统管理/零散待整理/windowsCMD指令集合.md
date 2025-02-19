## windowsCMD指令集合

### 一、文件目录命令

```shell
# 切换到C、D、E盘
D:
# 目录切换
cd ..
cd ../ # 切换到上级目录
cd ../.. # 切换到上上级目录
cd ./dirname  # 切换本文件夹内其他文件夹目录
# 查看当前目录下文件
dir
# 创建目录
md newdir_name
# 删除目录
rd has_exist_dir_name
# 复制文件
copy 原路径 新路径
# 移动文件
move 原路径 新路径
# 删除文件
del file_name
# 重命名
rename 原文件路径 新文件路径

# 在文件中搜索字符串。
FIND [/V] [/C] [/N] [/I] [/OFF[LINE]] "string" [[drive:][path]filename[ ...]] 
  /V         显示所有未包含指定字符串的行。
  /C         仅显示包含字符串的行数。
  /N         显示行号。
  /I         搜索字符串时忽略大小写。
  /OFF[LINE] 不要跳过具有脱机属性集的文件。
  "string" 指定要搜索的文本字符串。
  [drive:][path]filename
             指定要搜索的文件。 
# 如果没有指定路径，FIND 将搜索在提示符处键入
# 的文本或者由另一命令产生的文本。
```

### 二、网络相关

```shell
# 一般用来检测网络状态，注意有些ip本身是禁ping的
ping 域名/ip 
# 查看本机ip：
ipconfig
# 本机ip配置详细信息：
ipconfig /all 
# 刷新本地dns缓存：
ipconfig /flushdns
# 查看网络连接状态
netstat
netstat -anb|more 
netstat -ano
```

