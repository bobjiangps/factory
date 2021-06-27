from datetime import datetime, timedelta
import time
from redis import Redis
from rq import Queue, Retry, Worker
from te import task


# rq worker -u redis://:bobjiang@localhost:6379/0 --name worker1 --with-scheduler
# rq worker low high default


queue = Queue('debug', connection=Redis(password="bobjiang"))

def queue_tasks():
    queue.enqueue(task.print_task, 5)
    # queue.enqueue(task.print_task, 5, retry=Retry(max=2))
    queue.enqueue_in(timedelta(seconds=10), task.print_numbers, 5)

def main():
    queue_tasks()

if __name__ == "__main__":
    main()


# # 1
# myredis = Redis(password="bobjiang")
# workers = Worker.all(connection=myredis)
# print(workers[0])
# # 2
# queue = Queue(connection=Redis(password="bobjiang"))
# workers = Worker.all(queue=queue)
# print(workers[0])
# # 3
# myredis = Redis(password="bobjiang")
# queue = Queue('test',connection=Redis(password="bobjiang"))
# worker = Worker([queue], connection=myredis, name='foo')
# worker.work()