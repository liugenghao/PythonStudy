__Author__ = 'Bill Lau'

import pika

connection = pika.BlockingConnection(pika.ConnectionParameters('localhost'))
channel = connection.channel()#声明一个管道

 #声明queue
channel.queue_declare(queue='Hello')

channel.basic_publish(exchange='',routing_key='Hello',body='Hello World')

print('[x] sent "Hello World!"')
connection.close()