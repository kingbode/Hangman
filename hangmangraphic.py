import random






class Hangman():
    def __init__(self):
        self.mots = []
        self.hangmanpics=[]
        self.generateListOfWords()
        self.populateHangmanPics()
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

    def populateHangmanPics(self):
        self.hangmanpics.append("hangmanpic0.jpg")
        self.hangmanpics.append("hangmanpic1.jpg")
        self.hangmanpics.append("hangmanpic2.jpg")
        self.hangmanpics.append("hangmanpic3.jpg")
        self.hangmanpics.append("hangmanpic4.jpg")
        self.hangmanpics.append("hangmanpic5.jpg")
        self.hangmanpics.append("hangmanpic6.jpg")
        self.hangmanpics.append("hangmanpic7.jpg")
        self.hangmanpics.append("hangmanpic8.jpg")

    def getRandomWord(self):
        number = random.randint(0, len(self.mots)-1)
        return self.mots[number]
    
    def win(self):
        self.wins +=1
    
    def lose(self):
        self.losses += 1