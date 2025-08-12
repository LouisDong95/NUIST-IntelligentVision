
>[!warning] 提示
>推荐使用 [obsidian 软件](https://obsidian.md/), 以获得最好的阅读体验
>点击右上角「书本」![](https://raw.githubusercontent.com/Nekasu/Blog_pics/main/20240910163022.png)图标, 进入阅读模式, 以获得更好的阅读体验！
>
>作者：Nekasu/周肖桐

本文介绍了如何为所有用户安装 pycharm.

## 一、下载并解压

于 pycharm 官网下载 linux 版本的 pycharm, 在终端使用以下命令解压：

```bash
tar xfz pycharm-xxx.tar.gz
```

## 二、安装

1. 进入 root 用户

```bash
sudo su root
```

2. 进入解压后目录中的 bin 文件夹

```
cd ./pycharm-xxx/bin
```

3. 运行安装命令

```bash
./pycharm.sh
```

## 创建快捷方式

1. 在终端中输入命令

```bash
​ sudo gedit /usr/share/applications/pycharm.desktop
```

2. 输入上述命令后会进入编辑页面, 输入以下代码
	1. 注意修改 Exec 中的路径：要输入自己 pycharm. Sh 的位置
	2. 注意修改 Icon 中的路径：要输入自己 pycharm. png 的位置

```
[Desktop Entry]
Type=Application
Name=Pycharm
GenericName=Pycharm3
Comment=Pycharm3:The Python IDE
Exec=sh /home/miaojing/下载/pycharm-community-2023.1/bin/pycharm.sh
Icon=/home/miaojing/下载/pycharm-community-2023.1/bin/pycharm.png
Terminal=pycharm
Categories=Pycharm;
```

修改完毕后保存并退出, 这样就可以在所有应用中找到 pycharm 了.
