#-*- coding: utf-8 -*-

### dict
## key-value储存，相较于list，插入与查找速度快,内存占用大
d = {'first':1,'second':2,'third':3}
print(d['first'])
d['first'] = 0
print(d['first'])

print('second' in d)
print(d.get('zero',-1))
print(d.get('zero'))
## dict的key为不可变对象

### set
s = set([1,2,3])
print(s)
s.add(3)
print(s)
s.remove(3)
print(s)
s0 = set([2,3,4])
print(s & s0)
print(s | s0)
## set仍然也为key的集合，不存储value，不可放入可变对象