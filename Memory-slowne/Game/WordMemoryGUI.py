import PyQt5.QtWidgets
import PyQt5.QtCore
import functools

class WordMemoryGUI(PyQt5.QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__()
        
        self._initUI()
        self.newGame()

    def _initUI(self):
        #Window initialization
        self.setGeometry(0, 0, 1080, 720)
        self.move(self.screen().geometry().center() - self.frameGeometry().center())
        self.setWindowTitle("Memory słowne")

        #Menu bar initialization
        self._addMenuBar()

        self.mainWidget = PyQt5.QtWidgets.QWidget()
        self.mainWidget.setContentsMargins(15, 15, 0, 15)
        self.setCentralWidget(self.mainWidget)

        self.mainGridLayout = PyQt5.QtWidgets.QGridLayout(self.centralWidget())

        #QSpacerItem
        spacerItem1 = PyQt5.QtWidgets.QSpacerItem(40, 20, PyQt5.QtWidgets.QSizePolicy.Minimum, PyQt5.QtWidgets.QSizePolicy.Expanding)
        self.mainGridLayout.addItem(spacerItem1, 1, 2, 1, 1)
        spacerItem2 = PyQt5.QtWidgets.QSpacerItem(40, 20, PyQt5.QtWidgets.QSizePolicy.Minimum, PyQt5.QtWidgets.QSizePolicy.Expanding)
        self.mainGridLayout.addItem(spacerItem2, 1, 0, 1, 1)
        spacerItem3 = PyQt5.QtWidgets.QSpacerItem(20, 40, PyQt5.QtWidgets.QSizePolicy.Minimum, PyQt5.QtWidgets.QSizePolicy.Expanding)
        self.mainGridLayout.addItem(spacerItem3, 2, 1, 1, 1)
        spacerItem4 = PyQt5.QtWidgets.QSpacerItem(20, 40, PyQt5.QtWidgets.QSizePolicy.Minimum, PyQt5.QtWidgets.QSizePolicy.Expanding)
        self.mainGridLayout.addItem(spacerItem4, 0, 1, 1, 1)
        spacerItem5 = PyQt5.QtWidgets.QSpacerItem(15, 20, PyQt5.QtWidgets.QSizePolicy.Minimum, PyQt5.QtWidgets.QSizePolicy.Expanding)
        self.mainGridLayout.addItem(spacerItem5, 1, 4)

        #GameGridLayout
        self.gameGridLayout = PyQt5.QtWidgets.QGridLayout()
        self.gameGridLayout.setSizeConstraint(PyQt5.QtWidgets.QLayout.SetMinimumSize)
        self.gameGridLayout.setSpacing(15)
        self.mainGridLayout.addLayout(self.gameGridLayout, 1, 1, 1, 1)        
        
        #Buttons initialization
        self.buttonList = [PyQt5.QtWidgets.QPushButton("Bratysława {}".format(i), self.centralWidget()) for i in range(0, 30)]

        for i in range(0, len(self.buttonList)):
            self.buttonList[i].clicked.connect(functools.partial(self._onClickButton, i))
            self.buttonList[i].setStyleSheet(
                "QPushButton { font-size: 20px; background-color: #215ccb; color: white; border-radius: 4px; padding: 5px; } QPushButton:hover { color: red; }"
            )
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
        self.exitAction.triggered.connect(self.close)

        self.myStatsAction = PyQt5.QtWidgets.QAction("&Moje", self)
        self.allStatsAction = PyQt5.QtWidgets.QAction("&Wszystkich", self)

        self.helpAction = PyQt5.QtWidgets.QAction("&Pomoc", self)
        self.helpAction.triggered.connect(self._onHelpClicked)
    
    def newGame(self):
        return None

    def _onClickButton(self, btnNum):
        print(btnNum)
    

    def _onHelpClicked(self):
        print("Clicked!")