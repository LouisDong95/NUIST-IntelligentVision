
>[!warning] 提示
>推荐使用 [obsidian 软件](https://obsidian.md/), 以获得最好的阅读体验
>点击右上角「书本」![](https://raw.githubusercontent.com/Nekasu/Blog_pics/main/20240910163022.png)图标, 进入阅读模式, 以获得更好的阅读体验！
>
>作者：周肖桐


## 前言

1. 如果想要使用 mmcv 等包, 可能需要单独安装 nvcc, 现将流程进行简单记录

### 前提

要求已安装 Anaconda 与 PyTorch 

## 流程

### Step 1 查看自己环境的 cudatoolkit 的版本

1. 使用 `conda activate [环境名]` 的命令进入需要安装 nvcc 的 conda 环境中.
	1. ![](https://raw.githubusercontent.com/Nekasu/Blog_pics/main/20240512150325.png)
2. 输入 `python` 进入 Python 命令行模式
	1. ![](https://raw.githubusercontent.com/Nekasu/Blog_pics/main/20240512150409.png)
3. 输入以下两条命令
	1. `import torch`：输入此命令后不会显示任何信息
		1. ![](https://raw.githubusercontent.com/Nekasu/Blog_pics/main/20240512150716.png)
	2. `print(torch.version.cuda)`：输入此命令后命令行会显示当前环境下的 cudatoolkit 版本
		1. ![](https://raw.githubusercontent.com/Nekasu/Blog_pics/main/20240512150650.png)
		2. 如此处, 当前环境的 cudatoolkit 版本为 11.7

### Step 2 根据 cudatoolkit 版本信息查询版本对应信息

1. 进入 [anaconda 下载nvcc的官网](https://anaconda.org/nvidia/cuda-nvcc)
	1. ![](https://raw.githubusercontent.com/Nekasu/Blog_pics/main/20240512151009.png)
2. 根据上面查询的 cudatoolkit 版本, 找到对应的安装命令
	1. 本人的 cudatoolkit 版本为 11.7 , 所以找到以下两条命令
	2. ![](https://raw.githubusercontent.com/Nekasu/Blog_pics/main/20240512151143.png)
3. 选择其中一个, 在命令行中运行即可