#!/usr/bin/python3
from threading import Thread
from queue import Queue, Empty
from src.core_lib.concurrency.task import ITask

class Worker(Thread):

    def __init__(self, queue: Queue = None, is_core: bool = False):
        Thread.__init__(self)
        self.daemon = False
        self.__queue = queue
        self.__is_core = is_core
        self.__destroyed = False

    def destroy(self):
        self.__destroyed = True

    def get_task_from_queue(self) -> ITask:
        return self.__queue.get(block=True, timeout=10)

    def process(self):
        try:
            task: ITask = self.get_task_from_queue()
            if task:
                try:
                    task.run()
                except: pass
                self.__queue.task_done()
        except Empty as e:
            pass
        except Exception as e:
            print(e)

    def run(self):
        while self.__destroyed == False:
            try:
                if self.__queue is None:
                    break
                self.process()
                if self.__is_core == False:
                    break
            except Exception as e:
                print(e)
