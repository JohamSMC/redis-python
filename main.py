import redis

r = redis.Redis(host='localhost', port=6379, db=0,  password=None)

r.mset ({'clave1': 'valor1', 'clave2': 'valor2'})
print(r.mget('clave1', 'clave2'))