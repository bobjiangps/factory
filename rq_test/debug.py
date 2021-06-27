from redis import Redis
from rq import Queue, Worker
from te import debug_task
from rq.job import Job


if __name__ == "__main__":
    q = Queue("debug", connection=Redis(password="bobjiang"))
    job = q.enqueue(debug_task.test_round)
    print(job.id)
    print(job.result)
    print(job.worker_name)
    job.meta["test_round"] = {"name": "abc", "browser": "chrome"}
    job.save_meta()
    job_2 = Job.fetch(job.id, connection=Redis(password="bobjiang"))
    print(job_2.id)
    jobs = q.get_jobs()
    print(jobs)
    myredis = Redis(password="bobjiang")
    worker = Worker([q], connection=myredis, name='foo')
    worker.execute_job(jobs[0], q)  # ???
