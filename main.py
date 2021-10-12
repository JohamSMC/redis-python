from typing import List
import redis
import json

from Models import TestObject
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