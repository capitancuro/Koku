from PyQt6.QtWidgets import QMainWindow
from PyQt6.QtGui import QIcon

class MainWindow(QMainWindow):

    def __init__(self):
        super().__init__()
        self.initializeUI()

    def initializeUI(self):
        self.setGeometry(200, 100, 400, 300)
        self.setWindowTitle("Koku")
        self.setWindowIcon(QIcon("source/resources/Koku_Icon.png"))
        self.show()
