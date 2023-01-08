import redis
import json
red = redis.Redis(
    host='redis-10275.c263.us-east-1-2.ec2.cloud.redislabs.com',
    port=10275,
    password='X7KP4EK3MblYSOaxnTGN72qXWBj5PWOK'
)

red.delete('dict1') # удаляются ключи с помощью метода .delete()
print(red.get('dict1'))
