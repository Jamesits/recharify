#!/usr/bin/env python3
import asyncio
from PyQt5.QtCore import pyqtSignal, pyqtSlot, QThread, QTimer
from Recharify.MyLogger import MyLogger

class PQDispatcher(QThread):
    def __init__(self):
        """
        Make a new thread instance with the specified
        subreddits as the first argument. The subreddits argument
        will be stored in an instance variable called subreddits
        which then can be accessed by all other class instance functions

        :param subreddits: A list of subreddit names
        :type subreddits: list
        """
        self.logger = MyLogger("PQDispatcher")
        QThread.__init__(self)
        self.syncTasks = []
        self.threadPool = []
        self.isExecuting = False
        self.logger.info("Dispatcher initialized")

    def __del__(self):
        self.wait()
        self.logger.info("Dispatcher quit")

    async def _next_sync_task(self):
        """
        Run next sync task in list and return the return value.

        :return: Return value of that task.
        :rtype: any
        """
        if self.isExecuting:
            return
        self.logger.info("Dispatcher executing next func")
        self.isExecuting = True
        ret = await self.synctasks.pop(0)()
        self.isExecuting = False
        return ret

    def add_func(self, func):
        self.syncTasks.append(func)
        self.logger.info("Dispatcher added a function")

    def run(self):
        """
        Start queue dispatcher

        """
        try:
            self._next_sync_task()
        finally:
            QTimer.singleShot(10000, self.run)
