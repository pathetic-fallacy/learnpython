#-*- coding: utf-8 -*-
### 多重继承，在不同分类有多重交叉的情况下使用
### 如：动物-(鸟-鸵鸟/鹦鹉)/(哺乳-狗/蝙蝠)与动物-(跑-鸵鸟/狗)/(飞-鹦鹉/蝙蝠)等多种分类存在时

### 主要层次按哺乳与鸟进行分类

class Animal():
    pass

class Mammal(Animal):
    pass

class Bird(Animal):
    pass

class Dog(Mammal):
    pass

class Bat(Mammal):
    pass

class Parrot(Bird):
    pass

class Ostrich(Bird):
    pass

### 想要给动物加上Runnable与Flyable的功能，只需要定义好对应的类

class Runnable():
    def run(self):
        print('running...')

class FlyableMixIn():
    def fly(self):
        print('Flying...')

### 对需要相应功能的动物，则多继承一个类

class Dog(Mammal,Runnable):
    pass
### 即通过多重继承，一个子类同时获得多个父类的所有功能，MixIn即非单一主线继承

class Bat(Mammal,FlyableMixIn):
    pass

### 如此，不要复杂庞大的继承链，只需选择组合不同的类的功能，来快速构造出所需的子类