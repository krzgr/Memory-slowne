import json
import random

class WordMemoryGame:
    def __init__(self):
        self.difficulty = "easy"
        self.words_list = []
        self.number_of_correct_answears = 5
        self.numberOfAllAnswears = 3 * self.number_of_correct_answears

    def loadWordsFromFile(self):
        try:
            wordsFile = open("words.json", "r")
            self.words_dict = json.loads(wordsFile.read())  # wszystkie słowa wpisane z pliku
        except FileNotFoundError:
            return False
        except Exception:
            wordsFile.close()
            return False
        return True

    def addNewPlayer(self, player_nickname):
        self.players_dict[player_nickname] = [0, 0, 0, 0]
        return self.savePlayerStatistics()


    def loadPlayersDataFromFile(self):
        try:
            players_file = open("players.json", "r")
        except FileNotFoundError:
            return False
        except Exception:
            return False
        else:
            try:
                self.players_dict = json.loads(players_file.read())
            except Exception:
                return False
            else:
                return True

    def setGameType(self, game_type_input):
        self.game_type = game_type_input
        return None

    def setDifficulty(self, diff_input):
        self.difficulty = diff_input
        self.words_list = self.words_dict[self.difficulty]
        return None

    def shuffleWords(self):
        try:
            self.allAnswears = random.sample(self.words_list, self.numberOfAllAnswears) #klikalne odpowiedzi
            self.correctAnswers = random.sample(self.allAnswears, self.numberOfCorrectAnswers) # poprawne odpowiedzi wylosowane
        except Exception:
            return False
        return True

    def getAllAnswers(self):
        return self.all_answears

    def getCorrectAnswers(self):
        return self.correct_answears

    def getNickname(self):
        return self.nickname

    def getPlayerStatistics(self):
        return self.players_dict[self.nickname]

    def setNickname(self, nickname_input):
        self.nickname = nickname_input
        return None

    def setNumberOfCorrectAnswears(self, num):
        self.numberOfAllAnswears = num
        self.numberOfAllAnswears = 3 * self.number_of_correct_answears

    def savePlayerStatistics(self):
        try:
            file = open("players.json", "w")
            json_dict = json.dumps(self.players_dict)
        except FileNotFoundError:
            return False
        except Exception:
            file.close()
            return False
        return True