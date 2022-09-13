#-*- coding: utf-8 -*-

### 捕获错误是捕获到该class的一个实例，因此错误为通过创建才能抛出（内置函数或自己编写的函数）

class FooError(ValueError):
    pass

def foo(s):
    n = int(s)
    if n == 0:
        raise FooError('invalid value: %s' % s)
    return 10/n

foo('0')

### 尽量使用Python内置的错误类型