import random

class Hangman():
    def __init__(self):
        self.mots = []
        self.hangmanpics=[]
        self.generateListOfWords()
        self.generateHangmanPics()
        self.wins = 0
        self.losses = 0
        self.rounds = 8

    def generateListOfWords(self):
        self.mots.append("Awkward")
        self.mots.append("Bagpipes")
        self.mots.append("Banjo")
        self.mots.append("Bungler")
        self.mots.append("Croquet")
        self.mots.append("Crypt")
        self.mots.append("Dwarves")
        self.mots.append("Fervid")
        self.mots.append("Fishhook")
        self.mots.append("Fjord")
        self.mots.append("Gazebo")
        self.mots.append("Gypsy")
        self.mots.append("Haiku")
        self.mots.append("Haphazard")
        self.mots.append("Hyphen")
        self.mots.append("Ivory")
        self.mots.append("Jazzy")
        self.mots.append("Jiffy")
        self.mots.append("Jinx")
        self.mots.append("Jukebox")
        self.mots.append("Kayak")
        self.mots.append("Kiosk")
        self.mots.append("Klutz")
        self.mots.append("Memento")
        self.mots.append("Mystify")
        self.mots.append("Numbskull")
        self.mots.append("Ostracize")
        self.mots.append("Oxygen")
        self.mots.append("Pajama")
        self.mots.append("Phlegm")
        self.mots.append("Pixel")
        self.mots.append("Polka")
        self.mots.append("Quad")
        self.mots.append("Quip")
        self.mots.append("Rhythmic")
        self.mots.append("Rogue")
        self.mots.append("Sphinx")
        self.mots.append("Squawk")
        self.mots.append("Swivel")
        self.mots.append("Toady")
        self.mots.append("Twelfth")
        self.mots.append("Unzip")
        self.mots.append("Waxy")
        self.mots.append("Wildebeest")
        self.mots.append("Yacht")
        self.mots.append("Zealous")
        self.mots.append("Zigzag")
        self.mots.append("Zippy")
        self.mots.append("Zombie")

    def generateHangmanPics(self):
        self.hangmanpics.append("    +---+\n        |\n        |\n        |\n        |\n=========")
        self.hangmanpics.append("    +---+\n    |   |\n        |\n        |\n        |\n=========")
        self.hangmanpics.append("    +---+\n    |   |\n    o   |\n        |\n        |\n=========")
        self.hangmanpics.append("    +---+\n    |   |\n    o   |\n    |   |\n        |\n=========")
        self.hangmanpics.append("    +---+\n    |   |\n    o   |\n   /|   |\n        |\n=========")
        self.hangmanpics.append("    +---+\n    |   |\n    o   |\n   /|\  |\n        |\n=========")
        self.hangmanpics.append("    +---+\n    |   |\n    o   |\n   /|\  |\n   /    |\n=========")
        self.hangmanpics.append("    +---+\n    |   |\n    o   |\n   /|\  |\n   / \  |\n=========")

    def getRandomWord(self):
        number = random.randint(0, 48)
        return self.mots[number]
    
    def win(self):
        self.wins +=1
    
    def lose(self):
        self.losses += 1