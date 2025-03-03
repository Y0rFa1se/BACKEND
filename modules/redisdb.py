import redis

import os

async def get_redis_connection():
    connection = redis.Redis(
        host = os.getenv("REDIS_HOST"),
        password = os.getenv("REDIS_PASSWORD")
    )

    return connection

async def redis_ping():
    conn = await get_redis_connection()
    return conn.ping()

async def get_redis_val(key: str):
    conn = await get_redis_connection()
    return conn.get(key)

async def does_redis_exist(key: str):
    conn = await get_redis_connection()
    return conn.exists(key)

async def set_redis_val(key: str, val: str, ex: int = None):
    conn = await get_redis_connection()
    conn.set(key, val, ex=ex)

    return True

async def renew_redis_key(key: str, ex: int):
    conn = await get_redis_connection()
    conn.expire(key, ex)

    return True

async def delete_redis_key(key: str):
    conn = await get_redis_connection()
    conn.delete(key)

    return True