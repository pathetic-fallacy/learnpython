#-*- coding: utf-8 -*-

try:
    print('try...')
    r = 10 / 0
    print('result:',r)
except ZeroDivisionError as e:
    print('except:',e)
finally:
    print('finally...')
print('END')

try:
    print('try...')
    r = 10 / int('a')
    print('result:',r)
except ZeroDivisionError as e:
    print('ZeroDivisionError:',e)
except ValueError as e:
    print('ValueError:',e)
finally:
    print('finally...')
print('END')

try:
    print('try...')
    r = 10 / int('2')
    print('result:',r)
except ZeroDivisionError as e:
    print('ZeroDivisionError:',e)
except ValueError as e:
    print('ValueError:',e)
else:
    print('no error!')
finally:
    print('finally...')
print('END')

### Python的错误也是class，错误类型继承自BaseException，except捕捉该类型错误及其子类

import logging

def foo(s):
    return 10/int(s)

def bar(s):
    return foo(s) * 2

def main():
    try:
        bar('0')
    except Exception as e:
            print('Error:',e)
            logging.exception(e) #记录错误信息，通过配置，logging还可将错误记录到日志文件中方便事后排查
    finally:
        print('finally...')

main()
### 可实现跨越多层调用
### 如果错误没有被捕获，会一直往上抛，最终被Python解释器捕获打印一个错误的信息
### 可通过分析错误的调用栈信息，定位错误的位置