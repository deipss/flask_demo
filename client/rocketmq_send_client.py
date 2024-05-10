from rocketmq.client import Producer, Message


class RocketmqSendClient():

    def __init__(self):
        self.producer = Producer('PID-XXX')
        self.producer.set_name_server_address('127.0.0.1:9876')
        self.producer.start()

    def sent(self):
        msg = Message('YOUR-TOPIC')
        msg.set_keys('XXX')
        msg.set_tags('XXX')
        msg.set_body('XXXX')
        ret = self.producer.send_sync(msg)
        print(ret.status, ret.msg_id, ret.offset)

    def __del__(self):
        self.producer.shutdown()

if __name__ == '__main__':
    client = RocketmqSendClient()
    client.sent();