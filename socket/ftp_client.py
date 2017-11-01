import socket,hashlib
client = socket.socket()

#client.connect(('192.168.16.200',9999))
client.connect(('localhost',9999))

while True:
    cmd = input(">>:").strip()
    if len(cmd) == 0: continue
    if cmd.startswith('get'):
        client.send(cmd.encode())
        server_response = client.recv(1024)
        print("server response:",server_response)
        client.send('ready to recv file'.encode())
        file_total_size = int(server_response.decode())
        received_size = 0
        filename = cmd.split()[1]
        f = open(filename,'wb')
        m = hashlib.md5()
        while received_size < file_total_size:
            differ = file_total_size - received_size
            if differ > 1024:
                size = 1024
            else:
                size = differ
            data = client.recv(size)
            received_size += len(data)
            m.update(data)
            f.write(data)
            # print('File_Total_Size:%s,Receive_File_Size:%s'%(file_total_size,received_size))
        else:
            print("file recv done")
        new_file_md5 = m.hexdigest()
        f.close()
    server_file_md5 = client.recv(1024).decode()
    print("server file md5:",server_file_md5)
    print("new file md5",new_file_md5)
    if server_file_md5 == new_file_md5:
        print('文件传输完毕')
    else:
        print('md5校验失败')
client.close()