
items = [("Iphone",6888),("Samsung s8+",6288),("XiaoMi Mix2",3299),("Huawei P10",4888),("Meizu Pro7",2599)]

salary = input("Input your Salary:")
if salary.isdigit():
    salary = int(salary)
    shopping_list = []
while True:
    print("------Your Balance:\033[31;1m%d\033[0m"%(salary),"-------")
    for index,item in enumerate(items):
        print(index+1,item)
    choice = input("选择你要买的商品：")
    if choice.isdigit():
        choice = int(choice)
        if choice <= len(items) and choice > 0:
            p_item = items[choice-1]
            if p_item[1] <= salary:
                salary -= p_item[1]
                shopping_list.append(p_item)
                print("购买了%s，余额为：%d"%(p_item[0],salary))
            else:
                print("\033[31;1m余额不足\033[0m")
        else:
            print("编码有误，请重新输入")
    elif choice == "q":
        print("Exit")
        break
    else:
        print("Invalid option")
    print("-----------已购买的产品------------")
    for index, item in enumerate(shopping_list):
        print("\033[46;1m%s\033[0m" %(item[0]),"|",end="")
    print("")