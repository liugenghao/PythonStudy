
name = "liu\tgenghao"
sentence = "My name is {name},{age} years old"
print(name.capitalize())
print(name.count("g"))
print(name.center(50,"-"))
print(name.ljust(20,"*"))
print(name.rjust(20,"*"))

print(name.endswith("o"))
print('-----------',name.startswith("i"))
print(name.expandtabs(tabsize=10))
print(name[name.find("h"):])
print(sentence.format(name='Bill',age=23))
print(sentence.format_map({'name':'Bill','age':28}))
print("ab23".isalnum())
print("a".isdecimal())
print("0.223".isdigit())
print("aA".isalpha())
print("_aA".isidentifier())
print("+".join(['1','2','3','4']))

print("LEW".lower())
print("lew".upper())
print("Lew\n".strip())
print("---")
print("samsung".replace("s","x",1))
print("hallo hall".rfind("l"))
p = str.maketrans("abcde","12345")
print("axdkne".translate(p))


print("1+2+3+4".split("+"))
print("1+2\n+3+4".splitlines())
print("Find Your Weapon".swapcase())
print("tilte test.txt ok".title())
print(b'like')