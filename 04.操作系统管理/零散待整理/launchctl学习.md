```python

```

launchctl  开发备份

```python
launchctl

~/Library/LaunchAgents/app.jsnu_netkit.plist

# 加载任务, -w选项会将plist文件中无效的key覆盖掉，建议加上
launchctl load -w 
launchctl unload -w 
launchctl start 

# 删除任务
launchctl stop 

# com.jsnu.webhelper
```

```python
<string>/Users/xieheng/Library/LaunchAgents/jsnu.sh</string>

~/projects/jsnu_netkit/jsnu_netkit.sh:
```



```python
# 检查格式
plutil -lint com.jsnu
# 查看已经加载的代理
launchctl list | grep com.jsnu
-    78    com.applefs.user # 错误结果
-    0     com.applefs.user # 正确结果
```



