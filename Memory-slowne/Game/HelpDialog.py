import PyQt5.QtWidgets
import PyQt5.QtCore

class HelpDialog(PyQt5.QtWidgets.QDialog):
    def __init__(self):
        super().__init__()

        self._initUI()
    
    def _initUI(self):
        self.setWindowFlags(self.windowFlags() & ~PyQt5.QtCore.Qt.WindowContextHelpButtonHint)
        self.setWindowTitle("Pomoc")
        self.setMinimumSize(200, 100)
        
        self.mainVerticalLayout = PyQt5.QtWidgets.QVBoxLayout(self)
        
        self.helpLabel = PyQt5.QtWidgets.QLabel("Pomoc :)")
        self.mainVerticalLayout.addWidget(self.helpLabel)
        
        self.buttonBox = PyQt5.QtWidgets.QDialogButtonBox()
        self.buttonBox.setStandardButtons(PyQt5.QtWidgets.QDialogButtonBox.Ok)
        self.mainVerticalLayout.addWidget(self.buttonBox)
        self.buttonBox.clicked.connect(self.close)