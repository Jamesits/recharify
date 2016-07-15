#!/usr/bin/env python3

import sys
from PyQt5.QtCore import pyqtSignal, pyqtSlot, QObject, QThread, QTimer
from PyQt5.QtWidgets import QApplication
from Recharify.View import SplashScreen, WelcomeWindow, MainWindow
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
        """
        Handle GUI things before enterint Qt event loop

        :return: Qt return value
        """
        self.logger.info("[GUI] GUI initializating")
        self.dispatcher.start()

        # display splash screen
        sp = SplashScreen.SplashScreen()
        we = WelcomeWindow.WelcomeWindow()
        mc = MainWindow.MainController([])

        def call_init():
            """
            Call App.init() and update progress bar. Should be run async in ParallelQt.PQDispatcher.
            :return: None
            """
            for p in App.init():
                sp.progress_change(p)

            sp.close()

            # mc.exec_()
            # mc.main.show()

        sp.show()
        self.dispatcher.add_func(call_init)

        self.logger.info("[GUI] yielding event control to Qt")
        ret = self.app.exec_()
        if ret:
            return ret

        we.show()
        ret = self.app.exec_()
        if ret:
            return ret

        mc.main.show()
        ret = mc.exec_()
        self.dispatcher.kill()
        self.dispatcher.quit()
        return ret


class App:
    logger = MyLogger("App")

    @staticmethod
    def run():
        """
        Bootstrap function.

        :return: Qt return value
        """
        App.logger.info("[App] Application started")
        return GUI().main_loop()

    @staticmethod
    def init():
        """
        Initialize the application.

        :return: yield a progress value between 0-100 to update progress bar
        """
        App.logger.info("[App] initialization started")
        import time
        for i in range(5000):
            time.sleep(.001)
            yield i / 50
        App.logger.info("[App] initialization finished")
        yield 100