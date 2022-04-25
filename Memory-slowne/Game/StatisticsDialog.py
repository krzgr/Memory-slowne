import PyQt5.QtWidgets
import PyQt5.QtCore

class StatisticsDialog(PyQt5.QtWidgets.QDialog):
    def __init__(self):
        super().__init__()
        self.playersData = []
        
        self._initUI()
    
    def _initUI(self):
        self.setWindowFlags(self.windowFlags() & ~PyQt5.QtCore.Qt.WindowContextHelpButtonHint)
        self.setWindowTitle("Statystiki wszystkich graczy")
        self.setModal(True)

        self.mainHorizontalLayout = PyQt5.QtWidgets.QHBoxLayout(self)

        self.playersListWidget = PyQt5.QtWidgets.QListWidget()
        self.mainHorizontalLayout.addWidget(self.playersListWidget)

        self.playerStatisticsGroupBox = PyQt5.QtWidgets.QGroupBox("Statystyki gracza")
        self.playerStatisticsFormLayout = PyQt5.QtWidgets.QFormLayout()

        self.numberOfGamesLabel = PyQt5.QtWidgets.QLabel("Liczba gier")
        self.numberOfGamesField = PyQt5.QtWidgets.QLabel()
        self.numberOfWinGamesLabel = PyQt5.QtWidgets.QLabel("Liczba wygranych gier")
        self.numberOfWinGamesField = PyQt5.QtWidgets.QLabel()
        self.numberOfAllAnswersLabel = PyQt5.QtWidgets.QLabel("Liczba wszystkich odpowiedzi")
        self.numberOfAllAnswersField = PyQt5.QtWidgets.QLabel()
        self.numberOfCorrectAnswersLabel = PyQt5.QtWidgets.QLabel("Liczba poprawnych odpowiedzi")
        self.numberOfCorrectAnswersField = PyQt5.QtWidgets.QLabel()

        self.playerStatisticsFormLayout.addRow(self.numberOfGamesLabel, self.numberOfGamesField)
        self.playerStatisticsFormLayout.addRow(self.numberOfWinGamesLabel, self.numberOfWinGamesField)
        self.playerStatisticsFormLayout.addRow(self.numberOfAllAnswersLabel, self.numberOfAllAnswersField)
        self.playerStatisticsFormLayout.addRow(self.numberOfCorrectAnswersLabel, self.numberOfCorrectAnswersField)

        self.playerStatisticsGroupBox.setLayout(self.playerStatisticsFormLayout)
        self.mainHorizontalLayout.addWidget(self.playerStatisticsGroupBox)

        self.playersListWidget.itemClicked.connect(self._onItemClicked)
    
    def updatePlayersStatistics(self, playersData):
        self.playersListWidget.clear()
        self.playersData = playersData

        self.playersListWidget.addItems([el[0] for el in self.playersData])
    
    def showAllStatistics(self):
        self.setWindowTitle("Statystiki wszystkich graczy")
        self.playersListWidget.show()
        self.show()
    
    def showPlayerStatistics(self, nickname):
        self.setWindowTitle("Moje statystyki")
        self.playersListWidget.hide()
        resItemList = self.playersListWidget.findItems(nickname, PyQt5.QtCore.Qt.MatchFlag.MatchExactly)

        if len(resItemList) > 0:
            self.playersListWidget.setCurrentItem(resItemList[0])
            self._onItemClicked(resItemList[0])
        
        self.show()

    def _onItemClicked(self, item):
        self.numberOfWinGamesField.clear()
        self.numberOfGamesField.clear()
        self.numberOfCorrectAnswersField.clear()
        self.numberOfAllAnswersField.clear()
        
        for x in self.playersData:
            if x[0] == item.text():
                self.numberOfWinGamesField.setText(str(x[1][0]))
                self.numberOfGamesField.setText(str(x[1][1]))
                self.numberOfCorrectAnswersField.setText(str(x[1][2]))
                self.numberOfAllAnswersField.setText(str(x[1][3]))
                return