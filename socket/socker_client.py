
import socket

client = socket.socket()
client.connect(('192.168.6.130',9999))
# client.connect(('localhost',9999))

while True:
    msg = input("输入发送的内容：")
    if len(msg) == 0:continue
    client.send(msg.encode())
    data = client.recv(1024)
    print("recv:",data.decode())
client.close()