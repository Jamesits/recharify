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
        self.logger.info("Main loop stared")
        self.dispatcher.start()

        # display splash screen
        sp = SplashScreen.SplashScreen()

        def t():
            self.logger.info("t started")
            import time
            for i in range(5000):
                time.sleep(.001)
                self.app.processEvents()
            self.logger.info("t finished")
            # sp.close()

        @pyqtSlot()
        def addfunc():
            self.logger.info("Adding func")
            self.dispatcher.add_func(t)


        sp.loaded.connect(t)
        sp.show()
        return self.app.exec_()


class App:
    def __init__(self):
        self.logger = MyLogger("App")

    def run(self):
        self.logger.info("Event: App.run()")
        return GUI().main_loop()
