from PyQt5.QtWidgets import QApplication
import MainWindow
import sys


def main():
    app = QApplication(sys.argv)
    window = MainWindow.MainWindow()
    window.show()
    app.exec_()


if __name__ == '__main__':
    main()
