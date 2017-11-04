__Author__ = 'Bill Lau'
import pika,time

connection = pika.BlockingConnection(pika.ConnectionParameters('localhost'))

channel = connection.channel()

channel.queue_declare(queue='Hello')

def callback(ch,method,properties,body):#回调函数
    print("---->%s\n---->%s\n---->%s\n"%(ch,method,properties))
    print('[x] Received %r' % body)

    ch.basic_ack(delivery_tag=method.delivery_tag)#与服务器端确认任务完成

channel.basic_consume(callback,#如果收到消息，就调用callback函数来处理消息
                      queue='Hello')#,no_ack=True //确认消息完整性

print('[*] Waiting for messages. To exit press CTRL+C')
channel.start_consuming()