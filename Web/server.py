__Author__ = 'Bill Lau'

from wsgiref.simple_server import make_server
from controller import account

URL_DICT ={
    '/index':account.handle_index,
    '/date':account.handle_date
}
def RunServer(environ, start_response):
    #environ 客户端发来的所有数据
    #start_response 封装要返回给用户的数据，响应头状态
    start_response('200 OK',[('Content_Type','text/html')])
    current_url = environ['PATH_INFO']
    func = None
    if current_url in URL_DICT:
        func = URL_DICT[current_url]
    if func:
        return func()
    else:
        return ['<h1>404</h1>'.encode('utf-8')]
    #返回的内容
    # return '<h1>Hello Web!</h1>'#python2
    return ['<h1>Hello Web!</h1>'.encode('utf-8')]#python3

if __name__ == '__main__':
    httpd = make_server('',8000,RunServer)
    print('Serving HTTP on port 8000')
    httpd.serve_forever()