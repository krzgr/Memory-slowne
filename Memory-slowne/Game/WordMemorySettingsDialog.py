import PyQt5.QtWidgets
import PyQt5.QtCore
import functools
import Game.WordMemoryGUI

class WordMemorySettingsDialog(PyQt5.QtWidgets.QDialog):
    def __init__(self):
        super().__init__()
        self.setModal(True)

        self._initUI()
        
    def _initUI(self):
        self.setWindowFlags(self.windowFlags() & ~PyQt5.QtCore.Qt.WindowContextHelpButtonHint)
        self.setWindowTitle("Ustawienia")
        self.setModal(True)

        self.mainVerticalLayout = PyQt5.QtWidgets.QVBoxLayout(self)
        self.mainVerticalLayout.setSpacing(15)

        self.horizontalLayout = PyQt5.QtWidgets.QHBoxLayout()
        self.mainVerticalLayout.addLayout(self.horizontalLayout)

        self.verticalLayout1 = PyQt5.QtWidgets.QVBoxLayout()
        self.verticalLayout2 = PyQt5.QtWidgets.QVBoxLayout()
        self.verticalLayout3 = PyQt5.QtWidgets.QVBoxLayout()

        self.groupBox1 = PyQt5.QtWidgets.QGroupBox("Poziom trudności")
        self.groupBox2 = PyQt5.QtWidgets.QGroupBox("Ilość słów do zapamiętania")
        self.groupBox3 = PyQt5.QtWidgets.QGroupBox("Gra na czas")

        self.radioButton11 = PyQt5.QtWidgets.QRadioButton("Łatwy")
        self.radioButton12 = PyQt5.QtWidgets.QRadioButton("Średni")
        self.radioButton13 = PyQt5.QtWidgets.QRadioButton("Trudny")

        self.radioButton21 = PyQt5.QtWidgets.QRadioButton("5")
        self.radioButton22 = PyQt5.QtWidgets.QRadioButton("10")
        self.radioButton23 = PyQt5.QtWidgets.QRadioButton("15")
        self.radioButton24 = PyQt5.QtWidgets.QRadioButton("20")

        self.radioButton31 = PyQt5.QtWidgets.QRadioButton("Tak")
        self.radioButton32 = PyQt5.QtWidgets.QRadioButton("Nie")

        self.verticalLayout1.addWidget(self.radioButton11)
        self.verticalLayout1.addWidget(self.radioButton12)
        self.verticalLayout1.addWidget(self.radioButton13)
        self.verticalLayout1.addStretch(1)
        self.groupBox1.setLayout(self.verticalLayout1)
        self.horizontalLayout.addWidget(self.groupBox1)

        self.verticalLayout2.addWidget(self.radioButton21)
        self.verticalLayout2.addWidget(self.radioButton22)
        self.verticalLayout2.addWidget(self.radioButton23)
        self.verticalLayout2.addWidget(self.radioButton24)
        self.verticalLayout2.addStretch(1)
        self.groupBox2.setLayout(self.verticalLayout2)
        self.horizontalLayout.addWidget(self.groupBox2)

        self.verticalLayout3.addWidget(self.radioButton31)
        self.verticalLayout3.addWidget(self.radioButton32)
        self.verticalLayout3.addStretch(1)
        self.groupBox3.setLayout(self.verticalLayout3)
        self.horizontalLayout.addWidget(self.groupBox3)

        self.buttonBox = PyQt5.QtWidgets.QDialogButtonBox()
        self.buttonBox.setStandardButtons(PyQt5.QtWidgets.QDialogButtonBox.Cancel|PyQt5.QtWidgets.QDialogButtonBox.Ok)
        self.mainVerticalLayout.addWidget(self.buttonBox)

        self.buttonBox.accepted.connect(self.accept)
        self.buttonBox.rejected.connect(self.reject)
        
    
    def _getSettings(self):
        return None