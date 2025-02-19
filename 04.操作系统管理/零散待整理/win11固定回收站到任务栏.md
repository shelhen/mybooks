解决方法如下：

```python
# 1.桌面创建快捷方式输入下面内容，命名为回收站
explorer.exe shell:RecycleBinFolder  # 用shell命令打开回收站、
# 2.完成后右键属性更改图标，输入下面内容，选择回收站图标，固定到任务栏即可
%SystemRoot%\system32\imageres.dll ##图标路径
```



