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
        self.logger.info("Dispatcher initialized")
        self.timer = QTimer()
        self.stop = False

    def __del__(self):
        self.wait()
        self.logger.info("Dispatcher quit")

    def _next_sync_task(self):
        """
        Run next sync task in list and return the return value.

        """
        if self.isExecuting or len(self.syncTasks) == 0:
            self.logger.info("Dispatcher awaiting")
            return
        self.logger.info("Dispatcher executing next function")
        self.isExecuting = True

        def onFinish(_=None):
            self.logger.info("Task finished")
            self.isExecuting = False

        self.logger.info("Dispatcher started function")
        self.syncTasks.pop(0)(); onFinish()
        # self.threadPool.apply_async(self.syncTasks.pop(0), callback=onFinish)
        self.logger.info("Dispatcher returned")

    def add_func(self, func):
        self.syncTasks.append(func)
        self.logger.info("Dispatcher added a function")

    def run(self):
        """
        Start queue dispatcher

        """
        while not self.stop:
            self.logger.info("Checking unfinished tasks")
            self._next_sync_task()
            time.sleep(1)

        # self.timer.singleShot(1, self.start)
