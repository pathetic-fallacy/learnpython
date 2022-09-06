#-*- coding: utf-8 -*-
### 实例属性和类属性

### 依据类创建的实例可以任意绑定属性
### 通过实例变量或self变量

from unicodedata import name


class Student():
    def __init__(self,name):
        self.name = name

s = Student('Bob')
s.score = 90

### 直接在class中定义属性，给类绑定属性

class Student():
    name = 'Student'

s = Student()
print(s.name) # 打印name属性，由于实例中没有name属性，会继续查找class的name属性
print(Student.name) # 直接打印类的name属性
s.name = 'Michael' # 给实例绑定name属性，实例属性优先级高于类属性，对于实例屏蔽掉类的name属性
del s.name # 删除实例的name属性

###### 统计学生人数，可给Student类增加一个类属性，每创建一个实例，该属性自动增加：

class Student():
    count = 0

    def __init__(self,name):
        self.name = name
        Student.count += 1
### 关键在于用什么变量记录实例化函数的运行次数，类属性使用类名.属性名进行调用，在封装的内部与外部一致如此