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
            words_file = open("words.json", "r")
        except FileNotFoundError:
            return False
        except Exception:
            return False
        else:
            try:
                self.words_dict = json.loads(words_file.read())  # wszystkie słowa wpisane z pliku
            except Exception:
                return False
            finally:
                words_file.close()
            return True

    def setNewPlayer(self, player_nickname):
        self.players_dict[player_nickname] = [0, 0, 0, 0]
        self.savePlayerStatistics()
        return None

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

    def setNumberOfAnswears(self, num):
        self.numberOfAllAnswears = num
        return True

    def shuffleWords(self):
        self.all_answears = random.sample(self.words_list, self.numberOfAllAnswears)
        try:
            self.all_answears = random.sample(self.words_list, self.numberOfAllAnswears)
        except Exception:
            return False
        else:
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
        except FileNotFoundError:
            return False
        except Exception:
            return False
        else:
            try:
                json_dict = json.dumps(self.players_dict)
            except Exception:
                return False
            else:
                file.write(json_dict)
            finally:
                file.close()
            return True