# Authot:Bill Lew

info = {
    "a":1,
    "b":2,
    "c":3
}
info2 ={
    "a":"modify",
    "d":4,
    "e":5
}
info.update(info2)
# print(info)
# del info["a"]
#
# print(info)

# info.pop('c')
info.popitem()
print(info)
print(info.items())
print(info.get("c"))
print(info.get("a"))

print("a" in info)

c = dict.fromkeys(["dict01","dict02","dict03"],"item")
print(c)

for i in c:
    print(i,c[i])