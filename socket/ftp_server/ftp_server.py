import socket,os,hashlib

server = socket.socket()
server.bind(('localhost',9999) )

server.listen()
print('开始监听...')
while True:
    try:
        conn, addr = server.accept()
        print("new conn:",addr)
        while True:
            print("等待新指令")
            data = conn.recv(1024)
            print(data.decode())
            if not data:
                print("客户端已断开")
                break
            cmd,filename = data.decode().split()
            print(filename)
            if os.path.isfile(filename):#检测文件是否存在
                print("'%s'文件存在，准备下载..."%filename)
                f = open(filename,'rb')#打开文件
                m = hashlib.md5()
                file_size = os.stat(filename).st_size#检测文件大小
                conn.send(str(file_size).encode())#发送文件大小给客户端
                conn.recv(1024)#等待客户端确认
                for line in f:#发送文件
                    m.update(line)#md5加密
                    conn.send(line)
                md5info = m.hexdigest()
                print("file md5",md5info)
                f.close()
                conn.send(md5info.encode())#发送md5校验码给客户端
            print("Send done")
    except ConnectionResetError as e:
        print("客户端失去连接")
server.close()