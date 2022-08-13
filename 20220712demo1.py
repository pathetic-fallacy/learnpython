#-*- coding: utf-8 -*-

### list
classmates = ['first' , 'second' , 'third']
print(classmates[2])
print(classmates[-1])

classmates.append('fourth')
classmates.insert(0,'zero')
print(classmates)

print(classmates.pop())
print(classmates)

print(classmates.pop(2))
print(classmates)

classmates[0] = 'another'
print(classmates)

### tuple
classmates2 = ('first','second','third')
t = (1,)
t = ()

### input
#s = input('number:')
## 此时为str格式，可通过int(s)转换为int格式，但是对于int()，会在不是合法数字时报错，因此需要进行错误调试

### 循环
sum = 0
n = 99
while n > 0:
    sume = sum + n
    n = n - 2
print(sum)

L = ['one','two','three']
for x in L:
    print('hello,%s'%x)
## 不可滥用break与continue，尝试通过改写循环条件或修改循环逻辑，执行逻辑分叉过多容易出错