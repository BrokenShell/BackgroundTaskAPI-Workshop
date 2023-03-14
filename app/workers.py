import time


class Worker:
    count = 0

    def __call__(self):
        self.count += 1
        time.sleep(10)
        print(f"Job {self.count} done!")
