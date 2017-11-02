__Author__ = 'Bill Lau'

import gevent,time
from urllib import request
from gevent import monkey

monkey.patch_all()#当前程序所有的io操作加入gevent协程操作，加上标记
def f(url):
    print('GET: %s'%url)
    resp = request.urlopen(url)
    data = resp.read()
    filename = url[8:]
    if 'www' in filename:
        filename = filename[4:]
    filename = filename.split('.')[0] + '.html'
    # print(filename)
    with open(filename,'wb') as f:
        f.write(data)
        print('%d bytes received from %s.' % (len(data),url))
urls = ['https://www.python.org','https://www.yahoo.com','https://github.com']
startTime = time.time()
for i in urls:
    f(i)
print('同步costTime：',time.time() - startTime)
# f('http://blog.csdn.net/drdairen/article/details/51149498')0

async_time_start = time.time()
gevent.joinall([gevent.spawn(f,'https://www.python.org'),gevent.spawn(f,'https://www.yahoo.com'),gevent.spawn(f,'https://github.com')])
print("异步costTime：",time.time() - async_time_start)