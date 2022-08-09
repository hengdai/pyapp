from PySide2.QtWidgets import QMessageBox
from PySide2.QtWidgets import QTextBrowser
from PySide2.QtUiTools import QUiLoader
import random


class Window:
    def __init__(self):
        self.rst_ui = QTextBrowser()
        self.ui = QUiLoader().load('ui/rand_decimal.ui')
        self.ui.generate.clicked.connect(lambda: self._exec())

    def _exec(self):
        self.rand_data()

    def rand_data(self):
        try:
            min_data = float(self.ui.min.text())
            max_data = float(self.ui.max.text())  # 小数的范围A ~ B
            count = int(self.ui.count.text())
            keep = int(self.ui.keep.text())  # 随机数的精度round(数值，精度)
        except Exception as e:
            QMessageBox.warning(self.ui, "信息输入错误", "信息输入错误: " + str(e))
            return

        rst = []
        for j in range(count):
            temp = random.uniform(min_data, max_data)
            rst.append(format(round(temp, keep), "." + str(keep) + "f"))

        self.rst_ui.close()
        self.rst_ui.setWindowTitle("随机数结果")
        self.rst_ui.setText("\n".join(rst))
        self.rst_ui.show()
