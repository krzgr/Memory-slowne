import PyQt5.QtWidgets
import PyQt5.QtCore

class WordMemoryGUI(PyQt5.QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__()
        
        self.setGeometry(0, 0, 720, 480)
        self.move(self.screen().geometry().center() - self.frameGeometry().center())
        self.setWindowTitle("Memory słowne")
        
        self._addMenuBar()
    
    def _addMenuBar(self):
        menubar = self.menuBar()
        self._createMenuBarActions()
        
        self.gameMenu = PyQt5.QtWidgets.QMenu("&Gra", self)
        self.gameMenu.addAction(self.settingsAction)
        self.gameMenu.addSeparator()
        self.gameMenu.addAction(self.exitAction)
        menubar.addMenu(self.gameMenu)

        self.statsMenu = PyQt5.QtWidgets.QMenu("&Statystyki", self)
        self.statsMenu.addAction(self.myStatsAction)
        self.statsMenu.addAction(self.allStatsAction)
        menubar.addMenu(self.statsMenu)

        self.helpMenu = PyQt5.QtWidgets.QMenu("&Pomoc", self)
        menubar.addMenu(self.helpMenu)


    def _createMenuBarActions(self):
        self.settingsAction = PyQt5.QtWidgets.QAction("&Ustawienia", self)
        self.exitAction = PyQt5.QtWidgets.QAction("&Wyjście", self)
        self.exitAction.triggered.connect(self.close)

        self.myStatsAction = PyQt5.QtWidgets.QAction("&Moje", self)
        self.allStatsAction = PyQt5.QtWidgets.QAction("&Wszystkich", self)