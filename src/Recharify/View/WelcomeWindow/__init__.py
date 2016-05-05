#!/usr/bin/env python3

from PyQt5.QtWidgets import QWidget, QLabel, QDesktopWidget, QProgressBar
from PyQt5.QtCore import Qt, pyqtSignal


class WelcomeWindow(QWidget):
    """
    A splash screen window with an image, a textbox for current status, and a progress bar.
    """

    def __init__(self):
        super().__init__()
        self.setWindowTitle(_('Welcome to Recharify'))
        QLabel(_('Welcome'), self).move(15, 10)
        self.setGeometry(300, 300, 250, 150)
        self.movetocenter()

    def movetocenter(self):
        qr = self.frameGeometry()
        cp = QDesktopWidget().availableGeometry().center()
        qr.moveCenter(cp)
        self.move(qr.topLeft())

