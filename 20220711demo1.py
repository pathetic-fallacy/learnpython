### 申明utf-8
#-*- coding: utf-8 -*-

### 字符串与编码

print('I\'m ok.')
print('I\'m learning\nPython.')
print('\\\n\\')
print('\\\t\\')
print(r'\\\t\\')
print('''LINE1
LINE2
LINE3''')
print(r'''hello,\n
world''')

print(True and False , True or False , not False )

print(None)

print(10 / 3 , 9 / 3 , 10  //  3 , 10 % 3)

print('\u4e2d\u6587')

print('abc'.encode('ascii'))
print(b'abc'.decode('ascii'))
print(len('中'))

print('Hello, %s' %'world')
print('%d %%' % 7)
print('%%')

print('%2d-%03d' %(3,1))
print('%.2f' % 3.1415926)

r = 2.5
s = 3.14 * r ** 2
print(f'the area of a circle with radius {r} is {s:.2f}')