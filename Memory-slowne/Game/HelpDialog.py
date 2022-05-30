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
        
        self.helpLabel = PyQt5.QtWidgets.QLabel("Witaj w grze Memory słowne!\nTwoim celem będzie zapamiętanie określonej przez Ciebie ilości słów, a następnie wskazanie ich poprzez kliknęcie na ekranie. Nasz program oferuje kilka poziomów trudności, a także tryb gry na czas. Wszystkie te ustawienia możesz wybrać w oknie ustawień, znajdziesz je w panelu menu w górze otwartego okna. Następnie wybierz opcję nowa gra. Na twoim ekranie pojawią się słowa, które masz za zadanie zapamiętać. Gdy będziesz gotowy, kliknij start, a przed tobą pojawią się słowa spośród których masz wybrać poprawne. Jeśli wybrałeś opcję gry na czas, rozpoczęcie gry nastąpi automatycznie po upływie czasu na zapamiętanie słów.\nPowodzenia!")
        self.helpLabel.setWordWrap(True)
        self.mainVerticalLayout.addWidget(self.helpLabel)
        self.helpLabel.setStyleSheet("QLabel { font-size: 14px; }")
        
        self.buttonBox = PyQt5.QtWidgets.QDialogButtonBox()
        self.buttonBox.setStandardButtons(PyQt5.QtWidgets.QDialogButtonBox.Ok)
        self.mainVerticalLayout.addWidget(self.buttonBox)
        self.buttonBox.clicked.connect(self.close)