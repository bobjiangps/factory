from celery import shared_task
import time


@shared_task
def add(x, y):
    timeout = 10
    while timeout:
        print(timeout)
        time.sleep(1)
        timeout -= 1
    return x + y
