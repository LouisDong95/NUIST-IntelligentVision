
>[!warning] 提示
>推荐使用 [obsidian 软件](https://obsidian.md/), 以获得最好的阅读体验
>点击右上角「书本」![](https://raw.githubusercontent.com/Nekasu/Blog_pics/main/20240910163022.png)图标, 进入阅读模式, 以获得更好的阅读体验！
>
>作者：周肖桐


# 问题背景介绍

本人在多次交替使用 `pip install` 与 `conda install` 命令后, 终于出现了问题. 

实际上, 本人并不知道多次交替使用这两个安装 Python 包的命令会出现很大的问题, 最终可能导致整个环境不可用. 

痛定思痛, 决定写下这篇文档, 以警诫后来者, 不要将这两个命令多次交替使用. 

<mark style="background: #FF5582A6;">在文章末尾, 将给出「最佳实践列表」. </mark>

值得注意的是, 这篇文章的大部分内容来自 Anaconda 官方, 并非本人原创, 且翻译由网友完成, 本人仅仅是给出了问题背景, 并修改一些语句描述. 具体请看下面的转载介绍.

>[!tips] 声明
>本笔记转载自 [# Using Pip in a Conda Environment](https://www.anaconda.com/blog/using-pip-in-a-conda-environment)
>
并由 [wuzaoquant](https://www.zhihu.com/people/wuzaoquant) 于[知乎-pip 与 conda 可以混用吗？]([wuzaoquant](https://www.zhihu.com/people/wuzaoquant))问题下翻译并回答.

# Anaconda 官方回答

## 多次交替使用命令的后果与造成该后果的原因

### 后果

当 conda 和 pip 一起使用来创建环境时，可能会出现问题，尤其是当工具多次交叉使用时，建立了难以重现的状态。

### 造成该后果的原因

- 这些问题大多数因为 conda 与其他包管理器一样，控制未安装的包的能力有限。
- 在 pip 之后运行 conda 可能会覆盖并破坏 pip 安装的包。
	- 使用 pip 将软件安装到 conda 环境中，conda 并不知道这些更改，并且后续可能会继续进行破坏性修改。
	- 同样，pip 可能会升级或删除 conda 安装的软件包。
- 有时这些破坏是表面的，留存了一些本应删除的文件；更糟的情况下，环境可能会变的不可用。

## 一些解决方案

有几个步骤可以用来避免在一起使用 conda 和 pip 时破坏环境。

### 仅仅使用 conda 命令安装 Python 包

- 方法描述
	- 一种万无一失的方法是仅使用 conda 包。如果需要的软件没有 conda 包，可以使用 conda build 为所述软件创建包。
	- 对于 PyPI 上的项目，conda skeleton 命令（conda-build 的一部分）生成一个 recipe，只需很少或无需修改，即可创建一个 conda 包。
- 一些问题
	- 为所有包创建 conda 包是安全可靠的办法，但如果涉及大量仅在 PyPI 上才有的包，可能会带来较大工作量。

### 创建一个新环境

- 如果期望同时使用 pip 和 conda 包安装软件，最好使用一个新的专门的 conda 环境中，以保护其他环境免受 pip 修改。
- Conda 支持创建多个隔离环境，并可以在其中安装不同版本的包。在 conda 环境中，尽可能使用硬链接，而不是复制文件以节省空间。如果安装了一组类似的包，则每个新的 conda 环境只需要少量的额外磁盘空间。许多用户仅使用 conda 安装后的默认环境，如果此环境因 pip 和 conda 多次交替使用而变得混乱，则更难恢复。
- 如果单独创建了 conda 环境，则后续可以轻松删除和重新创建环境，而不会影响其他功能。
- 与其运行 conda、运行 pip、运行 conda，不如先创建一个具有组合 conda 要求的新环境，然后再运行 pip，可以在删除旧环境之前测试此新环境。主要是 pip 的“状态性”导致了问题，由于软件包安装顺序而存在的状态越多，保持正常就越困难。

Anaconda 官方已经意识到了将 pip 和 conda 结合起来的困难，所以一直在添加功能，以便让设置数据科学环境过程尽可能简单。

## 最佳实践列表

### 先使用 Conda 再使用 pip (简单易用)

- 使用 Conda 安装尽可能多的需求，然后使用 pip
	- 一旦使用了 `pip install` 命令, 则不可再使用 `conda install` 命令
- 使用 pip 安装时 –-upgrade-strategy 参数应当设置为 only-if-needed（默认）
- 不要将 pip 与 –-user 参数一起使用，避免为所有用户安装

### 使用 conda 环境进行隔离 (我就是要混用)

- 创建一个新的 conda 环境, 专门用于 pip 与 conda 混用
- 由于 anaconda 硬链接特性，新环境占用的空间很小
- 同时应注意避免在原的 conda 环境下运行 pip

### 如果需要更改，请重新创建环境

- 一旦使用 pip，conda 将不知道这些变化
- 要安装其他 Conda 软件包，最好重新创建环境