#!/usr/bin/env python3

import sys
from PyQt5.QtWidgets import QApplication
from Recharify.View import SplashScreen
import gettext

# Set up translation
gettext.translation('Recharify', localedir='resources/locale/', languages=['zh_CN'], fallback=True).install()


class App:
    @staticmethod
    def run():
        app = QApplication(sys.argv)
        sp = SplashScreen.SplashScreen()
        sp.show()
        sys.exit(app.exec_())
