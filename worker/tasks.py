import os

from celery import Celery

user = os.environ.get("RMQ_USER")
password = os.environ.get("RMQ_USER_PASSWORD")


app = Celery("tasks", broker=f"amqp://{user}:{password}@rabbit:5672//")


@app.task
def reverse(string):
    return string[::-1]
