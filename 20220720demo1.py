#-*- coding: utf-8 -*-

### 返回函数

def calc_sum(*args):
    ax = 0
    for n in args:
        ax = ax + n
    return ax

def lazy_sum(*args):
    def sum():
        ax = 0
        for n in args:
            ax = ax + n
        return ax
    return sum

f = lazy_sum(1,3,5,7,9)
print(f)
print(f())

## 返回的函数并没有立刻执行，直到调用了f()才执行，因此返回函数不要引用任何循环变量，或者后续会发生变化的变量
def count1():
    fs = []
    for i in range(1,4):
        def f():
            return i*i
        fs.append(f)
    return fs

f1,f2,f3 = count1()
print(f1(),f2(),f3())

## 一定要引用循环变量时，再创建一个函数，用该函数的参数绑定循环变量当前的值
## 已绑定到函数参数的值不变,lambda函数可缩短
def count2():
    def f(j):
        def g():
            return j*j
        return g
    fs = []
    for i in range(1,4):
        fs.append(f(i))
    return fs

f1,f2,f3 = count2()
print(f1(),f2(),f3())

## 使用闭包时，对外层变量赋值前，先使用nonlocal声明该变量不是当前函数的局部变量
def createcounter():
    x = 0
    def counter():
        nonlocal x
        x = x + 1
        return x
    return counter

counterA = createcounter()
print(counterA(), counterA(), counterA(), counterA(), counterA()) # 1 2 3 4 5
counterB = createcounter()
if [counterB(), counterB(), counterB(), counterB()] == [1, 2, 3, 4]:
    print('测试通过!')
else:
    print('测试失败!')