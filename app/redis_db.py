import redis

from app.config import settings


def redis_connect():
    r_connect = redis.Redis(host=settings.REDIS_DIALOG_HOST,
                            port=settings.REDIS_DIALOG_PORT,
                            db=settings.REDIS_DIALOG_DB,
                            password=settings.REDIS_DIALOG_PASSWORD,
                            decode_responses=True
                            )
    try:
        r_connect.ping()
    except BaseException as error:
        print(f"Error {error}", flush=True)

    return r_connect


def redis_db_add_count_unread_from_to(from_user: int, to_user: int) -> int:
    r = redis_connect()
    result = r.hget(f"user:{to_user}", str(from_user))

    if result is not None:
        r.hset(f"user:{to_user}", str(from_user), str(int(result) + 1))
    else:
        r.hmset(f"user:{to_user}", {from_user: 1})

    return int(result) + 1 if result is not None else 1


def redis_db_get_unread_messages(id_user: int) -> dict:
    r = redis_connect()
    return r.hgetall(f"user:{id_user}")


def redis_db_read_messages_from_user(from_user: int, to_user: int) -> int:
    r = redis_connect()
    return r.hdel(f"user:{to_user}", str(from_user))
