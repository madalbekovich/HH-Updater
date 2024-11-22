import time
from celery import Celery

app = Celery('app', broker='pyamqp://guest@localhost//')
app.conf.broker_url = 'redis://localhost:6379/0'


@app.task
def check_celery():
    print("Start celery tasks")
    time.sleep(2)
    print("Report celery.... OK")

check_celery()