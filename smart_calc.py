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

VWINDOW_SIZE = 80
HWINDOW_SIZE = 250
DISPLAY_HEIGHT = 20
#BUTTON_HEIGHT, BUTTON_WIDTH = 35, 80 
ERROR_MSG = "ERROR"

class calcWindow(QMainWindow):
    # the calc's main window

    def __init__(self):
        super().__init__()
        self.setWindowTitle("smart_calc")
        self.setFixedSize(HWINDOW_SIZE, VWINDOW_SIZE)
        self.generalLayout = QVBoxLayout()
        centralWidget = QWidget(self)
        centralWidget.setLayout(self.generalLayout)
        self.setCentralWidget(centralWidget)
        self.createDisplay()
        self.createButton()

    def createDisplay(self):
        self.display = QLineEdit()
        self.display.setFixedHeight(DISPLAY_HEIGHT)
        self.display.setAlignment(Qt.AlignmentFlag.AlignLeft)
        self.generalLayout.addWidget(self.display)

    def createButton(self):
        self.enterButton = QPushButton("ENTER")
        #self.enterButton.setFixedSize(BUTTON_WIDTH, BUTTON_HEIGHT)
        self.generalLayout.addWidget(self.enterButton)

def main():
    calcApp = QApplication([])
    mainWindow = calcWindow()
    mainWindow.show()
    sys.exit(calcApp.exec())

if __name__ == "__main__":
    main()