#-*- coding: utf-8 -*-
### 继承与多态

class Animal():
    
    def run(self):
        print('Animal is running...')

class Cat(Animal):

    def run(self):
        print('Cat is running...')

class Dog(Animal):

    def run(self):
        print('Dog is running...')
    def eat(self):
        print('Eating meat...')


dog = Dog()
dog.run()

cat = Cat()
cat.run()

a = list()
b = Animal()
c = Dog()

print(isinstance(a,list))
print(isinstance(b,Animal))
print(isinstance(c,Dog))

print(isinstance(c,Animal))

def run_twice(animal):
    animal.run()
    animal.run()

run_twice(Animal())
### 传入Animal的实例

run_twice(Dog())
### 任何依赖Animal作为参数的函数或者方法都可以不加修改地正常运行———多态
### 开闭原则：对扩展开放：允许新增Animal子类；对修改封闭：不需要修改依赖Animal类型的run_twice()等函数
### 对于静态语言(java等)，需要传入Animal类型，传入的对象必须是Animal类型或者它的子类，调用run()方法；
### 对于Python这样的动态语言，不一定需要传入Animal类型，只需要保证传入对象有一个run()方法