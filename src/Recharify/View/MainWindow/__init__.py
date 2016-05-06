#!/usr/bin/env python3
from PyQt5.QtWidgets import QWidget, QLabel, QDesktopWidget, QProgressBar, QApplication, QMainWindow, QPushButton
from PyQt5.QtCore import Qt, pyqtSignal, QRect, QUrl
from PyQt5.QtQuick import QQuickView



class MyPopup(QWidget):
    def __init__(self):
        QWidget.__init__(self)

    def paintEvent(self, e):
        dc = QPainter(self)
        dc.drawLine(0, 0, 100, 100)
        dc.drawLine(100, 0, 0, 100)


class MainWindow(QMainWindow):
    def __init__(self, *args):
        QMainWindow.__init__(self, *args)
        self.cw = QWidget(self)
        self.setCentralWidget(self.cw)
        self.btn1 = QPushButton("Click me", self.cw)
        self.btn1.setGeometry(QRect(0, 0, 100, 30))
        # self.connect(self.btn1, SIGNAL("clicked()"), self.doit)
        self.w = None

    def doit(self):
        print("Opening a new popup window...")
        self.w = MyPopup()
        self.w.setGeometry(QRect(100, 100, 400, 200))
        self.w.show()


class MainController(QApplication):
    def __init__(self, *args):
        QApplication.__init__(self, *args)
        self.main = MainWindow()
        # self.connect(self, SIGNAL("lastWindowClosed()"), self.byebye )
        # self.main.show()

    def byebye( self ):
        self.exit(0)