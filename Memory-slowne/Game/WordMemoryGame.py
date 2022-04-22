import json
import random

class WordMemoryGame:
    def __init__(self):
        pass

    def loadWordsFromFile(self):
        words_file = open("words.json", "r")
        self.words_dict = json.loads(words_file.read())    #wszystkie słowa wpisane z pliku
        self.words_list = self.words_dict[self.difficulty] #słowa wybrane zależnie od poziomnu trudności
        return None

    def setNewPlayer(self, player_nickname):
        self.players_dict[player_nickname] = [0, 0, 0, 0]
        self.savePlayerStatistics()
        return None

    def loadPlayersDataFromFile(self, player_nickname):
        players_file = open("players.json", "r")
        self.players_dict = json.loads(players_file.read())
        if(player_nickname in self.players_dict):
            self.current_player = self.players_dict[player_nickname]
        else:
            self.setNewPlayer(player_nickname) # ta funkcja bedzie dopisywac nowego gracza, doda sie domyslne staty

    def setGameType(self, game_type_input):
        self.game_type = game_type_input
        return None

    def setDifficulty(self, diff_input):
        self.difficulty = diff_input
        return None

    def shuffleWords(self, words_number):
        return random.sample(self.words_list, words_number)

    def getAllAnswers(self):
        return None

    def getCorrectAnswers(self):
        return None

    def getNickname(self):
        return self.nickname

    def setNickname(self, nickname_input):
        self.nickname = nickname_input
        return None

    def getPlayerStatistics(self):
        return self.current_player

    def savePlayerStatistics(self):
        file = open("players.json", "w")
        json_dict = json.dumps(self.players_dict)
        file.write(json_dict)
        file.close()
        return None