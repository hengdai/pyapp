from PySide2.QtWidgets import QMessageBox
from PySide2.QtUiTools import QUiLoader
import random


class Window:
    def __init__(self):
        self.ui = QUiLoader().load('ui/rand_decimal.ui')
        self.ui.generate.clicked.connect(lambda: self._exec())

    def _exec(self):
        self.rand_data()

    def rand_data(self):
        min_data = int(self.ui.min.text())
        max_data = int(self.ui.max.text())  # 小数的范围A ~ B
        count = int(self.ui.count.text())
        keep = int(self.ui.keep.text())  # 随机数的精度round(数值，精度)

        rst = []
        for j in range(count):
            temp = random.uniform(min_data, max_data)
            rst.append(str(round(temp, keep)))

        QMessageBox.warning(self.ui, "随即小数结果", "\n".join(rst))
