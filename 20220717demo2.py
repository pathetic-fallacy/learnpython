#-*- coding: utf-8 -*-

### sorted 用于排序
print(sorted([36,5,-9,27,-12]))
print(sorted([36,5,-9,27,-12],key = abs))
print(sorted(['bob','about','Zoo','Credit']))
print(sorted(['bob','about','Zoo','Credit'],key = str.lower))
print(sorted(['bob','about','Zoo','Credit'],key = str.lower,reverse=True))

L = [('Bob', 75), ('Adam', 92), ('Bart', 66), ('Lisa', 88)]
def by_name(t):
    return t[0].lower()
def by_score(t):
    return t[1]
L1 = sorted(L, key=by_name)
print(L1)
L2 = sorted(L, key=by_score,reverse=True)
print(L2)