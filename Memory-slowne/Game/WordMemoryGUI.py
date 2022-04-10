import PyQt5.QtWidgets
import PyQt5.QtCore

class WordMemoryGUI(PyQt5.QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__()
        
        self.setGeometry(300, 300, 720, 480)
        self.setWindowTitle("Memory słowne")
    