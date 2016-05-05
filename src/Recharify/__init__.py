#!/usr/bin/env python3

import sys
from PyQt5.QtCore import pyqtSignal, pyqtSlot, QObject, QThread, QTimer
from PyQt5.QtWidgets import QApplication
from Recharify.View import SplashScreen
import gettext

# Set up translation
gettext.translation('Recharify', localedir='resources/locale/', languages=['zh_CN'], fallback=True).install()


class BackgroundWorker(QObject):
    next = pyqtSignal()
    finished = pyqtSignal()
    intReady = pyqtSignal(int)

    def __init__(self, list=[]):
        super().__init__()
        self.list = list

    @pyqtSlot()
    def procCounter(self):  # A slot takes no params
        #sp.close()
        for i in range(1, 100):
            time.sleep(1)
            self.intReady.emit(i)

        self.finished.emit()



class App:
    def __init__(self):
        self.app = QApplication(sys.argv)

    def run(self):

        # display splash screen
        sp = SplashScreen.SplashScreen()
        sp.show()

        def task():
            # do initial checks
            # let's mock up something
            import time
            time.sleep(5)
            # initial work is done, close splash screen
            sp.close()

        self.obj = BackgroundWorker()  # no parent!
        self.thread = QThread()  # no parent!

        # 2 - Connect Worker`s Signals to Form method slots to post data.
        self.obj.intReady.connect(self.onIntReady)

        # 3 - Move the Worker object to the Thread object
        self.obj.moveToThread(self.thread)

        # 4 - Connect Worker Signals to the Thread slots
        self.obj.finished.connect(self.thread.quit)

        # 5 - Connect Thread started signal to Worker operational slot method
        self.thread.started.connect(self.obj.procCounter)

        # * - Thread finished signal will close the app if you want!
        # self.thread.finished.connect(app.exit)

        # 6 - Start the thread
        self.thread.start()

        # Load config
        #QTimer.singleShot(0, task)

        sys.exit(self.app.exec_())

    def onIntReady(self, i):
        #self.label.setText("{}".format(i))
        print(i)
