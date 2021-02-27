import sys
from PyQt5 import QtWidgets
from PyQt5 import QtCore


class MainWindow(QtWidgets.QMainWindow):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        widget = QtWidgets.QWidget()
        self.setCentralWidget(widget)
        self.show()


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    window = MainWindow()
    app.exec_()