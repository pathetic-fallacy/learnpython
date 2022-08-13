#-*- coding: utf-8 -*-

### 高级特性 将代码简单化

## 切片 Slice
L = list(range(100))
print(L[1:3])
print(L[:3])
print(L[-2:])
print(L[:10:2])
print(L[::5])
# tuple同样可进行切片，操作结果仍为tuple，字符串亦然
## 去除空格的practice
def trim(s):
    while s[:1] == ' ':
        s = s[1:]
    while s[-1:] == ' ':
        s = s[:-1]
    return s
print(trim('   aaa  '))

## 迭代 lteration for...in 循环具有更高的抽象程度

## 除有下标的list,tuple外，还可作用于其他可迭代对象（dict等）
# dict并不按照list的方式顺序排列，迭代出的结果顺序可能不同
# 默认情况下，dict迭代的为key，可使用for value in d.values来迭代value，使用for k,v in d.items来同时迭代key与value

## 可通过collections.abc模块的Iterable类型进行判断
from collections.abc import Iterable
from typing import Iterator
print(isinstance([1,2,3],Iterable))
print(isinstance(123,Iterable))

for x,y in [(1,1),(2,4),(3,9)]:
    print(x,y)

def findMinAndMax(L):
    if L == []:
        print(None,None)
    else:
        print(min(L),max(L))
findMinAndMax([7,3,1,19,5])

## 列表生成式
print(list(range(1,11)))
print([x * x for x in range(1,11)])
print([x * x for x in range(1,11) if x % 2 == 0])
# 在列表生成式中 for前面的if...else为表达式，for后面的if为过滤条件，不能带else
print([m + n for m in 'ABC' for n in 'XYZ'])
d = {'x':'1','y':'2','z':'3'}
print([a + '=' + b for a,b in d.items()])
L = ['PA','CE','DH']
print([s.lower() for s in L])

L1 = ['Hello','World',18,'Apple',None]
L2 = [x for x in L1 if isinstance(x,str)]
print(L2)

## 生成器：generator，一边循环一边计算的机制，不必创建完整的list，节省大量的空间
L = [x * x for x in range(10)]
g = (x * x for x in range(10))
print(next(g))
print(next(g))
for n in g:
    print(n)
# 推算算法复杂，列表生成式的list循环无法实现时，可通过函数来实现
def fibl(max):
    n,a,b = 0,0,1
    while n< max:
        print(b)
        a,b = b,a+b
        n = n+1
    return 'done'
def fibg(max):
    n,a,b = 0,0,1
    while n< max:
        yield b
        a,b = b,a+b
        n = n+1
    return 'done'
def odd():
    print('step1')
    yield 1
    print('step2')
    yield (3)
    print('step3')
    yield (5)
o = odd()
print(next(o))
print(next(o))
# 调用generator会创建一个generator对象，多次调用对应函数会创建多个相互独立的generator
print(next(odd()))
print(next(odd()))
for n in fibg(8):
    print(n)
def triangles():
    L = [1]
    while True:
        yield L
        L = [1] + [L[n] + L[n+1] for n in range(len(L)-1)] + [1]
n = 0
results = []
for t in triangles():
    results.append(t)
    n = n + 1
    if n == 10:
        break
for t in results:
    print(t)

## 可迭代对象：Iterable，可直接作用于for循环
## 迭代器：Iterator，可被next()函数调用并不断返回下一个值的对象
print(isinstance(iter('abc'),Iterator))
## Iterator对象表示的是一个数据流,惰性计算的序列
# python的for循环本质为通过不断调用next(函数)实现