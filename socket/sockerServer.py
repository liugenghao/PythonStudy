# Authot:Bill Lew

import socketserver

class MyTCPHandler(socketserver.BaseRequestHandler):
    def handle(self):
        try:
            while True:
                self.data = self.request.recv(1024).strip()
                print("{} wrote:".format(self.client_address[0]),self.data.decode())
                # if not self.data:
                #     print("数据传输错误")
                # print(self.data)
                self.request.sendall(self.data.upper())
        except ConnectionResetError as e:
            print("远程主机强迫关闭了一个现有的连接")

if __name__ == '__main__':
    HOST,PORT = '0.0.0.0',9999
    # server = socketserver.TCPServer((HOST,PORT),MyTCPHandler)
    server = socketserver.ThreadingTCPServer((HOST,PORT),MyTCPHandler)#多线程
    # server = socketserver.ForkingTCPServer((HOST,PORT),MyTCPHandler)#多进程（windows无法使用）
    print('服务器已启动，监听中...')
    server.serve_forever()
