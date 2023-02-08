import sys

from PyQt6.QtCore import Qt
from PyQt6.QtWidgets import (
    QApplication, 
    QMainWindow, 
    QWidget,
    QLineEdit,
    QPushButton,
    QVBoxLayout
)

HWINDOW_SIZE = 80
VWINDOW_SIZE = 250
DISPLAY_HEIGHT = 20

class calcWindow(QMainWindow):
    # the calc's main window

    def __init__(self):
        super().__init__()
        self.setWindowTitle("smart_calc")
        self.setFixedSize(VWINDOW_SIZE, HWINDOW_SIZE)
        self.generalLayout = QVBoxLayout()
        centralWidget = QWidget(self)
        centralWidget.setLayout(self.generalLayout)
        self.setCentralWidget(centralWidget)
        self.createDisplay()
        

    def createDisplay(self):
        self.display = QLineEdit()
        self.display.setFixedHeight(DISPLAY_HEIGHT)
        self.display.setAlignment(Qt.AlignmentFlag.AlignLeft)
        self.generalLayout.addWidget(self.display)

def main():
    calcApp = QApplication([])
    mainWindow = calcWindow()
    mainWindow.show()
    sys.exit(calcApp.exec())

if __name__ == "__main__":
    main()