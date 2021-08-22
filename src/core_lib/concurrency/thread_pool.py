#!/usr/bin/python3
import queue
import time
from src.core_lib.concurrency.task import ITask
from src.core_lib.concurrency.worker import Worker

class ThreadPoolExecutor(object):
    
    def __init__(self, pool_size = 1000, pool_size_core = 1, pool_size_max = 5):
        self.__pool = []
        self.__queue = queue.Queue(pool_size)
        self.__destroyed = False
        self.__pool_size_core = pool_size_core
        self.__pool_size_max = pool_size_max
    
    def start(self):
        if self.__pool_size_core < 1:
            return
        for i in range(self.__pool_size_core):
            w = Worker(self.__queue, True)
            w.start()
            self.__pool.append(w)

    def __active_threads(self):
        return [i for i in self.__pool if i and i.is_alive() == True]
    
    def __inactive_threads(self):
        return [i for i in self.__pool if i is None or i.is_alive() == False]

    def __delete_threads(self):
        inactive = self.__inactive_threads()
        if len(inactive) < 1:
            return
        for i in range(len(inactive)):
            self.__pool.remove(inactive[i])

    def __check(self):
        q_size = self.__queue.qsize()
        if q_size == 0:
            return
        else:
            self.__delete_threads()
            active_thread = len(self.__active_threads()) - self.__pool_size_core
            if active_thread > 0 and active_thread < abs(self.__pool_size_max - self.__pool_size_core):
                w = Worker(self.__queue, False)
                w.start()
                self.__pool.append(w)

    def __add(self, task: ITask = None) -> None:
        self.__queue.put(task)

    def add_task(self, task: ITask = None) -> None:
        if self.__destroyed == True:
            raise Exception('Cannont destroy as the pool has already been destroy.')
        self.__add(task)
        self.__check()

    def destroy(self):
        if self.__destroyed == True:
            raise Exception('Cannont destroy as the pool has already been destroy.')
        self.__destroyed = True
        if len(self.__pool) > 0:
            for i in range(len(self.__pool)):
                self.__pool[i].destroy()
        with self.__queue.mutex:
            self.__queue.queue.clear()
    
if __name__ == "__main__":
    from task import PushTask
    tp = ThreadPoolExecutor()
    for i in range(100):
        pt = PushTask()
        tp.add_task(pt)
    tp.stop()
    #tp.wait_completion()
