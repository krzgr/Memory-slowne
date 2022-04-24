import PyQt5.QtWidgets
import PyQt5.QtCore

class WordMemorySettingsDialog(PyQt5.QtWidgets.QDialog):
    def __init__(self):
        super().__init__()

        self._initUI()

        defaultSettings = {"nickname" : "" ,"difficulty" : "easy", "numberOfCorrectAnswers" : 5, "countdown" : False}
        self._setNewSettings(defaultSettings)
        
    def _initUI(self):
        self.setWindowFlags(self.windowFlags() & ~PyQt5.QtCore.Qt.WindowContextHelpButtonHint)
        self.setWindowTitle("Ustawienia")
        self.setModal(True)

        self.mainVerticalLayout = PyQt5.QtWidgets.QVBoxLayout(self)
        self.mainVerticalLayout.setSpacing(15)

        self.formLayout = PyQt5.QtWidgets.QFormLayout()
        self.nicknameLabel = PyQt5.QtWidgets.QLabel("Nick Gracza: ")
        self.nicknameTextInput = PyQt5.QtWidgets.QLineEdit()
        self.formLayout.setWidget(0, PyQt5.QtWidgets.QFormLayout.LabelRole, self.nicknameLabel)
        self.formLayout.setWidget(0, PyQt5.QtWidgets.QFormLayout.FieldRole, self.nicknameTextInput)
        self.mainVerticalLayout.addLayout(self.formLayout)

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
        self.buttonBox.setStandardButtons(PyQt5.QtWidgets.QDialogButtonBox.Cancel | PyQt5.QtWidgets.QDialogButtonBox.Ok)
        self.buttonBox.buttons()[1].setText("Anuluj")
        self.mainVerticalLayout.addWidget(self.buttonBox)

        self.buttonBox.accepted.connect(self._onSettingsAccepted)
        self.buttonBox.rejected.connect(self._onSettingsRejected)
    
    def _onSettingsRejected(self):
        if self.lastSettings["nickname"] == "":
            print("Nie został ustawiony nick")
            #popup
        
        self._setNewSettings(self.lastSettings)
        self.reject()
    
    def _onSettingsAccepted(self):
        self.lastSettings = self._getSettings()
        
        if self.lastSettings["nickname"] == "":
            print("Nie został ustawiony nick")
            #popup
        
        self.accept()

    def _getSettings(self):
        nickname = self.nicknameTextInput.text()

        difficulty = "easy"
        if self.radioButton12.isChecked():
            difficulty = "medium"
        elif self.radioButton13.isChecked():
            difficulty = "hard"

        numberOfCorrectAnswers = 5
        if self.radioButton22.isChecked():
            numberOfCorrectAnswers = 10
        elif self.radioButton23.isChecked():
            numberOfCorrectAnswers = 15
        elif self.radioButton24.isChecked():
            numberOfCorrectAnswers = 20

        countdown = True
        if self.radioButton32.isChecked():
            countdown = False
        
        return {"nickname" : nickname,"difficulty" : difficulty, "numberOfCorrectAnswers" : numberOfCorrectAnswers, "countdown" : countdown}
    
    def _setNewSettings(self, newSettings):
        self.lastSettings = newSettings

        self.nicknameTextInput.setText(newSettings["nickname"])

        self.radioButton11.setChecked(False)
        self.radioButton12.setChecked(False)
        self.radioButton12.setChecked(False)

        if newSettings["difficulty"] == "easy":
            self.radioButton11.setChecked(True)
        elif newSettings["difficulty"] == "medium":
            self.radioButton12.setChecked(True)
        else:
            self.radioButton13.setChecked(True)


        self.radioButton21.setChecked(False)
        self.radioButton22.setChecked(False)
        self.radioButton22.setChecked(False)
        self.radioButton24.setChecked(False)

        if newSettings["numberOfCorrectAnswers"] == 5:
            self.radioButton21.setChecked(True)
        elif newSettings["numberOfCorrectAnswers"] == 10:
            self.radioButton22.setChecked(True)
        elif newSettings["numberOfCorrectAnswers"] == 15:
            self.radioButton23.setChecked(True)
        else:
            self.radioButton24.setChecked(True)


        self.radioButton31.setChecked(False)
        self.radioButton32.setChecked(False)

        if newSettings["countdown"] == True:
            self.radioButton31.setChecked(True)
        else:
            self.radioButton32.setChecked(True)
        