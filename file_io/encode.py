#coding:gbk
import sys
print(sys.getdefaultencoding())
s = "你好"  # 默认unicode
s_to_gbk = s.encode("gbk")
s_to_utf8 =  s.encode("utf-8")
s_to_gb2312 = s_to_utf8.decode().encode("gb2312")
print(s_to_gbk)
print(s_to_utf8)
print(s_to_gb2312)
print(s_to_gb2312.decode("gb2312"))