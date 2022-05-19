from typing import Any

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
        self.playerSelectedWords = []

    def playerWin(self):
        for elem in self.playerSelectedWords:
            if elem not in self.correctAnswers:
                return False
        return True

    def isGameFinished(self):
        pass

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
            if len(self.playerSelectedWords) != 0:
                self.playersDict[self.nickname][1] += 1 #ilość wszystkich gier
                self.playersDict[self.nickname][3] += len(self.playerSelectedWords) #ilość wszystkich odpowiedzi

                if self.playerWin():
                    self.playersDict[self.nickname][0] += 1 #ilość wygranych gier
                
                numberOfCorrectPlayerAnswers = 0
                for elem in self.playerSelectedWords:
                    if elem in self.correctAnswers:
                        numberOfCorrectPlayerAnswers += 1
                self.playersDict[self.nickname][2] += numberOfCorrectPlayerAnswers #ilość poprawnych odpowiedzi

            self.savePlayerStatistics()
            self.allAnswers = random.sample(self.wordsList, self.numberOfAllAnswers) #klikalne odpowiedzi
            self.correctAnswers = random.sample(self.allAnswers, self.numberOfCorrectAnswers) # poprawne odpowiedzi wylosowane

        except Exception:
            return False

        self.playerSelectedWords = []
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

    def getNumberOfCorrectAnswers(self):
        return self.numberOfCorrectAnswers

    def getNumberOfAllAnswers(self):
        return self.numberOfAllAnswers

    # wzór: 5 * 2^(self.numberOfCorrectAnswers // 5)
    def getDurationOfLookingAtCorrectAnswersAsSeconds(self):
        return 5 * pow(2, self.numberOfCorrectAnswers // 5)

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

    def addPlayerAnswer(self, word):
        self.playerSelectedWords.append(word)
    
    def isGameFinished(self):
        return len(self.playerSelectedWords) >= self.numberOfCorrectAnswers
    
    def getPlayerSelectedWords(self):
        return self.playerSelectedWords