#!/usr/bin/env python3

from PyQt5.QtWidgets import QWidget, QLabel, QDesktopWidget


class SplashScreen(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle(_('Recharify'))
        QLabel(_('Loading splash screen image...'), self).move(15, 10)
        self.progress = QtGui.QProgressBar(self)
        self.progress.setGeometry(200, 80, 250, 20)
        self.setGeometry(300, 300, 250, 150)
        self.movetocenter()

    def movetocenter(self):
        qr = self.frameGeometry()
        cp = QDesktopWidget().availableGeometry().center()
        qr.moveCenter(cp)
        self.move(qr.topLeft())