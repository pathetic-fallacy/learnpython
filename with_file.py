#-*- coding: utf-8 -*-

### with_file.py

try:
    f = open('D:/git/learnpython/filetoread.txt','r')
    print(f.read())
finally:
    if f:
        f.close()
### 保证无论是否出错都能正确地关闭文件

with open('D:/git/learnpython/filetoread.txt','r') as f:
    print(f.read())
### 引入with语句来调用close()方法

with open('D:/git/learnpython/filetoread.txt','r') as f:
    print(f.read(2))
### 不能确定大小时，通过这种方式进行反复调用


with open('D:/git/learnpython/filetoread.txt','r') as f:
    print(f.readline())

with open('D:/git/learnpython/filetoread.txt','r') as f:
    print(f.readlines())
### 配置文件

with open('D:/git/learnpython/filetoread.txt','r') as f:
    for line in f.readlines():
        print(line.strip()) # 把末尾的'\n'删掉

### open()函数返回的有read()方法的对象，统称为file-like Object，无需从特定类继承，仅需写一个read()方法
### 读取二进制文件,r->rb
### 读取非UTF-8编码的文本文件，在open()中传入encoding参数，例如末尾加上encoding='gbk'
### 编码不规范文件(含有非法编码字符)，open()中可接受errors参数，例如errors='ignore'(忽略)

### 写文件
with open('D:/git/learnpython/filetowrite.txt','w') as f: # 创建/覆盖，写
    f.write('Goodbye,world!')
with open('D:/git/learnpython/filetowrite.txt','a') as f: # 追加模式写入
    f.write('\nGoodbye,world!')