import asyncio, concurrent.futures, time, os
import random

from async_class import AsyncClass, AsyncObject, task, link


class Fibonacci():
    def __init__(self, n):
        self.start = time.time()
        self.answear = self.__calculations(n)
        self.time = time.time() - self.start
        self.process = os.getpid()

    def __calculations(self, n):
        if n in (0, 1, 2):
            return 1
        return self.__calculations(n - 1) + self.__calculations(n - 2)

    def __repr__(self):
        return f'Process: {self.process}, Time work: {self.time}, Answear: {self.answear}'

class Factorial():
    def __init__(self, n):
        self.start = time.time()
        self.answear = self.__calculations(n)
        self.time = time.time() - self.start
        self.process = os.getpid()

    def __calculations(self, n):
        if n in [0, 1]:
            return n
        return n * self.__calculations(n-1)

    def __repr__(self):
        return f'Process: {self.process}, Time work: {self.time}, Answear: {self.answear}'

class Squares():
    def __init__(self, n):
        self.start = time.time()
        self.answear = self.__calculations(n)
        self.time = time.time() - self.start
        self.process = os.getpid()

    def __calculations(self, n):
        return n**2

    def __repr__(self):
        return f'Process: {self.process}, Time work: {self.time}, Answear: {self.answear}'

class Cubic():
    def __init__(self, n):
        self.start = time.time()
        self.answear = self.__calculations(n)
        self.time = time.time() - self.start
        self.process = os.getpid()

    def __calculations(self, n):
        return n**3

    def __repr__(self):
        return f'Process: {self.process}, Time work: {self.time}, Answear: {self.answear}'

class AsynFibonacci(AsyncClass):
    async def __ainit__(self, n):
        self.start = time.time()
        self.answear = await self.__calculations(n)
        self.time = time.time() - self.start
        self.process = os.getpid()

    async def __calculations(self, n):
        await asyncio.sleep(random.randint(1,  2))
        if n in (0, 1, 2):
            return 1
        return await self.__calculations(n - 1) + await self.__calculations(n - 2)

    def __repr__(self):
        return f'AsynFibonacci, Process: {self.process}, Time work: {self.time}, Answear: {self.answear}'

class AsyncFactorial(AsyncClass):
    async def __ainit__(self, n):
        self.start = time.time()
        self.answear = await self.__calculations(n)
        self.time = time.time() - self.start
        self.process = os.getpid()

    async def __calculations(self, n):

        if n in [0, 1]:
            return n
        return n * await self.__calculations(n-1)

    def __repr__(self):
        return f'AsyncFactorial, Process: {self.process}, Time work: {self.time}, Answear: {self.answear}'

class AsyncSquares(AsyncClass):
    async def __ainit__(self, n):
        self.start = time.time()
        self.answear = await self.__calculations(n)
        self.time = time.time() - self.start
        self.process = os.getpid()

    async def __calculations(self, n):
        return n**2

    def __repr__(self):
        return f'AsyncSquares, Process: {self.process}, Time work: {self.time}, Answear: {self.answear}'

class AsyncCubic(AsyncClass):
    async def __ainit__(self, n):
        self.start = time.time()
        self.answear = await self.__calculations(n)
        self.time = time.time() - self.start
        self.process = os.getpid()

    async def __calculations(self, n):
        return n**3

    def __repr__(self):
        return f'AsyncCubic, Process: {self.process}, Time work: {self.time}, Answear: {self.answear}'

async def main(object, n):
    instance = await object(n)
    print(instance)

if __name__ == '__main__':
    """TEST MULTIPROCCESING AND ASYNCIO"""
    #Multiprocessinf
    NUM_FIBONACCI = [i for i in range(10)]
    with concurrent.futures.ProcessPoolExecutor(5) as exec:
        result = {exec.submit(Fibonacci, num): num for num in NUM_FIBONACCI}
        for result_sub in concurrent.futures.as_completed(result):
            print(result_sub.result())
        time.sleep(2)

    NUM_FACTORIAL = [i for i in range(10)]
    with concurrent.futures.ProcessPoolExecutor(5) as exec:
        result = {exec.submit(Factorial, num): num for num in NUM_FACTORIAL}
        for result_sub in concurrent.futures.as_completed(result):
            print(result_sub.result())
        time.sleep(2)

    NUM_SQUARES = [i for i in range(10)]
    with concurrent.futures.ProcessPoolExecutor(5) as exec:
        result = {exec.submit(Squares, num): num for num in NUM_SQUARES}
        for result_sub in concurrent.futures.as_completed(result):
            print(result_sub.result())
        time.sleep(2)

    NUM_CUBIC = [i for i in range(10)]
    with concurrent.futures.ProcessPoolExecutor(5) as exec:
        result = {exec.submit(Cubic, num): num for num in NUM_CUBIC}
        for result_sub in concurrent.futures.as_completed(result):
            print(result_sub.result())
        time.sleep(2)

    class MainClass(AsyncObject):
        async def __ainit__(self):
            # Do async staff here
            pass

        async def __adel__(self):
            """ This method will be called when object will be closed """
            pass


    class RelatedClass(AsyncObject):
        async def __ainit__(self, parent: MainClass):
            link(self, parent)
    async def squad(n):
        print(f'Start {n}')
        await asyncio.sleep(1)
        return n**2

    #Asyncio
    loop = asyncio.new_event_loop()
    asyncio.set_event_loop(loop)
    loop.run_until_complete(asyncio.gather(main(AsynFibonacci, 1),
                                           main(AsynFibonacci, 2),
                                           main(AsynFibonacci, 3),
                                           main(AsynFibonacci, 4),
                                           main(AsynFibonacci, 5),
                                           main(AsynFibonacci, 6),
                                           main(AsynFibonacci, 7),
                                           main(AsynFibonacci, 8),
                                           main(AsynFibonacci, 9),
                                           main(AsynFibonacci, 10),
                                           ))

    loop = asyncio.new_event_loop()
    asyncio.set_event_loop(loop)
    loop.run_until_complete(asyncio.gather(main(AsyncFactorial, 1),
                                           main(AsyncFactorial, 2),
                                           main(AsyncFactorial, 3),
                                           main(AsyncFactorial, 4),
                                           main(AsyncFactorial, 5),
                                           main(AsyncFactorial, 6),
                                           main(AsyncFactorial, 7),
                                           main(AsyncFactorial, 8),
                                           main(AsyncFactorial, 9),
                                           main(AsyncFactorial, 10),
                                           ))

    loop = asyncio.new_event_loop()
    asyncio.set_event_loop(loop)
    loop.run_until_complete(asyncio.gather(main(AsyncSquares, 1),
                                           main(AsyncSquares, 2),
                                           main(AsyncSquares, 3),
                                           main(AsyncSquares, 4),
                                           main(AsyncSquares, 5),
                                           main(AsyncSquares, 6),
                                           main(AsyncSquares, 7),
                                           main(AsyncSquares, 8),
                                           main(AsyncSquares, 9),
                                           main(AsyncSquares, 10),
                                           ))

    loop = asyncio.new_event_loop()
    asyncio.set_event_loop(loop)
    loop.run_until_complete(asyncio.gather(main(AsyncCubic, 1),
                                           main(AsyncCubic, 2),
                                           main(AsyncCubic, 3),
                                           main(AsyncCubic, 4),
                                           main(AsyncCubic, 5),
                                           main(AsyncCubic, 6),
                                           main(AsyncCubic, 7),
                                           main(AsyncCubic, 8),
                                           main(AsyncCubic, 9),
                                           main(AsyncCubic, 10),
                                           ))