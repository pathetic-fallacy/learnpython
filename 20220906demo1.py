#-*- coding: utf-8 -*-
### 获取对象信息

### 可使用type()函数判断基本类型，在if中判断需要比较两个变量的type类型是否相同

print(type(456)==int)

### 对class的继承关系，type()很不方便，可使用isinstance()
### 可使用type()时，基本也可使用isinstance()判断

print(isinstance(123,int))

print(isinstance([1,2,3],(list,tuple)))

### 可使用dir()获得一个对象的所有属性和方法，返回一个包含字符串的list

print(dir('ABC'))

### 类似__xxx__的属性和方法都在Python中有着特殊用途，如__len__返回长度
### 以下等价

len('ABC')
'ABC'.__len__()

### 自己所写的类，也可用len(myobj)，自己写一个__len__方法
class MyDog():
    def __len__(self):
        return 100

dog = MyDog()
print(len(dog))

### 配合getattr(),setattr()以及hasattr可以直接操作一个对象的状态：

class MyObject():
    def __init__(self):
        self.x = 9
    def power(self):
        return self.x * self.x

obj = MyObject()

### 操作一个对象的状态
hasattr(obj,'x') # 有属性'x'吗
print(obj.x)
setattr(obj,'y',19) # 设置一个属性'y'
getattr(obj,'y') # 获取属性'y'

print(getattr(obj,'z',404)) # 传入default参数，属性不存在，返回默认值404

### 只有在不知道对象信息时，才会去获取对象信息

def readImage(fp):
    if hasattr(fp,'read'):
        return readData(fp)
    return None