#-*- coding: utf-8 -*-

### err_reraise.py

def foo(s):
    n = int(s)
    if n == 0:
        raise ValueError('invalid value: %s' % s)
    return 10/n

def bar():
    try:
        foo('0')
    except ValueError as e:
        print('valueError')
        raise

bar()

### 捕获错误用于记录，将该错误上抛，让顶层调用者进行处理

try:
    10/0
except ZeroDivisionError:
    raise ValueError('input error')
### raise语句不带参数为将当前错误原样抛出，在except中raise一个Error可将错误类型转化