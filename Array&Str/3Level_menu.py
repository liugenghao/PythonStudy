# Authot:Bill Lew

data = {
    "湖北":{"宜昌":{"夷陵区":["小溪塔","龙泉"]},"武汉":{"武昌":["洪山","街道口"]}},
    "北京":{"东城":{"长安街":["天安门","王府井"]},"宣武":{"望京":["西二旗","花家地"]}},
    "浙江":{"杭州":{"下城区":["桐庐","相安"]},"西湖区":{"洪野":["滨江","珙桐"]}},
}
exit_flag = False
while not exit_flag:
    for i in data:
        print(i)

    choice = input("请选择1>>>")
    if choice in data:
        while not exit_flag:
            for i2 in data[choice]:
                print("\t",i2)
            choice2 = input("请选择区域2>>>按'b'返回上一层")
            if choice2 == 'b':
                break
            if choice2 in data[choice]:
                while not exit_flag:
                    for i3 in data[choice][choice2]:
                        print("\t\t",i3)
                    choice3 = input("请选择区域3>>>按'b'返回上一层")
                    if choice3 == 'b':
                        break
                    if choice3 in data[choice][choice2]:
                        while not exit_flag:
                            for i4 in data[choice][choice2][choice3]:
                                print("\t\t\t",i4)
                            choice4 = input("按'b'返回上一级>>>按'q'退出")
                            if choice4 == 'b':
                                break;
                            if choice4 == 'q':
                                exit_flag = True