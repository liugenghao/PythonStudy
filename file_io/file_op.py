import sys,time
f = open("BubbleTea.bak","r+",encoding="utf-8")#r+ 读写

# f = open("BubbleTea","w+",encoding="utf-8")#r+ 写读
# f = open("BubbleTea","a+",encoding="utf-8")#r+ 追加读写

# print(f.readline())
# print(f.readline())
# print(f.readline())
# print(f.tell())
# f.write("-----------------")
# f.truncate(20)
# print(f.read())
# for i in range(50):
#     sys.stdout.write(">")
#     sys.stdout.flush()
#     time.sleep(0.2)
# print(f.readline())
# print(f.readline())
count = 0
for line in f:
    count += 1
    print(line)
print("LineNums:",count)
f.close()