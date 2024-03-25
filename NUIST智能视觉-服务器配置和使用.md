# 服务器安装和配置

### 1.装机(Ubuntu22.04)

镜像：https://releases.ubuntu.com/jammy/

UltraISO： https://cn.ultraiso.net

### 2.显卡驱动安装

应用程序-附加驱动（推荐选择最新tested版本）

重启

3.安装远程连接

**安装**

~~~shell
sudo apt update
sudo apt install openssh-server
检查是否启动
sudo systemctl status openssh-server
sudo ufw allow ssh
查看IP
ifconfig
~~~

**测试**

另外一台电脑内网，需要有线连接校园网，且安装openssh客户端

~~~shell
ssh username@ip
~~~

### 4.永久挂载磁盘

应用程序-工具-磁盘-复制额外磁盘UUID

~~~shell
sudo nano /etc/fstab
~~~

最后另起一行插入如下，挂载至/mnt/sda目录下

~~~shell
UUID=b42dc368-1896-4928-baab-14fd4a9a59b2 /mnt/sda ext4 auto,user,rw 0 0
~~~

重启

### 5.多用户使用Anaconda

**安装配置**

下载：https://www.anaconda.com/download

安装至：`/opt/anaconda3`下

详细步骤：https://anaconda.org.cn/anaconda/install/multi-user/ or https://zhuanlan.zhihu.com/p/570747928

**测试**

创建新用户：`sudo adduser username`

将其加入conda组：`sudo usermod -aG conda username`

切换用户后：`conda`

### 6.安装xrdp

https://www.digitalocean.com/community/tutorials/how-to-enable-remote-desktop-protocol-using-xrdp-on-ubuntu-22-04

~~~
sudo apt install xfce4 xfce4-goodies -y
选择gdm3
sudo apt install xrdp -y
验证状态
sudo systemctl status xrdp
如果不是active（running），手动启动
sudo systemctl start xrdp
~~~

# 服务器使用

### 内网用户（ssh+远程桌面）：

**ssh命令行连接**：

1.通ssh连接至公共用户，见上面3测试

2.添加自己的账户并加入conda组中，见上面5测试

3.切换至自己用户和目录下：`su - username `

4.创建RDP会话界面：

~~~
touch .xsession
nano .xsession
~~~

插入`echo "xfce4-session" | tee .xsession`确保远程登录连接到图形界面

**远程桌面登录图形界面**：

1.windows远程桌面连接/mac下载Microsoft Remote Desktop，输入ip，用户名和密码

### 外网用户：

向日葵

### 注意事项：

数据集代码等放在`/mnt/sda`下面
