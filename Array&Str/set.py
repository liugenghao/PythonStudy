# Authot:Bill Lew

list1 = [1,3,2,4,5,6,3,2,4,6,7,7,9]
print(list1)
list1 = set(list1)
print("list1:",list1)

list2 = set([2,5,66,6,3,22,0])
print(list1,list2)

print(list1.intersection(list2))#交集
print(list1.union(list2))#并集
print(list1.difference(list2))#差集
print(list2.difference(list1))

list3 = set([1,3,7])
print(list3.issubset(list1))
print(list1.issuperset(list3))