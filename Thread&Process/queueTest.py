# Authot:Bill Lew

import queue
# q = queue.Queue(maxsize=2)
q = queue.Queue()#堆
q.put("d1")
q.put("d2")
q.put("d3")

print(q.qsize())
print(q.get())
print(q.get())
print(q.get())


q2 = queue.LifoQueue()#栈
q2.put(1)
q2.put(2)
q2.put(3)

print(q2.get())
print(q2.get())
print(q2.get())

q3 = queue.PriorityQueue()#可设定优先级,自动排序
q3.put((-1,'Lau'))
q3.put((9,'Li'))
q3.put((5,'Jim'))
q3.put((3,'Alex'))

print(q3.get())
print(q3.get())
print(q3.get())
print(q3.get())