#-*- coding: utf-8 -*-

import functools

### 匿名函数，无需显式地定义函数
alist = list(map(lambda x: x*x , [1,2,3,4,5,6,7,8,9]))
print(alist)
## 关键字lambda表示匿名函数
## 限制为只能有一个表达式，但不用写return
## 函数名不会冲突，可赋给变量后用变量调用此函数
## 也可将匿名函数作为返回值

### 装饰器(decorator)，在代码运行期间动态增加功能
def log(func):
    @functools.wraps(func)
    def wrapper(*args, **kw):
        print('call %s():' % func.__name__)
        return func(*args, **kw)
    return wrapper
@log
def now():
    print('2022-7-21')
now()

def log(text):
    def decorator(func):
        @functools.wraps(func)
        def wrapper(*args, **kw):
            print('%s %s():' % (text, func.__name__))
            return func(*args, **kw)
        return wrapper
    return decorator
@log('execute')
def now():
    print('2022-7-21')
now()

def log(func):
    @functools.wraps(func)
    def wrapper():
        print('begin call')
        func()
        print('end call')
    return wrapper
@log
def now():
    print('2022-7-21')
now()

## 函数运行时间测试
import time, functools

def metric(fn):
    @functools.wraps(fn)
    def wrapper(*args,**kw):
        t1=time.time()
        fn(*args,**kw)
        t2=time.time()
        print('%s executed in %s ms' % (fn.__name__, t2-t1))
        return fn(*args,**kw)
    return wrapper

@metric
def fast(x, y):
    time.sleep(0.0012)
    return x + y;

@metric
def slow(x, y, z):
    time.sleep(0.1234)
    return x * y * z;

f = fast(11, 22)
s = slow(11, 22, 33)
if f != 33:
    print('测试失败!')
elif s != 7986:
    print('测试失败!')

### 偏函数

import functools
int2 = functools.partial(int,base=2)
print(int2('101010101'))
## 对函数重新设置默认值为新函数