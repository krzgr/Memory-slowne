import PyQt5.QtWidgets
import PyQt5.QtCore

class StatisticsDialog(PyQt5.QtWidgets.QDialog):
    def __init__(self):
        super().__init__()

        self._initUI()
    
    def _initUI(self):
        self.setWindowFlags(self.windowFlags() & ~PyQt5.QtCore.Qt.WindowContextHelpButtonHint)
        self.setWindowTitle("Statystiki wszystkich graczy")
        self.setModal(True)

        self.mainHorizontalLayout = PyQt5.QtWidgets.QHBoxLayout(self)

        self.playersScrollArea = PyQt5.QtWidgets.QScrollArea()
        self.scrollAreaGroupBox = PyQt5.QtWidgets.QGroupBox()
        self.scrollAreaLayout = PyQt5.QtWidgets.QVBoxLayout()
        self.scrollAreaGroupBox.setLayout(self.scrollAreaLayout)
        self.playersScrollArea.setWidget(self.scrollAreaGroupBox)
        self.playersScrollArea.setWidgetResizable(True)
        self.mainHorizontalLayout.addWidget(self.playersScrollArea)

        self.playerStatisticsGroupBox = PyQt5.QtWidgets.QGroupBox("Statystyki gracza")
        self.playerStatisticsFormLayout = PyQt5.QtWidgets.QFormLayout()
        self.mainHorizontalLayout.addWidget(self.playerStatisticsGroupBox)

        
    
    def showAllStatistics(self, playersData):
        self.playersScrollArea.show()

        self.show()
    
    def showPlayerStatistics(self, playerData):
        self.playersScrollArea.hide()

        self.show()
