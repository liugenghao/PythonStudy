__Author__ = "Bill Lau"
import time
def handle_index():
    v = time.strftime('%Y-%m-%d %H:%M:%S',time.localtime(time.time()))
    f = open('View/index.html',mode='rb')
    data = f.read()
    f.close()
    data = data.replace(b'@uuu',v.encode('utf-8'))
    return [data,]
def handle_date():
    return ['<h1>Hello,Date!</h1>'.encode('utf-8')]