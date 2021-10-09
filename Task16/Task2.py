class Boss:
    def __init__(self, id_: int, name: str, company: str):
        self.id = id_

        self.name = name

        self.company = company

        self.workers = []
    @property
    def boss(self):
        return self.id, self.name, self.company, self.workers

    @boss.setter
    def boss(self, workers_ = None):
        self.workers.append(workers_)

    def __repr__(self):
        return self.name



class Worker:

    def __init__(self, id_: int, name: str, company: str, boss: Boss):
        self.id = id_

        self.name = name

        self.company = company

        self.boss = boss

    @property
    def worker(self):
        return self.id, self.name, self.company, self.boss


    @worker.setter
    def worker(self, boss = None):
        self.boss = boss

    def __repr__(self):
        return self.name


boss1 = Boss(1, "Danil", "RoschaCORP")
worker1 = Worker(2, "Daria", "RoschaCORP", boss1)
worker2 = Worker(3, "Andrew", "RoschaCORP", boss1)
boss1.boss = worker1
boss1.boss = worker2
print(worker1.worker)
print(boss1.boss)

