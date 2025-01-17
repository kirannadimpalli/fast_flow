from fastapi import FastAPI
from celery import Celery

celery = Celery(
    __name__,
    broker="redis://127.0.0.1:6379/0",
    backend="redis://127.0.0.1:6379/0"
)

app = FastAPI()


@app.get("/")
async def root():
    return {"message": "Hello World"}


@celery.task
def divide(x, y):
    import time
    time.sleep(5)
    return x / y