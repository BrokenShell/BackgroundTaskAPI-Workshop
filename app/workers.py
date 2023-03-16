import time


class Worker:
    count = 0

    def __call__(self):
        self.count += 1
        result = f"Job {self.count} done!"
        time.sleep(10)
        print(result)
