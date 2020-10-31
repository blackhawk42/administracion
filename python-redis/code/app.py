import redis

r = redis.StrictRedis(
    host='104.198.244.0',
    port=6379,
    charset="utf-8",
    decode_responses=True
)

r.set('ip_address', '0.0.0.0');
print ("ip : ", r.get('ip_address'));

r.lpush('list1', 'A')
r.lpush('list1', 'B')
r.lpush('list1', 'C')

print ("list : ", r.lrange('list1', 0, -1));

myrecord = {
    "name": "Hackers and Slackers",
    "description": "Mediocre tutorials",
    "website": "https://hackersandslackers.com/",
    "github": "https://github.com/hackersandslackers"
}

r.hmset('myhash', myrecord)
print ("myhash : " ,  r.hgetall('myhash'));


