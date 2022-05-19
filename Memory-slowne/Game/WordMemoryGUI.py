from ctypes.wintypes import PINT
import PyQt5.QtWidgets
import PyQt5.QtCore
import functools
import Game.WordMemoryGame
import Game.SettingsDialog
import Game.HelpDialog
import Game.StatisticsDialog

class WordMemoryGUI(PyQt5.QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__()
        self.game = Game.WordMemoryGame.WordMemoryGame()
        self.settingsDialog = Game.SettingsDialog.SettingsDialog()
        self.helpDialog = Game.HelpDialog.HelpDialog()
        self.statisticsDialog = Game.StatisticsDialog.StatisticsDialog()

        self.btnClickableStyleSheet = "QPushButton { font-size: 20px; background-color: #215ccb; color: white; border-radius: 4px; padding: 5px; } QPushButton:hover { color: red; }"
        self.btnNotClickableStyleSheet = "QPushButton { font-size: 20px; background-color: #0e3aa9; color: white; border-radius: 4px; padding: 5px; }"

        self._initUI()

        if self._initGameLogic() == False:
            self.close()
        else:
            self.settingsDialog.show()

    def _initUI(self):
        #Window initialization
        self.setGeometry(0, 0, 1080, 720)
        self.move(self.screen().geometry().center() - self.frameGeometry().center())
        self.setWindowTitle("Memory słowne")

        #Other windows event connection 
        self.settingsDialog.accepted.connect(self._onSettingsDialogAccepted)
        self.settingsDialog.rejected.connect(self._onSettingsDialogRejected)

        #Menu bar initialization
        self._addMenuBar()

        self.mainWidget = PyQt5.QtWidgets.QWidget()
        self.mainWidget.setContentsMargins(15, 15, 0, 15)
        self.setCentralWidget(self.mainWidget)

        self.mainGridLayout = PyQt5.QtWidgets.QGridLayout(self.centralWidget())

        #QSpacerItem
        spacerItem1 = PyQt5.QtWidgets.QSpacerItem(0, 0, PyQt5.QtWidgets.QSizePolicy.Expanding, PyQt5.QtWidgets.QSizePolicy.Maximum)
        self.mainGridLayout.addItem(spacerItem1, 1, 2, 1, 1)
        spacerItem2 = PyQt5.QtWidgets.QSpacerItem(0, 0, PyQt5.QtWidgets.QSizePolicy.Expanding, PyQt5.QtWidgets.QSizePolicy.Maximum)
        self.mainGridLayout.addItem(spacerItem2, 1, 0, 1, 1)
        spacerItem3 = PyQt5.QtWidgets.QSpacerItem(0, 0, PyQt5.QtWidgets.QSizePolicy.Minimum, PyQt5.QtWidgets.QSizePolicy.Expanding)
        self.mainGridLayout.addItem(spacerItem3, 2, 1, 1, 1)
        spacerItem4 = PyQt5.QtWidgets.QSpacerItem(0, 0, PyQt5.QtWidgets.QSizePolicy.Minimum, PyQt5.QtWidgets.QSizePolicy.Expanding)
        self.mainGridLayout.addItem(spacerItem4, 0, 1, 1, 1)
        spacerItem5 = PyQt5.QtWidgets.QSpacerItem(15, 0, PyQt5.QtWidgets.QSizePolicy.Expanding, PyQt5.QtWidgets.QSizePolicy.Minimum)
        self.mainGridLayout.addItem(spacerItem5, 1, 4)

        #GameGridLayout
        self.gameGridLayout = PyQt5.QtWidgets.QGridLayout()
        self.gameGridLayout.setSizeConstraint(PyQt5.QtWidgets.QLayout.SetMinimumSize)
        self.gameGridLayout.setSpacing(15)
        
        for i in range(0, 5):
            self.gameGridLayout.setColumnStretch(i, 1)
            self.gameGridLayout.setRowStretch(i, 1)
        
        for i in range(3):
            self.mainGridLayout.setRowStretch(i, 1)
    
        self.mainGridLayout.addLayout(self.gameGridLayout, 1, 1, 1, 1)
        
        #Buttons initialization
        self.buttonList = [PyQt5.QtWidgets.QPushButton("", self.centralWidget()) for i in range(0, 60)]

        for i in range(0, len(self.buttonList)):
            self.buttonList[i].clicked.connect(functools.partial(self._onClickButton, i))
            self.buttonList[i].setStyleSheet(self.btnClickableStyleSheet)
            self.buttonList[i].setCursor(PyQt5.QtGui.QCursor(PyQt5.QtCore.Qt.PointingHandCursor))
            self.gameGridLayout.addWidget(self.buttonList[i], i // 5, i % 5)

        #Time counter
        self.timeVerticalLayout = PyQt5.QtWidgets.QVBoxLayout()

        spacerItem6 = PyQt5.QtWidgets.QSpacerItem(20, 200, PyQt5.QtWidgets.QSizePolicy.Minimum, PyQt5.QtWidgets.QSizePolicy.Expanding)
        self.timeVerticalLayout.addItem(spacerItem6)

        self.timerLabel1 = PyQt5.QtWidgets.QLabel("Czas:", self.centralWidget())
        self.timerLabel2 = PyQt5.QtWidgets.QLabel("0:00", self.centralWidget())

        #Time counter fonts
        font = PyQt5.QtGui.QFont()
        font.setPointSize(24)
        self.timerLabel1.setFont(font)
        self.timerLabel1.setAlignment(PyQt5.QtCore.Qt.AlignCenter)
        self.timerLabel2.setFont(font)
        self.timerLabel2.setAlignment(PyQt5.QtCore.Qt.AlignCenter)

        self.timerLabel1.setMargin(10)
        self.timerLabel2.setMargin(5)
        
        self.timeVerticalLayout.addWidget(self.timerLabel1)
        self.timeVerticalLayout.addWidget(self.timerLabel2)

        spacerItem7 = PyQt5.QtWidgets.QSpacerItem(20, 200, PyQt5.QtWidgets.QSizePolicy.Minimum, PyQt5.QtWidgets.QSizePolicy.Expanding)
        self.timeVerticalLayout.addItem(spacerItem7)

        self.mainGridLayout.addLayout(self.timeVerticalLayout, 1, 3)

    def _addMenuBar(self):
        menubar = self.menuBar()
        self._createMenuBarActions()
        
        self.gameMenu = PyQt5.QtWidgets.QMenu("&Gra", self)
        self.gameMenu.addAction(self.newGameAction)
        self.gameMenu.addAction(self.settingsAction)
        self.gameMenu.addSeparator()
        self.gameMenu.addAction(self.exitAction)
        menubar.addMenu(self.gameMenu)

        self.statsMenu = PyQt5.QtWidgets.QMenu("&Statystyki", self)
        self.statsMenu.addAction(self.myStatsAction)
        self.statsMenu.addAction(self.allStatsAction)
        menubar.addMenu(self.statsMenu)

        menubar.addAction(self.helpAction)

    def _createMenuBarActions(self):
        self.newGameAction = PyQt5.QtWidgets.QAction("&Nowa Gra", self)
        self.settingsAction = PyQt5.QtWidgets.QAction("&Ustawienia", self)
        self.exitAction = PyQt5.QtWidgets.QAction("&Wyjście", self)
        self.newGameAction.triggered.connect(self.newGame)
        self.exitAction.triggered.connect(self.close)
        self.settingsAction.triggered.connect(self.settingsDialog.show)

        self.myStatsAction = PyQt5.QtWidgets.QAction("&Moje", self)
        self.allStatsAction = PyQt5.QtWidgets.QAction("&Wszystkich", self)
        self.myStatsAction.triggered.connect(self._onMyStatisticsClicked)
        self.allStatsAction.triggered.connect(self._onAllStatisticsClicked)

        self.helpAction = PyQt5.QtWidgets.QAction("&Pomoc", self)
        self.helpAction.triggered.connect(self._onHelpClicked)
    
    def _onHelpClicked(self):
        self.helpDialog.show()

    def _onSettingsDialogAccepted(self):
        settings = self.settingsDialog._getSettings()
        print("Accepted")
        print(settings)
        self.game.setDifficulty(settings["difficulty"])
        self.game.setNickname(settings["nickname"])
        self.game.setNumberOfCorrectAnswers(settings["numberOfCorrectAnswers"])

        if not self.game.shuffleWords():
            self.close()
        else:
            self.newGame()
    
    def _onSettingsDialogRejected(self):
        print("Rejected")
        print(self.settingsDialog._getSettings())
    
    def _onMyStatisticsClicked(self):
        self.statisticsDialog.showPlayerStatistics(self.settingsDialog._getSettings()["nickname"])

    def _onAllStatisticsClicked(self):
        self.statisticsDialog.showAllStatistics()

    def _initGameLogic(self):        
        if self.game.loadWordsFromFile() and self.game.loadPlayersDataFromFile():
            return True
        else:
            return False

    def newGame(self):
        self.game.shuffleWords()
        for i in range(len(self.buttonList)):
            self.buttonList[i].clicked.disconnect() 
            self.buttonList[i].clicked.connect(functools.partial(self._onClickButton, i))
            self.buttonList[i].setStyleSheet(self.btnClickableStyleSheet)
        
        i = 0
        for x in self.game.getAllAnswers():
            self.buttonList[i].setText(self.tr(x))
            self.buttonList[i].show()
            i += 1
        
        print("Correct: ", self.game.getCorrectAnswers())

        buttonListLen = len(self.buttonList)

        while i < buttonListLen:
            self.buttonList[i].hide()
            i += 1

    def _onClickButton(self, btnNum):
        self.buttonList[btnNum].clicked.disconnect() 
        self.buttonList[btnNum].clicked.connect(lambda : None)

        print("Clicked button!")
        self.buttonList[btnNum].setStyleSheet(self.btnNotClickableStyleSheet)

        self.game.addPlayerAnswer(self.buttonList[btnNum].text())
        
        if self.game.isGameFinished():
            if self.game.playerWin():
                print("Wygrana!")
            else:
                print("Przegrana!")
            
            self.newGame()