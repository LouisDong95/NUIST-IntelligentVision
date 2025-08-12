# 服务器安装和配置

### 1.装机(Ubuntu22.04)

镜像：https://releases.ubuntu.com/jammy/

UltraISO： https://cn.ultraiso.net

### 2.显卡驱动安装

#### 2.1 使用 ubuntu 软件安装

应用程序-附加驱动（推荐选择最新tested版本）

重启

#### 2.2 从 Nvidia 官网安装

https://blog.csdn.net/qq_48559526/article/details/134070092

- 如果安装失败，可能是gcc版本过低导致的, 可以用如下方法修改gcc版本：https://blog.csdn.net/weixin_43356770/article/details/139072376

### 3.安装远程连接

**安装**

```bash
sudo apt update
sudo apt install openssh-server
检查是否启动
sudo systemctl status openssh-server
sudo ufw allow ssh
查看IP
ifconfig
```


**测试**

另外一台电脑内网，需要有线连接校园网，且安装openssh客户端

~~~shell
ssh username@ip
~~~

### 4.永久挂载磁盘

1. 应用程序-工具-磁盘-复制额外磁盘 UUID
2. 修改 `etc/fstab` 文件
```shell
sudo nano /etc/fstab
```
3. 最后另起一行插入如下，挂载至/mnt/sda目录下

~~~shell
UUID=b42dc368-1896-4928-baab-14fd4a9a59b2 /mnt/sda ext4 auto,user,rw 0 0
~~~
4. 重启

### 5. 为系统创建多用户

有时, 我们需要为不同的人创建不同的账户, 这时需要用到以下命令
1. 添加用户
	1. useradd -s /bin/bash -m 用户名
		- ` -s /bin/bash` 表示使用 bash 作为默认的终端
		- ` -m` 表示将 `/home/用户名` 当作用户默认的根目录
	2. `useradd -s /bin/bash -d /mnt/sda/home/用户名 用户名`
		1. `-d /mnt/sda/home/用户名` 表示将指定路径当作用户默认的根目录
	3. 二选一即可
	4. 
1. 设置密码
	1. 我们需要使用以下命令为用户设置用户密码, 否则用户可能无法使用他的账号
	2. `passwd 用户名`
2. 删除账号
	1. 如果需要删除用户, 则可以使用以下命令
	2. `userdel -r 用户名`
3. 修改用户的根目录 (home 地址)
	1. 可以通过 usermod 命令修改用户的根目录
	2. `usermod -d 新的根目录地址 用户名`

### 6.多用户使用 Anaconda

**安装配置**

1. 下载： https://www.anaconda.com/download
2. 安装至：`/opt/anaconda3` 下
3. 详细步骤请参考：
	-  https://anaconda.org.cn/anaconda/install/multi-user/
4. 或参考 csdn：
	1. https://blog.csdn.net/youban_47/article/details/125420758

**测试**

创建新用户：`sudo adduser username`

将其加入conda组：`sudo usermod -aG conda username`

切换用户后：`conda`

### 7.安装 xrdp_使用 Windows 远程桌面工具来远程连接控制 Ubuntu 系统

https://www.digitalocean.com/community/tutorials/how-to-enable-remote-desktop-protocol-using-xrdp-on-ubuntu-22-04

```bash
sudo apt install xfce4 xfce4-goodies -y
#选择gdm3
sudo apt install xrdp -y
#验证状态
sudo systemctl status xrdp
#如果不是active（running），手动启动
sudo systemctl start xrdp
```


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
