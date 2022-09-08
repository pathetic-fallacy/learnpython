#-*- coding: utf-8 -*-
### 使用枚举类

### 对于枚举类型常量，定义一个class类型，每个常量都是class的一个唯一实例

from enum import Enum

Month = Enum('Month',('Jan','Feb','Mar','Apr','May','Jun','Jul','Aug','Sep','Oct','Nov','Dec'))
### 获得Month类型的枚举类，可直接使用Month.Jan来引用常量或枚举所有成员

for name,member in Month.__members__.items():
    print(name,'=>',member,',',member.value)

print(Month.Jan.value)

### value属性为自动赋给成员的int常量，默认从1开始计数
### 更精确地控制枚举类型，从Enum派生出自定义类

from enum import Enum,unique

@unique # 装饰器，检查保证没有重复值
class Weekday(Enum):
    Sun = 0
    Mon = 1
    Tue = 2
    Wed = 3
    Thu = 4
    Fri = 5
    Sat = 6

day1 = Weekday.Mon
print(day1)
print(Weekday.Tue)
print(Weekday['Tue'])
print(Weekday.Tue.value)
print(Weekday(1))