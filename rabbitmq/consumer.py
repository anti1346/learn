import pika

def callback(ch, method, properties, body):
    # 메시지 처리 로직을 작성합니다.
    print("Received message:", body.decode())

# RabbitMQ 서버에 연결합니다.
connection = pika.BlockingConnection(pika.ConnectionParameters('localhost'))
channel = connection.channel()

# 큐를 생성합니다.
channel.queue_declare(queue='my_queue')

# 큐에서 메시지를 소비하는 콜백 함수를 등록합니다.
channel.basic_consume(queue='my_queue', on_message_callback=callback, auto_ack=True)

# 메시지를 계속해서 소비합니다.
print('Waiting for messages...')
channel.start_consuming()
