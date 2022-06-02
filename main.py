from PySide2.QtWidgets import QApplication
from PySide2.QtUiTools import QUiLoader

import module.rand_decimals.rand_decimals as decimal


def _exec_main(btn):
    a = btn.text()
    decimal_window = decimal.Window()
    decimal_window.ui.show()
    print(a)
    # QMessageBox.warning(self.ui, "信息", a)


class MainWindow:
    def __init__(self):
        self.ui = QUiLoader().load('ui/main.ui')
        self.ui.btn_rand_decimals.clicked.connect(lambda: _exec_main(self.ui.btn_rand_decimals))


if __name__ == "__main__":
    app = QApplication([])
    main_window = MainWindow()
    main_window.ui.show()
    app.exec_()
