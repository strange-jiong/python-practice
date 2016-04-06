# -*-coding:utf-8-*-

# please install redis-server firstly

__author__ = 'jiong'
import redis
import uuid
# default db is db0
r = redis.StrictRedis(host='localhost', port=6379)

for i in range(200):
    r.set('key_id' + str(i), uuid.uuid1())

for i in range(200):
    print(r.get("key_id" + str(i)))
