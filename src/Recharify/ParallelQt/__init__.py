#!/usr/bin/env python3
import asyncio
from PyQt5.QtCore import pyqtSignal, pyqtSlot, QThread, QTimer
from Recharify.MyLogger import MyLogger
from multiprocessing import Pool
import time


class PQDispatcher(QThread):
    def __init__(self):
        """
        """
        self.logger = MyLogger("PQDispatcher")
        QThread.__init__(self)
        self.syncTasks = []
        self.threadPool = Pool(processes=2)
        self.threads = []
        self.isExecuting = False
        self.timer = QTimer()
        self.stop = False

    def __del__(self):
        self.stop = True
        self.wait()
        self.logger.info("[ParallelQt] Dispatcher quit")

    def _next_sync_task(self):
        """
        Run next sync task in list and return the return value.

        """
        if self.isExecuting or len(self.syncTasks) == 0:
            return
        self.isExecuting = True

        def onFinish(_=None):
            self.logger.info("[ParallelQt] Function returned")
            self.isExecuting = False

        self.logger.info("[ParallelQt] Dispatcher executing next task")
        self.syncTasks.pop(0)(); onFinish()
        # self.threadPool.apply_async(self.syncTasks.pop(0), callback=onFinish)

    def add_func(self, func):
        """
        Add function as next background task.

        :param func: The function to be added
        :return: None
        """
        self.syncTasks.append(func)
        self.logger.info("[ParallelQt] New task added")

    def run(self):
        """
        Start queue dispatcher

        """
        while not self.stop:
            self._next_sync_task()
            time.sleep(1)

