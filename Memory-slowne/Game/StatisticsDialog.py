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

        #-----------------------------------------
        for i in range(30):
            self.playersListWidget.addItem("Item {}".format(i))
        self.mainHorizontalLayout.addWidget(self.playersListWidget)

        self.playersListWidget.addItem("qwerty")
        #-----------------------------------------

        self.playerStatisticsGroupBox = PyQt5.QtWidgets.QGroupBox("Statystyki gracza")
        self.playerStatisticsFormLayout = PyQt5.QtWidgets.QFormLayout()

        #------------Statystyki gracza------------
        #
        #-----------------------------------------

        self.playerStatisticsGroupBox.setLayout(self.playerStatisticsFormLayout)
        self.mainHorizontalLayout.addWidget(self.playerStatisticsGroupBox)

        self.playersListWidget.itemClicked.connect(self._onItemClicked)
    
    def updatePlayersStatistics(self, playersData):
        self.playersListWidget.clear()
        self.playersData = playersData

        self.playersListWidget.addItems([el[0] for el in self.playersData])
    
    def showAllStatistics(self):
        self.playersListWidget.show()
        


        self.show()
    
    def showPlayerStatistics(self, nickname):
        self.playersListWidget.hide()
        resItemList = self.playersListWidget.findItems(nickname, PyQt5.QtCore.Qt.MatchFlag.MatchExactly)

        if len(resItemList) > 0:
            self.playersListWidget.setCurrentItem(resItemList[0])
    
    def _onItemClicked(self, item):
        print(item.text())