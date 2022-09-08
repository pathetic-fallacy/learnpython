#-*- coding: utf-8 -*-
### 定制类

class Student():
    def __init__(self,name):
        self.name = name
    def __str__(self):
        return 'Student object (name:%s)' % self.name
    __repr__ = __str__

print(Student('Michael'))

### 直接显示变量调用的为__str__()，__str__返回用户所看到的字符串(使用print时)，repr()返回程序开发者看到的字符串，为调试服务
### 也可以再定义一个__repr__()

class Fib():
    def __init__(self):
        self.a,self.b = 0,1

    def __iter__(self):
        return self # 实例本身就是迭代对象，因此返回自己

    def __next__(self):
        self.a,self.b = self.b,self.a + self.b 
        if self.a > 100000: # 退出循环的条件
            raise StopIteration()
        return self.a # 返回下一个值

### 实现一个__iter__()方法返回一个迭代对象，之后不断调用该迭代对象的__next__()方法拿到循环的下一个值
### 可将类用于for...in循环，直到遇到StopIteration错误时退出循环

# for n in Fib():
#    print(n)

class Fib2():
    def __getitem__(self,n):
        a,b = 1,1
        for x in range(n):
            a,b = b,a+b
        return a

f2 = Fib2()
print(f2[100])

class Fib3():
    def __getitem__(self,n):
        if isinstance(n,int): # n为索引
            a,b = 1,1
            for x in range(n):
                a,b = b,a+b
            return a
        if isinstance(n,slice): # n为切片
            start = n.start
            stop = n.stop
            if start is None:
                start = 0
            a,b = 1,1
            L = []
            for x in range(stop):
                if x >= start:
                    L.append(a)
                a,b = b,a+b
            return L

f3 = Fib3()
print(f3[0:5])

### 此时虽然能进行切片处理，但还不能对step参数进行处理，也没有对负数进行处理
### 将对象看成dict，__getitem__()的参数可能是一个可以作key的object
### __setitem__()方法可将对象视作list或dict对集合进行赋值;__delitem__()用于删除某个元素
### 以上方法可将自己定义的类表现得与Python自带的list，tuple，dict功能相同，这是因为其不需要强制继承某个接口，动态语言

class Student():

    def __init__(self):
        self.name = 'Michael'
    
    def __getattr__(self,attr):
        if attr == 'score':
            return 99

s = Student()
print(s.score)

class Student2():

    def __getattr__(self,attr):
        if attr == 'age':
            return lambda:25
        raise AttributeError('\'Student\' Object has no attribute \'%s\'' % attr)

s2 = Student2()
print(s2.age())

class Chain():

    def __init__(self,path=''):
        self.path = path

    def __getattr__(self,path):
        return(Chain('%s/%s' % (self.path,path)))

    def __str__(self):
        return self.path

    __repr__ = __str__

print(Chain().status.user.timeline.list)

class Student3():
    
    def __init__(self,name):
        self.name = name
    
    def __call__(self):
        print('My name is %s.' % self.name)

s3 = Student3('Bart')
s3()

### 判断一个变量是对象还是函数/判断一个对象能否被调用：callable
print(callable(max))