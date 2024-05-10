import time

from rocketmq.client import PushConsumer, ConsumeStatus

class RocketmqConsumerClient():
    def callback(msg):
        print(msg.id, msg.body)
        return ConsumeStatus.CONSUME_SUCCESS

    def __init__(self):


        self.selfconsumer = None
        self.consumer = PushConsumer('CID_XXX')
        self.consumer.set_name_server_address('192.168.0.2:9876')
        self.selfconsumer.subscribe('YOUR-TOPIC', self.callback)
        self.consumer.start()

        while True:
            time.sleep(3)

    def __del__(self):
        self.consumer.shutdown()

