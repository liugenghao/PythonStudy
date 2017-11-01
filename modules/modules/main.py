import os
import sys
import module_bill

print(module_bill.name)
# module_bill.billP()
path = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
print(path)

sys.path.append(path)
print(sys.path)