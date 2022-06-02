from PySide2.QtWidgets import QApplication, QMessageBox
from PySide2.QtUiTools import QUiLoader


class Stats:
    def __init__(self):
        self.ui = QUiLoader().load('main.ui')
        self.ui.generate.clicked.connect(lambda: self.but_status(self.ui.generate))

    def but_status(self, btn):
        a = btn.text()
        QMessageBox.warning(self.ui, "信息", a)


app = QApplication([])
stats = Stats()
stats.ui.show()
app.exec_()
