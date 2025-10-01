from fastapi import FastAPI, HTTPException
from starlette import status
from app.config import settings
import app.redis_db as redis_db


app = FastAPI(title=settings.PROJECT_NAME,
              version=settings.PROJECT_VERSION,
              root_path="/v1/unread_messages"
              )


@app.post("/set/unreadcount/{from_user}/{to_user}")
async def add_user_unread_message(from_user: int, to_user: int):
    try:
        result = redis_db.redis_db_add_count_unread_from_to(from_user, to_user)
        if result:
            return {f"Count unread messages from user {from_user}": result}
        else:
            return {"Add unread message": "false"}
    except BaseException:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Add unread message not send"
        )


@app.post("/readmessages/{from_user}/{to_user}")
async def read_messages_from_user(from_user: int, to_user: int):
    try:
        result = redis_db.redis_db_read_messages_from_user(from_user, to_user)
        if result:
            return {"ok": result}
        else:
            return {"ok": "false"}
    except BaseException:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Unread message not found"
        )

@app.post("/get/unredmessages/{id_user}")
async def get_user_unread_messages(id_user: int):
    try:
        result = redis_db.redis_db_get_unread_messages(id_user)
        return result
    except BaseException:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Unread message for user {id_user} not found"
        )
