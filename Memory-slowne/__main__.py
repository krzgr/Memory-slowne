import Game.WordMemoryGUI
import PyQt5.QtWidgets
import PyQt5.QtCore
import sys

if __name__ == '__main__':
    app = PyQt5.QtWidgets.QApplication(sys.argv)
    game = Game.WordMemoryGUI.WordMemoryGUI()
    game.show()
    app.exec_()