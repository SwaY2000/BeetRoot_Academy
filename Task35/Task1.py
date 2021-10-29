import threading

class MyThearding(threading.Thread):
    counter = 0
    def __init__(self, round):
        threading.Thread.__init__(self)
        self.round = round

    def run(self):
        print(f"Starting thread {self.name}")
        for _ in range(self.round):
            MyThearding.counter += 1
        print(MyThearding.counter)
        print(f"Finished thread {self.name}")

thread1 = MyThearding(1000000)
thread2 = MyThearding(1000000)

thread1.start()
thread2.start()