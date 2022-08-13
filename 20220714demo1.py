#-*- coding: utf-8 -*-

### 递归函数
def fact(n):
    if n == 1:
        return 1
    return n * fact(n-1)
print(fact(6))
## 防止栈溢出
## 尾递归优化和循环等价，Python标准的解释器没有针对尾递归进行优化，任何递归函数都存在栈溢出的问题

## 汉诺塔移动
def move(n,a,b,c):
    if n == 1:
        print(a,'-->',c)
    else:
        move(n-1,a,c,b)
        move(1,a,b,c)
        move(n-1,b,a,c)
move(3,'A','B','C')