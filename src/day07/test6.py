# 元组
t = (1, 'dwk', 'apple')
print(t)
print(type(t))
print(t[0])
# 重新赋值，前一个会被垃圾回收
t = (2, False, 'apple')
# 元组转换为列表
persion = list(t)
persion.append('banana')
print(persion)
# 删除列表指定元素
persion.pop(len(persion) - 2)
# 列表转换为元组
_turle = tuple(persion)
print(_turle)
print("==================================")
# 集合
_set = {1, 2, 3, 4, 5}
print(_set, 'length:', len(_set))
_set1 = set(range(1, 10))
print(_set1, 'length:', len(_set1))
set3 = set((1, 2, 3, 3, 2, 1))
print(_set, set3)
# 创建集合的推导式语法(推导式也可以用于推导集合)
set4 = {num for num in range(1, 100) if num % 3 == 0 or num % 5 == 0}
print(set4)
print("============================集合删除=====================================")
if 1 in _set:
    #删除元素1，如果不存在，会报错
    _set.remove(1)
print(_set)
#删除元素5，如果不存在，不会报错
_set.discard(5)
#增加元素1
_set.update([1])
print(_set)
print(_set1)
print("=========================交集======================================")
#两个集合的交集,也可这样写print(_set.intersection(_set1))
#_set:{2, 3, 4, 1,10086},_set1:{1, 2, 3, 4, 5, 6, 7, 8, 9}
#result:{1, 2, 3, 4}
print(_set & _set1)
print("========================合集===========================================")
#两个集合的合集，也可这样写print(_set.union(_set1))
#_set:{2, 3, 4, 1,10086},_set1:{1, 2, 3, 4, 5, 6, 7, 8, 9}
#result:{1, 2, 3, 4, 5, 6, 7, 8, 9,10086}
print(_set | _set1)
print("========================差集===========================================")
#两个集合的差集，也可这样写print(_set.difference(_set1))
print(_set - _set1)
print("========================对称差集===========================================")
#两个集合的对称差集，也可这样写print(set1.symmetric_difference(set2))
print(_set ^ _set1)
# print(set1.symmetric_difference(set2))
print("========================判断子集===========================================")
# 判断子集和超集
print(_set <= _set1)
# print(set2.issubset(set1))
print(_set1 <= _set)
# print(set3.issubset(set1))
print("========================判断超集===========================================")
print(_set >= _set1)
# print(set1.issuperset(set2))
print(_set1 >= _set)
# print(set1.issuperset(set3))