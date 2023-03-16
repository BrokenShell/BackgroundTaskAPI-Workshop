import time
from collections import deque
from typing import Callable, Iterable


class Worker:
    count = 0

    def __call__(self):
        self.count += 1
        result = f"Job {self.count} done!"
        time.sleep(10)
        print(result)


class Job:

    def __init__(self, worker: Callable, *args, **kwargs):
        self.worker = worker
        self.args = args
        self.kwargs = kwargs

    def __call__(self):
        return self.worker(*self.args, **self.kwargs)


class Agent:

    def __init__(self, job_queue: Iterable[Job]):
        self.job_queue = deque(job_queue)

    def __call__(self):
        for idx, job in enumerate(self.job_queue):
            self.job_queue[idx] = job()
        return self.job_queue
