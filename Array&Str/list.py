# Author:Bill Lew
import copy

names = ["ZhangYang","Guyun",["Alex","Bill"],"XuLiangChen"]
names.append("LiuYunPeng")
names.insert(1,"LiShangMing")
print(names)
# print(names[0],names[2])
# print(names[1:-1:2])
# print(names[-1])
# print(names[-2])
# print(names[-2:])
# print(names.index("XuLiangChen"))
names.pop(names.index("XuLiangChen"))
# names.sort()
# names2 = copy.copy(names)
names2 = copy.deepcopy(names)
names[0] = "张扬"
names[3][0] = "A"

print(names)
print(names2)
print(names[::2])