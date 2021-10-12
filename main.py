from typing import List
import redis
import json

from Models import ItemPublish, TestObject
from fastapi import FastAPI, Depends

app = FastAPI()

TIME_LIFE_DB =  15

def get_db_NSql():
    try:
        db_nsql = redis.Redis(host='localhost', port=6379, db=0, password=None)
        yield  db_nsql
    finally:
        return None

@app.get("/ping", response_model=str)
def get_ping(db_nsql: redis.Redis = Depends(get_db_NSql)):
    try:
        if db_nsql.ping():
            return "pong"
    except Exception as e:
        print(e)
        return None

@app.get("/get-user-db", response_model= str)
def get_users_db(db_nsql: redis.Redis = Depends(get_db_NSql)):
    try:
        return db_nsql.acl_whoami()
    except Exception as e:
        print(e)
        return None

@app.get("/get-users-db", response_model= List[str])
def get_users_db(db_nsql: redis.Redis = Depends(get_db_NSql)):
    try:
        return db_nsql.acl_users()
    except Exception as e:
        print(e)
        return None

@app.post("/item", response_model=TestObject)
def create_item(item: TestObject, db_nsql: redis.Redis = Depends(get_db_NSql)):
    try:
        if db_nsql.ping():
            item.time_life =  item.time_life if item.time_life != None  else TIME_LIFE_DB
            db_nsql.set(item.id, json.dumps(item.dict()), ex=item.time_life)
            return item
    except Exception as e:
        print(e)
        return None

@app.get("/item/{item_id}", response_model= TestObject)
def get_item(item_id: str, db_nsql: redis.Redis = Depends(get_db_NSql)):
    try:
        item_db = db_nsql.get(item_id)
        if db_nsql.ping() and  item_db != None:
            return  json.loads(item_db.decode("utf-8"))
        else:
            return None
    except Exception as e:
        print(e)
        return None

@app.delete("/item/{item_id}", response_model= TestObject)
def delete_item(item_id: str, db_nsql: redis.Redis = Depends(get_db_NSql)):
    try:
        item_db = db_nsql.get(item_id)
        if db_nsql.ping() and  item_db != None:
            db_nsql.delete(item_id)
            return  json.loads(item_db.decode("utf-8"))
        else:
            return None
    except Exception as e:
        print(e)
        return None

@app.post("/publish", response_model=ItemPublish)
def publish_item(item: ItemPublish, db_nsql: redis.Redis = Depends(get_db_NSql)):
    try:
        if db_nsql.ping():
            print(db_nsql.publish(channel=item.channel, message=item.message))
            return item
    except Exception as e:
        print(e)
        return None