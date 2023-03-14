import time


class Worker:
    count = 0

    def __call__(self):
        time.sleep(10)
        self.count += 1
        print(f"Job {self.count} done!")
