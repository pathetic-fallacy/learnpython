#-*- coding: utf-8 -*-

### 面向过程的程序设计，以函数作为程序设计的基本单元
### 函数式编程，抽象程度很高的编程范式，多个函数的嵌套调用，开闭原则
### 高阶函数，函数的参数可接受别的函数

## map
def f(x):
    return x * x
r = map(f,range(1,10))
print(list(r))

## reduce
from functools import reduce
def add(x,y):
    return x+y
r1 = reduce(add,[a for a in range(1,10) if a % 2 !=0])
print(r1)

def normalize(name):
    return name.title()
L1 = ['adam', 'LISA', 'barT']
L2 = list(map(normalize, L1))
print(L2)

def prod(L):
    return reduce(lambda x,y:x*y,L)
print('3 * 5 * 7 * 9 =', prod([3, 5, 7, 9]))
if prod([3, 5, 7, 9]) == 945:
    print('测试成功!')
else:
    print('测试失败!')

num_dict = {'0': 0, '1': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9}
def char2num(s):
    return num_dict[s]
def str2float(s):
    s1, s2 = s.split('.')
    print(s1,s2)
    return reduce(lambda x, y: x * 10 + y, map(char2num, s1)) + reduce(lambda x, y: x / 10 + y, map(char2num, s2[::-1])) / 10
print('str2float(\'123.456\') =', str2float('123.456'))