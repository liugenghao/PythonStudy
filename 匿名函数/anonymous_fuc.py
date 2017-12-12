__Author__ = "Bill Lau"

infos = [{'name':'Jim','age':32},{'name':'Peter','age':55},{'name':'Bill','age':21},{'name':'Susan','age':16},{'name':'Tom','age':28},{'name':'Rose','age':35},]

infos.sort(key=lambda x:x['name'],reverse=True)
print(infos)