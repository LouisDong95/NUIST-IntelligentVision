
>[!warning] 提示
>点击右上角「书本」![[Pasted image 20231125105318.png]]图标, 进入阅读模式, 以获得更好的阅读体验！

本文要求已安装 Anaconda

# 安装 cudatoolkit 与 cudnn

- 安装的命令
	- 使用如下命令即可在创建环境时安装 cudatoolkit 与 cudnn 
	- `环境名`可以为任意
	- Python 版本号推荐使用 3.9 或 3.10, 较为稳定
```anaconda
conda create -n [环境名] python=[版本号] cudatoolkit cudnn
```

- 一个例子
	- 下面是一个例子, 用于安装名为 zxt_cuda_11.8 并使用 python3.9 作为 Python 版本的环境：
```anaconda
conda create -n zxt_cuda_11.8 python=3.9 cudatoolkit cudnn
```

输入命令后等待安装完毕即可

安装完毕后使用如下命令进入创建的新环境：
```anaconda
conda activate [环境名]
```

下面是一个例子, 演示进入刚刚创建的 `zxt_cuda_11.8` 环境：
```anaconda
conda activate zxt_cuda_11.8
```

## 安装 PyTorch

访问 PyTorch 官网, [这是链接](https://pytorch.org/get-started/locally/) 

- 进入后, 可以看到如下的面板
	- ![](https://raw.githubusercontent.com/Nekasu/Blog_pics/main/20240326103114.png) 
- 我们可以通过面板选择获取安装 PyTorch 的命令
- 下面我解释一下面板中各个选项的意思
	1. PyTorch Build 项
		1. Stable 表示稳定版, Preview 表示开发版
		2. 建议选择 Stable, 防止有些包尚为对开发版做支持
	2. Your OS
		1. 根据你的操作系统选择
	3. Package
		1. 如果知道是什么意思就按需选择
		2. 如果不知道就选 pip
	4. Compute Platform
		1. 根据自己的 cudatoolkit 版本选择
		2. 关于如何查看自己的 cudatoolkit 版本, 请阅读本文文末的说明部分, 或点击 [[2_配置cuda与PyTorch#查看自己 cudatoolkit 版本的方法|这里]] 直达该部分
		3. 如果没有自己需要的版本, 请点击图中红框处的链接获取以往版本
			1. ![](https://raw.githubusercontent.com/Nekasu/Blog_pics/main/20240326105442.png) 

- 选择完毕后, 复制 `run this commamd` 中的命令, 在命令行中运行即可, 推荐[[1_服务器网络代理设置#使命令行也使用代理|在服务器命令行中开启代理]] , 以获取更快的下载速度
- 不开也没事, 就是下载的慢一点

输入命令后等待安装完毕即可

# 验证

1. 在命令行中输入需要激活的环境：
	1. 使用如下命令激活环境：`conda acitvate [环境名]`
	2. 激活后前面的括号中会变成「己激活的环境名」
	3. ![](https://raw.githubusercontent.com/Nekasu/Blog_pics/main/20240326104209.png) 
2. 在命令行中输入 `python` 以进入 Python 环境.
	1. ![](https://raw.githubusercontent.com/Nekasu/Blog_pics/main/20240326104941.png) 
3. 输入以下几条命令
	1. `import torch`
	2. `torch.__version__`
		1. 注意是 `version` 两侧分别为两个下划线, 共 4 个下划线
	3. 如果出现 torch 的版本信息就是安装完毕
	4. ![](https://raw.githubusercontent.com/Nekasu/Blog_pics/main/20240326105333.png) 

# 注意！

这里特别提醒, 不建议将 `conda install` 命令与 `pip install` 命令连续交替使用, 具体请看[[3_conda与pip的冲突_不建议二者交替使用]]

# 一些说明
## 查看自己 cudatoolkit 版本的方法

1. 在命令行中输入需要激活的环境：
	1. 使用如下命令激活环境：`conda acitvate [环境名]`
	2. 激活后前面的括号中会变成「己激活的环境名」
	3. ![](https://raw.githubusercontent.com/Nekasu/Blog_pics/main/20240326104209.png) 
2. 输入 `conda list` 查看环境中的所有包
	1. ![](https://raw.githubusercontent.com/Nekasu/Blog_pics/main/20240326104443.png) 
3. 找到 cudatoolkit 项, 中间的数字就是版本信息
	1. ![](https://raw.githubusercontent.com/Nekasu/Blog_pics/main/20240326104416.png) 