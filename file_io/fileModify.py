
f = open("BubbleTea",'r',encoding='utf-8')
f_new = open("BubbleTea.bak",'w',encoding='utf-8')
# with open("BubbleTea.bak",'w',encoding='utf-8') as f_new: #后台自动关闭文档
print(f.read())
f.seek(0)
key = input("搜索:")
for line in f:
    if key in line:
        replaceKey = input("输入你想替换的词:")
        line = line.replace(key,replaceKey)
    f_new.write(line)
f_new = open("BubbleTea.bak", 'r', encoding='utf-8')
print(f_new.read())
f.close()
f_new.close()