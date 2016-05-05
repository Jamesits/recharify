#!/usr/bin/env python3

from PyQt5.QtWidgets import QWidget, QLabel, QDesktopWidget, QProgressBar
from PyQt5.QtCore import Qt, pyqtSignal


class SplashScreen(QWidget):
    loaded = pyqtSignal()

    def __init__(self):
        super().__init__()
        self.setWindowFlags(Qt.FramelessWindowHint)
        self.setWindowTitle(_('Recharify'))
        QLabel(_('Loading splash screen image...'), self).move(15, 10)
        self.progress = QProgressBar(self)
        self.progress.setGeometry(0, 0, 250, 20)
        self.setGeometry(300, 300, 250, 150)
        self.movetocenter()

    def showEvent(self, arg):
        super().showEvent(arg)
        self.loaded.emit()

    def movetocenter(self):
        qr = self.frameGeometry()
        cp = QDesktopWidget().availableGeometry().center()
        qr.moveCenter(cp)
        self.move(qr.topLeft())