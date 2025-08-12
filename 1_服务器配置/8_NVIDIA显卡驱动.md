如果遇到 GCC 错误的问题, 需要进行以下操作:

1. 运行以下命令, 将需要的 GCC 版本设为默认编译器, 并验证是否设置成功
```
sudo update-alternatives --config gcc
gcc --version
```
2. 如果 PATH 中包含自定义的 GCC 路径（如 /usr/local/gcc-7.5.0/bin），需要调整 PATH，确保 /usr/bin 优先. 注意! 添加到环境变量时, 添加到bin即可！不能将gcc可执行程序放到路径中!
```
export PATH=/usr/bin:$PATH # 这是正确的
export PATH=/usr/bin/gcc-13:$PATH # 这是错误的
```