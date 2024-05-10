import redis


class RedisClient():
    def __init__(self, host, port, password):
        self.host = host
        self.port =port
        self.password = password
        self.db = 0
        self.r = redis.Redis(host=self.host, port=self.port, password=self.password, db=self.db,decode_responses=True)


    def get(self,key):
        return self.r.get(key)

    def keys(self):
        return self.r.keys()


if __name__ == '__main__':
    redis_client = RedisClient("192.168.0.2", 6379, "jhkdjhkjdhsIUTYURTU_T2RPWr")
    print(redis_client.keys())

