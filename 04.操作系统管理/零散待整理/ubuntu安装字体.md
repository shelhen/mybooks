# ubuntu安装字体

将待安装的`ttf`或`ttc`字体文件拷贝至`/usr/share/fonts/truetype`目录下即可，也可以在该目录下创建新的文件夹如`winfont`来进一步分类。

```shell
sudo mkdir /usr/share/fonts/truetype/myfonts
sudo cp *.ttc /usr/share/fonts/truetype/myfonts/*.ttc

# 最后刷新字体缓存
sudo fc-cache -fv
# 安装成功后通过如下命令测试是否安装成功
fc-match Times  # 查看Times New Roman
# Times New Roman.ttf: "Times New Roman" "Regular"

# 如果想在matplotlib下使用还需要刷新matplotlib缓存

emcho python -c "import matplotlib as plt;plt.get_cachedir()"
# /home/<user>/.cache/matplotlib
# 清空该文件夹即可
rm -rf /home/<user>/.cache/matplotlib
```

