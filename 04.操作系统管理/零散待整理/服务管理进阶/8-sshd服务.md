# ssh服务

## 学习目标

1. 能够清楚ssh的作用
3. 能够使用ssh进行远程连接
4. 能够使用远程传输指令进行文档传输

## 一、ssh介绍

ssh（Secure Shell）是一种能够提供安全远程登录会话的协议。该协议有2个作用：远程连接、远程文件传输。

默认端口号是：22。因为ssh协议会对传输的数据进行加密，所以强调ssh协议是安全的。

ssh服务名：sshd（服务名中的d 全称daemon，守护进程）

**sshd服务提供两种安全验证的方法：**

1. 基于口令的安全验证：经过验证账号与密码即可登录到远程主机
2. 基于秘钥的安全验证：需要在本地生成“秘钥对”后将公钥传送至服务端，进行公共秘钥的比较。

## 二、客户端远程连接

### 1. 基于口令安全验证

**ssh命令用于远程管理linux主机，格式为：ssh 【选项】 主机**

| 选项 | 作用                     |
| ---- | ------------------------ |
| -p   | 指定连接端口（默认为22） |

示例：

```shell
[root@itcast ~]# ssh -p22 root@172.16.99.154
# 或者：[root@itcast ~]# ssh root@172.16.99.154
The authenticity of host '172.16.99.154 (172.16.99.154)' can't be established.
ECDSA key fingerprint is SHA256:Bxg4t/hWyxETavu9nPaGxavoXHes90wW106ePXwWLTE.
Are you sure you want to continue connecting (yes/no)? yes   # 第一次连接输入yes
Warning: Permanently added '172.16.99.154' (ECDSA) to the list of known hosts.
root@172.16.99.154's password: 								 							 # 此处输入远程主机root用户的密码
Last login: Wed Mar 13 09:06:36 2019 from 172.16.99.1
```

### 2. 基于秘钥安全验证

**第一步：**在本地主机中生成"秘钥对"，将公钥传送到远程主机中

```shell
[root@localhost 桌面]# ssh-keygen
Generating public/private rsa key pair.
Enter file in which to save the key (/root/.ssh/id_rsa):  #回车或这只秘钥的存储路径
Created directory '/root/.ssh'.
Enter passphrase (empty for no passphrase): 				      #回车或设置秘钥密码
Enter same passphrase again: 
Your identification has been saved in /root/.ssh/id_rsa.
Your public key has been saved in /root/.ssh/id_rsa.pub.
The key fingerprint is:
e2:6d:a5:a9:66:0c:8d:1a:12:44:44:86:6b:46:b3:9b root@localhost.localdomain
The key's randomart image is:
+--[ RSA 2048]----+
|==               |
|o+               |
|o.o              |
|o+               |
|o.o  o. S .      |
|.E. o..o +       |
| . o o. =        |
|  .   +o         |
|     o.          |
```

将公钥传送到远程主机

```shell
[root@localhost ~]# ssh-copy-id 172.16.247.220(远程服务器地址)
The authenticity of host '172.16.247.220 (172.16.247.220)' can't be established.
ECDSA key fingerprint is 31:f7:3f:e5:5c:98:1f:88:99:2e:79:37:0a:c7:e8:5c.
Are you sure you want to continue connecting (yes/no)? yes      # 输入yes
/usr/bin/ssh-copy-id: INFO: attempting to log in with the new key(s), to filter out any that are already installed
/usr/bin/ssh-copy-id: INFO: 1 key(s) remain to be installed -- if you are prompted now it is to install the new keys
root@172.16.247.220's password: 					 								# 输入对应ip的密码

Number of key(s) added: 1

Now try logging into the machine, with:   "ssh '172.16.247.220'"
and check to make sure that only the key(s) you wanted were added.
```

**第二步：**在远程服务器中修改sshd服务的配置文件

```shell
[root@localhost ~]# vim /etc/ssh/sshd_config

# 将允许秘钥验证的参数设置为yes
#PubkeyAuthentication yes    

# 将允许密码验证的参数设置为no
PasswordAuthentication yes      


# 保存退出，重启ssh服务
[root@localhost ~]# systemctl restart sshd
```

**第三步：**无密码远程登录

```shell
[root@localhost ~]# ssh 172.16.247.221
```

## 三、修改sshd的配置文件

修改sshd服务的端口，重新进行远程连接

> 注意：
>
> 1. 端口范围从0-65535
> 2. 不能使用别的服务已经占用的端口（常见的：20、21、23、25、80、443、3389、3306、11211等）

```shell
# 打开sshd_config文件，修改端口为2222
[root@itcast ~]# vim /etc/ssh/sshd_config
Port 2222

# 重启sshd服务
[root@itcast ~]# systemctl restart sshd
```

退出远程连接终端，重新连接会发现连接不成功，那是因为防火墙对新端口默认是拒绝的，执行一下命令关闭防火墙和selinux：

```
[root@itcast ~]# setenforce 0
[root@itcast ~]# systemctl stop firewalld
```

## 四、远程传输命令

> 要想将一些文件通过网络传输给其他主机，恰好两台主机都是linux系统，我们可以直接使用scp命令传输文件到另外一台主机

**scp命令用于在网络中安全的传输文件**

| 选项       | 作用                     |
| ---------- | ------------------------ |
| -P（大写） | 指定远程主机的sshd端口号 |
| -r         | 传送文件夹时添加此参数   |

**将本地文件传送到远程主机**

格式为：scp 【选项】 本地文件 远程账户@远程ip:远程目录

```shell
# 将本地文件/root/out.txt 传送到远程主机的/root/目录
[root@itcast ~]# touch out.txt
[root@itcast ~]# scp -P2222 out.txt root@172.16.99.159:/root/
root@172.16.99.159's password: 				//此处输入远程主机的密码
out.txt                                                      100%    0     0.0KB/s   00:00 

# 将本地文件夹/root/outdir 传送到远程主机的/root/目录
[root@itcast ~]# mkdir outdir
[root@itcast ~]# scp -P2222 -r outdir/ root@172.16.99.159:/root/
root@172.16.99.159's password: 				//此处输入远程主机密码
```

**将远程主机文件下载到本地**

格式为：scp [选项]  远程用户@远程ip:远程文件 本地目录

```shell
# 将远程主机的/root/down.txt 文件下载到本地的/root目录
[root@itcast ~]# scp -P2222 root@172.16.99.159:/root/down.txt ./
root@172.16.99.159's password: 		 //远程主机密码
down.txt                                    							100%    0     0.0KB/s   00:00

# 将远程主机/root/downdir目录下载到本地/root目录
[root@itcast ~]# scp -P2222 -r root@172.16.99.159:/root/downdir ./
root@172.16.99.159's password:    //远程主机密码
```
