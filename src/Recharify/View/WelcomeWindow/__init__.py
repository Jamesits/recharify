#!/usr/bin/env python3

import sys

from PyQt5.QtGui import QIcon
from PyQt5.QtWidgets import QLabel, QDesktopWidget
from PyQt5.QtWidgets import QMainWindow, QAction, qApp, QApplication, QMenuBar


class WelcomeWindow(QMainWindow):

    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setWindowTitle(_('Welcome to Recharify'))
        QLabel(_('Welcome'), self).move(15, 10)

        # exitAction = QAction(QIcon('exit.png'), '&Exit', self)
        exitAction = QAction('&Fuck', self)
        exitAction.setShortcut('Ctrl+Q')
        exitAction.setStatusTip('Exit application')
        exitAction.triggered.connect(qApp.quit)

        self.statusBar()

        menubar = self.menuBar()
        # menubar = QMenuBar()
        fileMenu = menubar.addMenu('&File')
        fileMenu.addAction(exitAction)

        self.setGeometry(300, 300, 300, 200)
        self.movetocenter()

        # self.show()

    def movetocenter(self):
        qr = self.frameGeometry()
        cp = QDesktopWidget().availableGeometry().center()
        qr.moveCenter(cp)
        self.move(qr.topLeft())


if __name__ == '__main__':

    app = QApplication(sys.argv)
    ww = WelcomeWindow()
    ww.show()
    sys.exit(app.exec_())