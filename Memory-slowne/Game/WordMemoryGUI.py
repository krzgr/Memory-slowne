import PyQt5.QtWidgets
import PyQt5.QtCore

class WordMemoryGUI(PyQt5.QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__()
        
        self.setGeometry(400, 400, 720, 480)
        self.setWindowTitle("Memory słowne")
    