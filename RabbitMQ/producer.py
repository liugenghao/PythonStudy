__Author__ = 'Bill Lau'

import pika

connection = pika.BlockingConnection(pika.ConnectionParameters('localhost'))
channel = connection.channel()#声明一个管道

 #声明queue
channel.queue_declare(queue='Hello',durable=True)#durable=True队列持久化

channel.basic_publish(exchange='',routing_key='Hello',body='Hello World',properties=pika.BasicProperties(delivery_mode=2))#delivery_mode=2消息持久化

print('[x] sent "Hello World!"')
connection.close()