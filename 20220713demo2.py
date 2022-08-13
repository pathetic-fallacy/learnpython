#-*- coding: utf-8 -*-

### 函数参数
## 将函数内部的复杂逻辑进行封装

## from xxx import yy/导入xxx.py文件中的yy函数

## 位置参数
def power(x,n):
    s = 1
    while n>0:
        n = n-1
        s = s * x
    return s
print(power(2,5))
## 同一程序中，使用函数需在函数定义后

## 默认参数
def power1(x,n = 3):
    s = 1
    while n>0:
        n = n-1
        s = s * x
    return s
print(power1(3))
## 默认参数必须指向不变对象 None，str等

## 可变参数
def calc(numbers):
    sum = 0
    for n in numbers:
        sum = sum + n * n
    return sum
print(calc([1,2,3]))

def calc1(*numbers):
    sum = 0
    for n in numbers:
        sum = sum + n * n
    return sum
print(calc1(1,2,3))

nums = [1,2,3]
print(calc1(*nums))

## 关键字参数，在函数内部组装为dict，可变参数组装为tuple
def person(name,age,**kw):
    print('name:',name,'age:',age,'other:',kw)
person('A',18)
person('a',19,city='b',job='c')
extra = {'city':'b','job':'c'}
person('a',20,**extra)

## 命名关键字参数,限制调用者可传入的参数名，同时可提供默认值
def person1(name,age,*,city,job):
    print(name,age,city,job)
person1('a',20,job='no',city='beijing')

## practice
def mul(x,*args):
    for i in args:
        x = x * i
    return x

print('mul(5,6,7)=',mul(5,6,7))