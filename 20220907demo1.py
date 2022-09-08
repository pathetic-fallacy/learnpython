#-*- coding: utf-8 -*-
### 面向对象的高级特性

class Student():
    pass

s = Student()
s.name = 'Michael' # 动态给实例绑定一个属性

def set_age(self,age):
    self.age = age

from types import MethodType
s.set_age = MethodType(set_age,s) # 给实例绑定一个方法

def set_score(self,score):
    self.score = score

Student.set_score = set_score # 给类绑定方法
### 动态绑定允许在程序与性的过程中动态给class加上功能，在静态语言中很难实现

### __slots__ 限制class实例能添加的属性

class Student():
    __slots__ = ('name','age') # 用tuple定义允许绑定的属性名称
### __slots__定义的属性仅对当前类实例起作用，对继承的子类不起作用
### 如对继承的子类中也定义__slots__，子类实例允许定义的属性即为自身的__slots__加上父类的__slots__

### @property装饰器可将方法变成属性调用
class Student():

    @property
    def score(self):
        return self._score
    
    @score.setter
    def score(self,value):
        if not isinstance(value,int):
            raise ValueError('score must be an integer!')
        if value < 0 or value >100:
            raise ValueError('score must between 0~100')
        self._score = value
### 将getter方法变为属性，只需要加上@property，@property本身又创建了另一个装饰器@score,setter，负责把另一个setter方法变为属性赋值

s = Student()
s.score = 60 # 实际转化为s.set_score(60)
s.score # 实际转化为s.get_score()

### 通过只定义getter方法，不定义setter方法，即只读属性
### 属性的方法名不要和实例变量重名，例如line34与line42中的_score不可写作score，否则在执行return self.birth时，视为访问self的属性
### 此时转化为方法调用，造成无限递归