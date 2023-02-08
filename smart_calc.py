import sys

from PyQt6.QtWidgets import QApplication, QMainWindow, QWidget

HWINDOW_SIZE = 80
VWINDOW_SIZE = 250

class calcWindow(QMainWindow):
    # the calc's main window

    def __init__(self):
        super().__init__()
        self.setWindowTitle("smart_calc")
        self.setFixedSize(VWINDOW_SIZE, HWINDOW_SIZE)
        centralWidget = QWidget(self)
        self.setCentralWidget(centralWidget)

def main():
    calcApp = QApplication([])
    mainWindow = calcWindow()
    mainWindow.show()
    sys.exit(calcApp.exec())

if __name__ == "__main__":
    main()