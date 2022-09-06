#-*- coding: utf-8 -*-
### 类和实例，访问限制

std1 = {'name':'Michael','score':98}
std2 = {'name':'Bob','score':81}

def print_score(std):
    print('%s:%s'%(std['name'],std['score']))

print_score(std1)

class Student():

    def __init__(self,name,score):
### 注意_特殊方法__init__前后分别有两个下划线
### 第一个参数永远是self，表示创建的实例本身，__init__方法内部将各种属性绑定到self，self无需传
        self.__name = name
        self.__score = score
### 在属性的名称前加上两个下划线，成为私有变量，只有内部可以访问，外部不能访问，防止外部代码随意修改对象内部的状态
    def print_score(self):
        print('%s:%s'%(self.__name,self.__score))
    
    def get_grade(self):
        if self.__score >= 90:
            return 'A'
        elif self.__score >=60:
            return 'B'
        else:
            return 'C'
    
    def get_name(self):
        return self.name

    def get_score(self):
        return self.__score
### 补充从外部代码获取私有变量的方法
    
    def set_score(self,score):
        if 0 <= score <= 100:
            self.score = score
        else:
            raise ValueError('bad score')
### 补充从外部修改私有变量的方法
### 在方法中可对参数进行检查，避免输入无效参数

### __xxx__，特殊变量，可直接进行访问，不能用；_xx，外部可访问，但请不要随意访问；
### __xxx不能直接访问是因为Python解释器对外将__xxx变量改成了_Studen__xxx，仍可进行访问，不同版本所改可能不同

bart = Student('Bart Simpson',59)
lisa = Student('Lisa Simpson',87)
bart.print_score()
lisa.print_score()

print(bart)

print (lisa.get_grade())