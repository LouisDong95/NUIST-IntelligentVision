这是一个快速生成上机时间的小工具, 只需要输入日期、天数等信息, 就能自动生成合适的上机时间！

## 文件介绍

一共包含两个文件：

1. time.exe：是一个在windows下可直接运行的程序, 包含了所有的功能
2. time.py：是上述exe文件的源代码, 各位如果有兴趣可以根据代码自定义功能.

## 功能介绍

1. 下载time.exe文件可直接体验功能
2. 双击time.exe运行程序, ~~由于没有资金支持所以~~界面是小黑窗, 能用就行
	1. ![](https://raw.githubusercontent.com/Nekasu/Blog_pics/main/20241104163906.png)
	2. 输入日期如"2024-11-04"或"2024-11-4"均可, 且存在一定的纠错功能, 如果输入有误会提醒
3. 随后输入需要生成的天数
	1. ![](https://raw.githubusercontent.com/Nekasu/Blog_pics/main/20241104164023.png)
	2. 如果输入10, 则会从输入的起始日期开始计算连续的10天
4. 随后输入开始工作的时间, 用一个\[0,23\]的数字表示开始工作的时间
	1. ![](https://raw.githubusercontent.com/Nekasu/Blog_pics/main/20241104164122.png)
	2. 存在一定的纠错机制, 如果输入<0或>24的数, 则会需要重新输入
5. 随后输入结束工作的时间, 用一个\[开始时间,23\]的数字表示结束工作的时间
	1. ![image-20241104164254228](C:\Users\Nekasu\AppData\Roaming\Typora\typora-user-images\image-20241104164254228.png)
6. 随后输入y/n
	1. 若对该生成的时间不满意, 请输入y, 程序将自动重新生成一对时间数据
		1. ![](https://raw.githubusercontent.com/Nekasu/Blog_pics/main/20241104164351.png)
	2. 若玟 该生成的时间合适, 请输入n, 程序将进行下一对时间的生成
		1. ![](https://raw.githubusercontent.com/Nekasu/Blog_pics/main/20241104164421.png)
	3. 如果输入了除(n/N)以外的其他字符, 均会按照输入了y的情况处理, 如下图所示：
		1. ![](https://raw.githubusercontent.com/Nekasu/Blog_pics/main/20241104164512.png)
7. 重复多次后完成生成, 在exe程序的同目录下找到csv文件, 生成结果就在其中 
	1. ![](https://raw.githubusercontent.com/Nekasu/Blog_pics/main/20241104164555.png)
	2. ![](https://raw.githubusercontent.com/Nekasu/Blog_pics/main/20241104164619.png)
	3. 若出现"###########", 请不用惊慌, 这不是乱码, 而是字符太长导致的, 请双击单元格或调整单元格大小以显示信息, 如下图：
		1. ![](https://raw.githubusercontent.com/Nekasu/Blog_pics/main/20241104164746.png)
8. 最后复制粘贴到Excel文件中, 并使用格式刷完成最终的格式统一.