
import functools
print(all((1,0,-1)))#可迭代元素中所有元素为真则返回真
print(any((1,0,-1)))#可迭代元素中有任意一个元素为真则为真
# with open('GeneratorParallel.py',encoding="utf-8") as f:
#     exec(f.read())
calc = lambda n : print(n)# 匿名函数
calc(5)
# res = filter(lambda n:n>5,range(10))
res = map(lambda n:n*n,range(10))
for index,item in enumerate(res):
    print(index,item)
res2 = functools.reduce(lambda x,y:x+y,range(5))
print(res2)
a={6:2,3:4,5:9,4:2,7:21,11:2,10:31}
print(sorted(a.items(),key=lambda x:x[1]))
