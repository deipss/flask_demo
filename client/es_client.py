from datetime import datetime

from elasticsearch import Elasticsearch

# 指定地址和端口

if __name__ == '__main__':
    es = Elasticsearch([{'host': '192.168.0.2', 'port': 9200}])

    doc = {
        'author': '张三',
        'text': '这是一个示例文档',
        'timestamp': datetime.now(),
    }

    # 索引一个文档到名为"my_index"的索引中，ID自动生成
    res = es.index(index="my_index", body=doc)
    print(res['result'])

    # 索引一个文档并指定ID
    res = es.index(index="my_index", id=1, body=doc)
    print(res['result'])
