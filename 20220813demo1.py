#-*- coding: utf-8 -*-

'a test module'

__author__ = 'YW FENG'

import sys

def test():
    args = sys.argv
    if len(args) == 1:
        print('Hello,world!')
    elif len(args) == 2:
        print('Hello,%s!'%args[1])
    else:
        print('Too many arguments!')

if __name__ == '__main__':
    test()
### 在命令行运行hello模块文件时，python 解释器将特殊变量_name_置为_main_
### 其他地方导入时，if判断将失败，这种if测试可让一个模块通过命令行运行时执行额外的代码/运行测试
## 将外部不需要引用的函数定义为private(_xxx或__xxx)，外部需要引用的函数定义为public
## pip install -i https://pypi.tuna.tsinghua.edu.cn/simple +模块名