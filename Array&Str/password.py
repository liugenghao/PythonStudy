import getpass
G = 50
count = 0
while count<3:
    age = int(input("age:"))
    if age > 50:
        print("too big")
    elif age == 50:
        print("right!")
        break
    else:
        print("too small")
    count += 1