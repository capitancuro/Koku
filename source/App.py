import sys
from PyQt6.QtWidgets import QApplication
from gui import MainWindow


if __name__=='__main__':
    app = QApplication(sys.argv)
    main = MainWindow.MainWindow()
    sys.exit(app.exec())
