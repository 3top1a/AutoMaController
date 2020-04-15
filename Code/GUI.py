from PyQt5 import uic
from PyQt5.QtWidgets import QApplication


def Start():
    Form, Window = uic.loadUiType("GUI.ui")

    app = QApplication([])
    window = Window()
    form = Form()
    form.setupUi(window)

    form.AddAgent.clicked.connect(AddDialogShow)


    window.show()
    app.exec_()


def AddDialogShow():
    Form, Window = uic.loadUiType("add.ui")

    app2 = QApplication([])
    window = Window()
    form = Form()
    form.setupUi(window)
    #form.label.setText("")
    window.show()
    #app2.exec()
