from redis import Redis
from rq import Queue
from rq.job import Job
import time


def round_data():
    return 1 + 2



if __name__ == "__main__":
    redis_conn = Redis(password="bobjiang")
    q_pending = Queue("pending", connection=redis_conn)
    q_running = Queue("running", connection=redis_conn)
    q_success = Queue("success", connection=redis_conn)
    q_fail = Queue("fail", connection=redis_conn)

    job = Job.create(round_data, connection=redis_conn, id=f"round_2876-worker_23-{int(time.time())}")
    job.save()
    job.meta["test_round"] = {"name": "abc", "browser": "chrome"}
    job.save_meta()

    # q_pending.enqueue(round_data)
    q_pending.enqueue_job(job)

    # q_pending.run_job(job)

    required_job_ids = q_pending.get_job_ids(0, 2)  # get the first two job ids in the queue, 0 for start index, 2 for the length; then you can move out and run
    q_pending.remove(required_job_ids[0])
    required_jobs = q_pending.get_jobs(0, 2)  # get first two jobs instead of id
    q_pending.remove(required_jobs[0])

    first_pending_id = q_pending.pop_job_id()  # move out of pending queue, but cannot assign specific job id
    job3 = Job.fetch(first_pending_id, connection=Redis(password="bobjiang"))
    q_running.enqueue_job(job3)  # move to running queue


