# Author:Bill Lew
import socket
import json
import os

class FtpClient(object):
    def __init__(self):
        self.client = socket.socket()
    def help(self):
        msg = ''
    def connect(self,ip,port):
        # self.client.connect(('192.168.6.130', 9999))
        self.client.connect((ip, port))
    def interactive(self):
        #self.authenticate()
        while True:
            cmd = input(">>:").strip()
            if len(cmd) == 0:continue
            cmd_str = cmd.split()[0]
            if hasattr(self,'cmd_%s'%cmd_str):#反射
                func = getattr(self,'cmd_%s'%cmd_str)
                func(cmd)
            else:
                self.help()
    def cmd_put(self,*args):
        cmd_split = args[0].split()
        if len(cmd_split) > 1:
            filename = cmd_split[1]
            if os.path.isfile(filename):
                filesize = os.stat(filename).st_size
                msg_dic = {
                    "action":"put",
                    "filename":filename,
                    "size":filesize,
                    "overridden":True
                }
                self.client.send(json.dumps(msg_dic).encode())
                #防止粘包，等服务器验证
                server_response = self.client.recv(1024)
                f = open(filename,'rb')
                for line in f:
                    self.client.send(line)
                else:
                    print("发送完毕")
                    f.close()
            else:
                print(filename,'is not exist')
    def cmd_get(self):
        pass

ftp = FtpClient()
ftp.connect('192.168.6.130',9999)
ftp.interactive()