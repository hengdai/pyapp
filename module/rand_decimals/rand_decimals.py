from PySide2.QtWidgets import QApplication, QMessageBox
from PySide2.QtUiTools import QUiLoader


class Window:
    def __init__(self):
        self.ui = QUiLoader().load('rand_decimal.ui')
        self.ui.generate.clicked.connect(lambda: self._exec(self.ui.generate))

    def _exec(self, btn):
        a = btn.text()
        QMessageBox.warning(self.ui, "随即小数结果", a)
