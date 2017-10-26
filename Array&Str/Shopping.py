# Author:Bill Lew

salary  = int(input("Iput Your Salary:"))
productList = (["Iphone",5666],["Mac Pro",12800],["Samsung S8+",6288],["Bike",1320],["Samsung HardDisk",590])
while salary > 0:
    print("----Your Account Balance:",salary,"-----")
    info = '''----product list-----
            1.%s -- %d
            2.%s -- %d
            3.%s -- %d
            4.%s -- %d
            5.%s -- %d
    ''' %(productList[0][0],productList[0][1],
          productList[1][0],productList[1][1],
          productList[2][0],productList[2][1],
          productList[3][0],productList[3][1],
          productList[4][0], productList[4][1],)
    print(info)
    count = int(input("Enter product num:"))
    if count < 6:
        print("Your Choice is:", productList[count - 1][0], ",Price is:", productList[count - 1][1])
        salary -= productList[count-1][1]
    else:
        print("Wrong Number,Try again!")
print("Insufficient Balance")