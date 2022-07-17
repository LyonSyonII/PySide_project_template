from PySide6.QtWidgets import QMainWindow, QApplication
from PySide6.QtGui import QIcon
from window import Ui_MainWindow


class MainWindow(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)


def main():
    app = QApplication()
    window = MainWindow()

    window.setWindowTitle("Application Title")
    icon = QIcon("assets/icon.svg")
    app.setWindowIcon(icon)

    window.show()
    app.exec()


if __name__ == "__main__":
    main()
