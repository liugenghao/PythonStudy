# Authot:Bill Lew
import socket
server = socket.socket()
server.bind(('localhost',9999))
server.listen(5)
print('开始监听...')
while True:
    conn, addr = server.accept()
    print('开始连接...')
    try:
        while True:
            data = conn.recv(1024)
            print('消息:',data.decode())
            conn.send(data)
    except ConnectionResetError as e:
            print('客户端断开连接')
server.close()