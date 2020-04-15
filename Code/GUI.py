from PyQt5 import uic
from PyQt5.QtWidgets import QApplication


def Start():
    Form, Window = uic.loadUiType("GUI.ui")

    app = QApplication([])
    window = Window()
    form = Form()
    form.setupUi(window)
    window.show()
    app.exec_()
