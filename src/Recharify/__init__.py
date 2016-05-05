#!/usr/bin/env python3

import sys
from PyQt5.QtCore import pyqtSignal, pyqtSlot, QObject, QThread, QTimer
from PyQt5.QtWidgets import QApplication
from Recharify.View import SplashScreen
import gettext
from Recharify.ParallelQt import PQDispatcher
from Recharify.MyLogger import MyLogger

# Set up translation
gettext.translation('Recharify', localedir='resources/locale/', languages=['zh_CN'], fallback=True).install()


class GUI:
    def __init__(self):
        self.logger = MyLogger("GUI")
        self.app = QApplication(sys.argv)
        self.dispatcher = PQDispatcher()

    def main_loop(self):
        self.logger.info("Main loop started")
        self.dispatcher.start()

        # display splash screen
        sp = SplashScreen.SplashScreen()

        def call_init():
            for p in App.init():
                sp.progress_change(p)
            sp.close()

        self.dispatcher.add_func(call_init)

        sp.show()
        self.logger.info("Qt now handling events")
        return self.app.exec_()


class App:
    logger = MyLogger("App")

    @staticmethod
    def run():
        App.logger.info("Event: App.run()")
        return GUI().main_loop()

    @staticmethod
    def init():
        App.logger.info("background initialization started")
        import time
        for i in range(5000):
            time.sleep(.001)
            yield i / 50
        App.logger.info("background initialization finished")
        yield 100