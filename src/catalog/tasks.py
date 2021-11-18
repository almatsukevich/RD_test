from celery import Celery
from . import models

app = Celery('tasks')


@app.task
def add(x, y):
    
    return x + y