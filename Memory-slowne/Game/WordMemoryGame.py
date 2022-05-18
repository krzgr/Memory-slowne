import json
import random

class WordMemoryGame:
    def __init__(self):
        self.difficulty = "easy"
        self.wordsList = []
        self.numberOfCorrectAnswers = 5
        self.numberOfAllAnswers = 3 * self.numberOfCorrectAnswers
        self.playersDict = {}
        self.wordsDict = {}
        self.allAnswers = []
        self.correctAnswers = []

    # funkcje typu load
    def loadWordsFromFile(self):
        try:
            wordsFile = open("data/words.json", "r", encoding="utf-8")
            self.wordsDict = json.loads(wordsFile.read())  # wszystkie słowa wpisane z pliku
        except FileNotFoundError:
            return False
        except Exception:
            wordsFile.close()
            return False
        return True

    def loadPlayersDataFromFile(self):
        try:
            playersFile = open("data/players.json", "r", encoding="utf-8")
            self.playersDict = json.loads(playersFile.read())
        except FileNotFoundError:
            return False
        except Exception:
            playersFile.close()
            return False
        return True

    def setDifficulty(self, diffInput):
        self.difficulty = diffInput
        self.wordsList = self.wordsDict[self.difficulty]
        return None

    def shuffleWords(self):
        try:
            self.allAnswers = random.sample(self.wordsList, self.numberOfAllAnswers) #klikalne odpowiedzi
            self.correctAnswers = random.sample(self.allAnswers, self.numberOfCorrectAnswers) # poprawne odpowiedzi wylosowane
        except Exception:
            return False
        return True


    # funckje typu get
    def getAllAnswers(self):
        return self.allAnswers

    def getCorrectAnswers(self):
        return self.correctAnswers

    def getNickname(self):
        return self.nickname

    def getAllPlayersStatistics(self):
        return [(elem, self.playersDict[elem]) for elem in self.playersDict]

    # funckje z gracz
    def setNickname(self, nicknameInput):
        self.nickname = nicknameInput
        if nicknameInput not in self.playersDict:
            return self.addNewPlayer(nicknameInput)
        return True

    def setNumberOfCorrectAnswers(self, num):
        self.numberOfCorrectAnswers = num
        self.numberOfAllAnswers = 3 * self.numberOfCorrectAnswers

    def addNewPlayer(self, playerNickname):
        self.playersDict[playerNickname] = [0, 0, 0, 0]
        return self.savePlayerStatistics()

    def savePlayerStatistics(self):
        try:
            playersFile = open("data/players.json", "w", encoding="utf-8")
            jsonDict = json.dumps(self.playersDict)
        except FileNotFoundError:
            return False
        except Exception:
            playersFile.close()
            return False
        else:
            playersFile.write(jsonDict)
        return True