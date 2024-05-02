import pika

# RabbitMQ 서버에 연결합니다.
connection = pika.BlockingConnection(pika.ConnectionParameters('localhost'))
channel = connection.channel()

# 큐를 생성합니다.
channel.queue_declare(queue='my_queue')

# 메시지를 전송합니다.
message = 'Hello, RabbitMQ!'
channel.basic_publish(exchange='', routing_key='my_queue', body=message)

print("Message sent:", message)

# 연결을 닫습니다.
connection.close()
