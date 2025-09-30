from fastapi import FastAPI
from app.config import settings


app = FastAPI(title=settings.PROJECT_NAME,
              version=settings.PROJECT_VERSION,
              root_path="/v1/unread_messages"
              )


@app.get("/")
async def root():
    return {"message": "Hello World"}


@app.get("/hello/{name}")
async def say_hello(name: str):
    return {"message": f"Hello {name}"}
