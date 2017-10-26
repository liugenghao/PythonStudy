# Author:Bill Lew

import sys
import os
print(sys.path)
print(sys.argv)

# cmd_res = os.system("dir")
cmd_res = os.popen("dir")
print("----->>",cmd_res.read())