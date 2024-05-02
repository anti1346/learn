#### python3-pip 설치
```
apt install -y python3-pip
```
#### 파이션 pika 라이브러리 설치
```
pip install pika
```
#### Consumer (소비자): RabbitMQ 큐에서 메시지를 수신하여 처리하는 역할을 담당합니다.
###### Consumer는 큐에 연결되어 메시지를 받아들이고, 해당 메시지를 소비하여 필요한 로직을 수행합니다. Consumer는 메시지를 소비하면서 큐에서 메시지를 제거합니다.
##### Publisher (발행자): RabbitMQ 큐로 메시지를 발행하는 역할을 담당합니다.
###### Publisher는 큐에 연결하여 메시지를 발행하고, 해당 메시지를 큐에 전달합니다. 메시지는 큐에 저장되어 대기하며, Consumer가 이를 소비하여 처리합니다.
