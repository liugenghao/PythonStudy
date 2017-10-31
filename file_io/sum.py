# Author:Bill Lew

data = [
            {'value':48417, 'name':'江苏省'},
                {'value':35285, 'name':'广东省'},
                {'value':32957, 'name':'浙江省'},
                {'value':16436, 'name':'上海市'},
                {'value':13810, 'name':'湖北省'},
                {'value':7728, 'name':'山东省'},
                {'value':17536,'name':'北京市'},
                {'value':6949, 'name':'福建省'},
                {'value':6715, 'name':'安徽省'},
                {'value':6487, 'name':'河南省'},
                {'value':16069, 'name':'其他'}]

sum = 0
for k in data:
    sum += k['value']
print(sum)