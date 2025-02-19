# Apache服务

## 学习目标

1. 清楚如何安装linux
2. 掌握apahce的管理命令
3. 能够独立配置虚拟机
4. 学会apache的日志分割
5. 能够配置rwrite重写规则

## 一、Apache概述安装

### 1. 介绍

  	Apache HTTP Server（简称Apache）是Apache软件基金会的一个开源的网页服务器，是世界使用排名第一的Web服务器软件。它可以运行在几乎所有广泛使用的计算机平台上，由于其跨平台和安全性被广泛使用，是最流行的Web服务器端软件之一。

​	apache的服务名称是httpd

​	[apache官网](<https://apache.org/>)

​	[httpd2.4官方文档](http://httpd.apache.org/docs/2.4/)

### 2. 安装

```shell
[root@itcast ~]# yum -y install httpd
```

### 3. 快速入门

#### 3.1 apache基本管理

```shell
# apache状态管理
[root@itcast ~]# systemctl start|stop|restart|reload|status httpd.service

# 设置apache开机启动
[root@itcast ~]# systemctl enable httpd.service

# 设置apache开机不启动
[root@itcast ~]# systemctl disable httpd.service
```

#### 3.2 站点根目录

apache默认站点根目录：`var/www/html`

#### 3.3 apache服务目录介绍

```shell
# /etc/httpd/
├── conf											  							# 主配置文件目录
│   ├── httpd.conf
│   └── magic
├── conf.d																		# 模块化配置文件目录(辅助配置文件目录)
│   ├── autoindex.conf
│   ├── README
│   ├── userdir.conf
│   └── welcome.conf
├── conf.modules.d														# 模块配置文件目录
│   ├── 00-base.conf
│   ├── 00-dav.conf
│   ├── 00-lua.conf
│   ├── 00-mpm.conf
│   ├── 00-proxy.conf
│   ├── 00-systemd.conf
│   └── 01-cgi.conf
├── logs -> ../../var/log/httpd								# 日志目录
├── modules -> ../../usr/lib64/httpd/modules	# 模块目录
└── run -> /run/httpd	     										# 运行时目录
```

#### 3.4  apache用户

apache在安装后会创建一个叫做apache的用户， apache的子进程就是用这个用户运行的

```shell
[root@itcast www]# tail -1 /etc/passwd
apache:x:48:48:Apache:/usr/share/httpd:/sbin/nologin
```

### 4.apache基本概念

#### 4.1 apache进程

- apache默认监听TCP协议的80端口
- apache默认会启动一个主进程(控制进程)和多个子进程

查看apache相关进程：

```shell
[root@itcast html]# ps aux | grep httpd
```

其中root运行的是主进程，apache身份运行的是子进程，主进程的id保存在/etc/httpd/run/httpd.pid文件内。真正用来处理web请求的是子进程，主进程用来管理子进程。

#### 4.2 apache模块

- apache是一个模块化设计的服务，核心只包含主要功能，扩展功能通过模块实现（可扩展性强，各功能依赖性低）。不同模块可以被静态的编译进程序，也可以动态加载。
- 模块的动态加载通过DSO(Dynamic shared Object)实现。

查看模块

```shell
[root@itcast html]# httpd -M
```

## 二、apache配置详解及实践

### 1、配置文件说明

#### 1.1 主配置文件位置

`/etc/httpd/conf/httpd.conf`

#### 1.2 配置文件格式

```shell
#directive(指令)			value(值)
 ServerRoot				 "/etc/httpd"
```

### 2、配置项详解

#### 2.1 ServerRoot

服务所在目录的路径，不需要做修改

```shell
ServerRoot "/etc/httpd"
```

#### 2.2 Listen

监听端口

```shell
#Listen 12.34.56.78:80                                                                                                                 
Listen 80 
```

配置语法

`Listen [IP-address:]portnumber [protocol]`

实践

```shell
# 1. 修改端口号
Listen 8080

# 2. Listen指令可重复出现多次
Listen 8080
Listen 80

# 注意：修改后必须重启服务才可生效
[root@itcast conf]# systemctl restart httpd.service
```

#### 2.3 Include

导入配置文件

```shell
Include conf.modules.d/*.conf				
```

#### 2.4 IncludeOptional

和include功能相同，都是导入配置文件的。区别是IncludeOptional导入的路径有问题时会被忽略。不会报错。

```shell
IncludeOptional conf.d/*.conf		  
```

#### 2.5 User和Group

httpd服务子进程启动时的账号和组，这个不用修改

```shell
User apache
Group apache
```

#### 2.6 ServerAdmin

服务运行时的管理员邮箱地址

```shell
ServerAdmin root@localhost
```

#### 2.7 DocumentRoot

站点根目录

```shell
DocumentRoot "/var/www/html"
```

语法

`DocumentRoot directory-path`

实践

```shell
#DocumentRoot "/var/www/html"                                                                                                          
DocumentRoot "/www"

#<Directory "/var/www/html">                                                                                 
<Directory "/www">   
```

#### 2.8 Directory

确定访问目录位置，标签配置。标签内是设置针对该目录的访问权限

```shell
<Directory "/var/www/html">
    Options Indexes FollowSymLinks			# 访问时的展示形式，Indexes索引展示
    AllowOverride None									# 设置指令是否可以在.htaccess使用
    Require all granted									# 允许所有人访问
</Directory>
```

- Options   访问时展示形式

  ​	Options Indexes    当前目录下没有默认页面，就显示目录结构

  ​        Options FollowSymLinks   默认设置，允许访问符号链接

  ​	Options None   关闭

- AllowOverride    `.htaccess`文件中允许的指令类型

  ​	AllowOverride All		     全部指令

  ​	AllowOverride None		默认值，不允许

  ​	AllowOverride directive-type [directive-type] …       具体指令类型

- Require      访问权限设置

  ​	Require all granted		无条件允许访问

  ​	Require all denied    	     无条件拒绝访问

  ​	Require method http-method **[**http-method] …  仅允许给定的HTTP方法访问

  ​	Require ip 10 172.20 192.168.2	指定ip地址范围的客户端可以访问		

实践

```shell
# 1. 去掉Indexes查看效果,注意改完配置后要重启http服务
<Directory "/var/www/html">
    Options FollowSymLinks
    AllowOverride None
    Require all granted
</Directory>

# 2. 去掉FollowSymLinks
<Directory "/var/www/html">
    Options None
    AllowOverride None
    Require all granted
</Directory>

# 3. 使用Require
<Directory "/var/www/html">
    Options None
    AllowOverride None
    Require all denied					# 无条件拒绝访问
</Directory>

<Directory "/var/www/html">
    Options None
    AllowOverride None
    Require method POST            # 仅允许post请求
</Directory>
```

#### 2.9 IfModule

以特定模块存在与否为条件的处理指令

```shell
# 如果dir_module存在，执行DirectoryIndex
<IfModule dir_module>                                                                                                                  
    DirectoryIndex index.html                   # 站点默认展示页                                                                                       
</IfModule>      
```

语法

`DirectoryIndex disabled | local-url [local-url] …`

默认

DirectoryIndex   index.html

实践

```shell
# 在站点根目录下创建一个index.html
[root@itcast html]# echo 'myindex' > index.html
```

#### 2.10 Files

包含适用于匹配文件名的指令

```shell
<Files ".ht*">
    Require all denied			  # 以.ht开头的文件拒绝提供访问
</Files>
```

#### 2.11 ErrorLog

错误日志记录位置

```shell
ErrorLog "logs/error_log"
```

#### 2.12 LogLevel

错误日志记录级别

```shell
LogLevel warn
```

错误级别选项

| **水平** | **描述**                  |
| :------- | :------------------------ |
| `emerg`  | 紧急情况 - 系统无法使用。 |
| `alert`  | 必须立即采取行动。        |
| `crit`   | 关键条件。                |
| `error`  | 错误条件。                |
| `warn`   | 警告条件。                |
| `notice` | 正常但重要的情况。        |
| `info`   | 基本信息                  |
| `debug`  | 调试级消息                |

#### 2.13 IfModule log_config_module

访问日志配置模块

```shell
<IfModule log_config_module>
		# 访问日志3种格式： combined，common， combinedio
    LogFormat "%h %l %u %t \"%r\" %>s %b \"%{Referer}i\" \"%{User-Agent}i\"" combined
    LogFormat "%h %l %u %t \"%r\" %>s %b" common

    <IfModule logio_module>
      # You need to enable mod_logio.c to use %I and %O
      LogFormat "%h %l %u %t \"%r\" %>s %b \"%{Referer}i\" \"%{User-Agent}i\" %I %O" combinedio
    </IfModule>
    
    # 确定访问日志位置和使用哪种日志格式
    CustomLog "logs/access_log" combined
</IfModule>
```

日志格式说明

| 标识           | 含义                                                         |
| -------------- | ------------------------------------------------------------ |
| %h             | 客户端ip                                                     |
| %l             | Remote User, 通常为一个减号（“-”）；                         |
| %u             | Remote user (from auth; may be bogus if return status (%s) is 401)；非为登录访问时，其为一个减号； |
| %t             | 服务器收到请求时的时间；                                     |
| %r             | First line of request，即表示请求报文的首行；记录了此次请求的“方法”，“URL”以及协议版本； |
| %>s            | 响应状态码；                                                 |
| %b             | 响应报文的大小，单位是字节；不包括响应报文的http首部；       |
| %{Referer}i    | 请求报文中首部“referer”的值；即从哪个页面中的超链接跳转至当前页面的； |
| %{User-Agent}i | 请求报文中首部“User-Agent”的值；即发出请求的应用程序；       |

#### 2.14 IfModule alias_module

文档映射

```shell
<IfModule alias_module>
    #
    # Redirect: Allows you to tell clients about documents that used to 
    # Example:
    # Redirect permanent /foo http://www.example.com/bar

    # Alias: Maps web paths into filesystem paths and is used to
    # Example:
    # Alias /webpath /full/filesystem/path

    # ScriptAlias: This controls which directories contain server scripts. 
    ScriptAlias /cgi-bin/ "/var/www/cgi-bin/"   # cgi脚本映射
</IfModule>
```

Redirect   外部重定向

Alias   将url映射到文件系统个位置

ScriptAlias   将url映射到CGI脚本

#### 2.15 AddDefaultCharset

响应内容的编码格式

```shell
AddDefaultCharset UTF-8
```

## 三、虚拟主机配置

> 虚拟主机指的是在单一机器上运行多个网站.
>
> 虚拟主机可以“基于IP”，即每个 IP 一个站点； 或者“基于域名”， 即每个 IP 多个站点。这些站点运行在同一物理服务器上。

虚拟机配置语法

```shell
<VirtualHost addr[:port] [addr[:port]] ...> 
    serverName    ...
    DocumentRoot	...
    ...
</VirtualHost>
```

### 1、基于域名

```shell
# 实践1，配置文件：/etc/httpd/conf.d/iplinux1.conf
<VirtualHost>
  DocumentRoot "/var/www/iplinux1/"
  ServerName www.iplinux1.org
  ErrorLog "iplinux1-error_log"
  TransferLog "iplinux1-access_log"
  <Directory "/var/www/html">
    Options Indexes FollowSymLinks
    AllowOverride None
    Require all granted
	</Directory>
</VirtualHost>

# 实践2，配置文件：/etc/httpd/conf.d/iplinux2.conf
<VirtualHost>
  DocumentRoot "/var/www/iplinux2/"
  ServerName www.iplinux2.org
  ErrorLog "ip2inux1-error_log"
  TransferLog "ip2inux1-access_log"
  <Directory "/var/www/html">
    Options Indexes FollowSymLinks
    AllowOverride None
    Require all granted
	</Directory>
```



### 2、基于ip

```shell
# 实践1，配置文件：/etc/httpd/conf.d/iplinux1.conf
<VirtualHost 172.16.99.251>
  DocumentRoot "/var/www/iplinux1/"
  ServerName www.iplinux1.org
  ErrorLog "iplinux1-error_log"
  TransferLog "iplinux1-access_log"
  <Directory "/var/www/html">
    Options Indexes FollowSymLinks
    AllowOverride None
    Require all granted
	</Directory>
</VirtualHost>

# 实践2，配置文件：/etc/httpd/conf.d/iplinux2.conf
<VirtualHost 172.16.99.252>
  DocumentRoot "/var/www/iplinux2/"
  ServerName www.iplinux2.org
  ErrorLog "ip2inux1-error_log"
  TransferLog "ip2inux1-access_log"
  <Directory "/var/www/html">
    Options Indexes FollowSymLinks
    AllowOverride None
    Require all granted
	</Directory>
</VirtualHost>
```

## 四、rewrite重写

> `mod_rewrite` 提供了基于[正则表达式](https://httpd.apache.org/docs/2.4/zh-cn/rewrite/intro.html#regex)规则动态修改传入的请求的 URL 的方法。可以定义任意的的url映射到内部的站点文件中

1演示现象，解决效果，得出rewrite概念

2-1如何实现具体讲解步骤，可以带入原理

2-2实践

3剖析实现原理，提升知识面

4小结

### 1、rewrite需求

我们在使用Apache做为Web服务器时，有时候出于SEO优化或者是url路径的简洁，需要将输入的url转换成更为友好的url，这时候就可以使用rewrite重写功能。

使用rewrite功能首先需要开启mod_rewrite模块。yum安装的apache默认已经开启。

### 2、rewrite使用详解

rewrite规则可以在Directory指令中进行配置

rewrite学习的三个核心是**RewriteEngine**，**RewriteCond**，**RewriteRule**

#### 2.1 RewriteEngine

rewrite功能的总开关，用来开启rewrite重写功能

```shell
RewriteEngine on
```

#### 2.2 RewriteCond

RewriteCond定义规则条件，当请求满足RewriteCond配置的条件时，执行RewriteCond后面的RewriteRule语句

比如：

```shell
RewriteEngine on
RewriteCond  %{HTTP_USER_AGENT}  ^Mozilla//5/.0.*
RewriteRule  index          index.html    
```

上面的规则表示：如果匹配到http请求中HTTP_USER_AGENT是Mozilla//5/.0.*开头的。访问index时，会自动访问到index.html

RewriteCond 和 RewriteRule 是上下对应的关系。可以有1个或者好几个RewriteCond来匹配一个RewriteRule

**RewriteCond常见的HTTP请求匹配方式

```
RewriteCond %{HTTP_REFERER} (www.mytest.com)
RewriteCond %{HTTP_USER_AGENT}  ^Mozilla//5/.0.*
RewriteCond %{REQUEST_FILENAME} !-f
```

**HTTP_REFERER** 

判断访问者的来源

案例：

```shell
RewriteCond %{HTTP_REFERER} (www.mytest.com)
RewriteRule (.*)$ mytest.html
# 如果访问的上一个页面是www.mytest.com,无论当前访问的是哪个页面，都会跳转到mytest.html
```

**REQUEST_FILENAME** 

匹配当前访问的文件

案例：

```shell
RewriteCond %{REQUEST_FILENAME} !-f
RewriteCond %{REQUEST_FILENAME} !-d
RewriteRule ^news/sports/(\d+)\.html web/index\.php?c=news&a=sports&num=$1 [QSA,NC,L]

# 访问news/sports/123.html,真实访问的是web/index.php?c=news&a=sports&num=123
```

`-f`是否是一个目录，判断是否不是一个目录：`!-d`

`-d`是否是一个文件，判断是否不是一个问价：`!-f`

`$1`表示第一个参数

#### 2.3 RewriteRule

> RewriteRule是配合RewriteCond一起使用的，RewriteRule是RewriteCond成功匹配后的具体执行过程

`RewriteRule`的写法：

```shell
RewriteRule Pattern Substitution [flags]
```

`Pattern`是一个正则匹配

`Substitution`匹配的替换内容

`[flags]`参数限制

`[QSA]`qsappend(追加查询字符串)的意思，次标记强制重写引擎在已有的替换字符串中追加一个查询字符串，而不是简单的替换。如果需要通过重写规则在请求串中增加信息，就可以使用这个标记。

`NC`nocase(忽略大小写)的意思，它使Pattern忽略大小写，也就是在Pattern与当前URL匹配时，"A-Z"和"a-z"没有区别。这个一般也会加上，因为我们的url本身就不区分大小写的。

`Rredirect(强制重定向)的意思，适合匹配Patter后，Substitution是一个http地址url的情况，就调整出去了。`

`L`last(结尾规则)的意思，就是已经匹配到了，就立即停止，不再匹配下面的Rule了，类似于编程语言中的`break`语法，跳出去了。

## 五、apache日志切割

### 1、为什么要进行日志切割

随着网站访问越来越大，web服务产生的日志文件也会越来越大，这个时候日志文件不仅占用了大量的服务器空间，而且日志分析也很麻烦

### 2、日志分割两种方式

#### 2.1 rotatelogs

> rotatelogs是apache自带的日志切割工具

案例：使用rotatelogs每天记录一个日志文件

```shell
# 编辑httpd主配置文件 /etc/httpd/conf/httpd.conf
# 注释下面两行
ErrorLog "logs/error_log" 
CustomLog "logs/access_log" combined

# 添加下面两行
ErrorLog "|/usr/sbin/rotatelogs -l logs/error_%Y%m%d.log 86400"
CustomLog "|/usr/sbin/rotatelogs -l logs/access_%Y%m%d.log 86400" combined
```

说明：

86400为轮转的时间,单位为秒

#### 2.2 cronolog

> Cronolog是一款日志轮循（rotation）工具，可以用它来把Apache、Tomcat等Web服务器上输出的日志切分成按日或月保存的文件。

cronolog安装

```shell
[root@ ~]# tar zxf cronolog-1.6.2.tar.gz
[root@ ~]# cd cronolog-1.6.2/
[root@ cronolog-1.6.2]# ./configure && make && make install
```

案例：使用cronologs每天记录一个日志文件

```shell
ErrorLog "|/usr/local/sbin/cronolog logs/error-%Y%m%d.log"
CustomLog "|/usr/local/sbin/cronolog logs/access-%Y%m%d.log" combined
```

扩展：按小时轮询生成日志

```shell
CustomLog "|/usr/local/sbin/cronolog logs /access_%Y%m%d%H.log" combined
```

### 3 总结

推荐使用cronolog，因为cronolog稳定高配置简单。

## 六、apache防盗链

> 防盗链就是防止别人网站代码里调用我们服务器的图片、文件、视频等资源。如果别人盗用我们的资源，会增加服务器的贷款压力。
>
> 通过防盗链的方式，可以设置限制第三方的站点通过引用的方式获取服务器上的图片，如果想要获取本站点的图片数据，只能通过本站点访问获取，这样也有效的减少了服务器的资源。

### 1、rewrite实现防盗链

```shell
1. RewriteEngine On
2. RewriteCond %{HTTP_REFERER} !^http://www.myitcast.com/.*$ [NC]
3. RewriteCond %{HTTP_REFERER} !^http://www.myitcast.com$ [NC]
4. RewriteCond %{HTTP_REFERER} !^http://myitcast.com/.*$ [NC]
5. RewriteCond %{HTTP_REFERER} !^http://myitcast.com$ [NC]
6. RewriteRule .*\.(gif|jpg|swf)$ http://www.myitcast.com/link.png [R,NC]
```

说明：

第1条：开启rewrite重写

第2~5条：开启授信任的站点，能够访问站点的图片资源

第6条：访问站点的gif|jpg|swf等类型资源时，跳转到

### 2、SetEnvIfNoCase

> 通过判断浏览器头信息来阻止盗链请求

```shell
SetEnvIfNoCase Referer "^$" local_ref
SetEnvIfNoCase Referer "www.benet.com/.*$" local_ref
SetEnvIfNoCase Referer "benet.com/.*$" local_ref
<filesmatch "\.(mp3|mp4|zip|rar|jpg|gif)">
		Require all denied
		Require env local_ref
</filesmatch>
```

说明：

SetEnvIfNoCase 当满足某个条件时，为变量赋值，即根据客户端请求属性设置环境变量。

Referer ：指明了请求当前资源原始资源的URL





