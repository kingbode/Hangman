from hangmangraphic import Hangman

from tkinter import *
import tkinter as tk
import string
from PIL import ImageTk, Image


class main():

    def __init__(self):

        self.screen = Tk()
        self.screen.geometry('320x410')
        self._font = 'calibri 13 bold'
        # And Image should be in the same folder where there is script saved
        self._icon = PhotoImage(file='../hangman.png')
        # Icon set for program window
        self.screen.iconphoto(False,self._icon)
        alphabet = set(string.ascii_lowercase)
        self.alphabetButtons = string.ascii_uppercase

        self._alphabet_buttons = {}


        self.screen.title('Hangman')

        #How to make a Tkinter window not resizable?
        self.screen.resizable(False, False)

        #=====================================================
        # your function is here !!!


        def _ch_Button_act(_ch):
            # to update the label with button text !! === Action as what you need !!
            self.word_list_label.configure(text=self._alphabet_buttons[_ch]['text'])
            # to disable the button
            self._alphabet_buttons[_ch]['state'] = DISABLED


        def _draw_alphabet_buttons():

            _chOffset = 8

            for _chOffset in range(4):
                x = 30
                y = 190
                xOffset = 0
                yOffset = _chOffset * 38

                for _ch in self.alphabetButtons[0+_chOffset*7:7+_chOffset*7]:
                    char_button = tk.Button(self.screen, text=_ch, width=3, font=(self._font), fg='black', command=lambda _ch=_ch : _ch_Button_act(_ch))
                    char_button.place(x=x+xOffset, y=y+yOffset)
                    self._alphabet_buttons[_ch] = char_button


                    xOffset += 37

        def _hangman():
            _hangman = Hangman()
            _rounds = 0

            _stop_game = False

            while (not _stop_game or _rounds > 9):

                _newgame_start = True
                word = _hangman.getRandomWord()
                print(f'Help !! the word is {word}')

                _draw_alphabet_buttons()

                word_letters = set(word.lower())  # letters in the word
                alphabet = set(string.ascii_lowercase)
                used_letters = set()  # what the user has guessed
                # to store letters that user inputs and is not in the word !!
                missed_letters = ''

                lives = 0

                while len(word_letters) > 0 and lives < 8:

                    word_list = [letter if letter in used_letters else '-' for letter in word.lower()]

                    # what current word is (ie W - R D)
                    # print('Current word: ', ' '.join(word_list))
                    _to_display_word_list = ' '.join(word_list).lower().capitalize()

                    print('Misses : ', missed_letters.rstrip(',').lower())

                    user_letter = input('Please enter a single letter: ').lower()

                    if user_letter in alphabet - used_letters:
                        used_letters.add(user_letter)

                        if user_letter in word_letters:
                            word_letters.remove(user_letter)
                            print(_hangman.hangmanpics[lives])

                        else:
                            print(_hangman.hangmanpics[lives])
                            lives += 1  # takes away a life if wrong
                            missed_letters += user_letter + ','


                    elif user_letter in used_letters:
                        print('\nYou have already used that letter. Guess another letter.')

                    else:
                        print('\nThat is not a valid letter.')

                # ==============================================================
                # gets here when len(word_letters) == 0 OR when lives == 0
                if lives == 8:
                    # print(_hangman.hangmanpics[lives])
                    # word_list = [letter if letter in used_letters else '-' for letter in word.lower()]
                    # print(' '.join(word_list).lower())

                    print("Sorry! You've lost. The word was", word)
                    _hangman.lose()
                    print(f'Wins: {_hangman.wins} Losses: {_hangman.losses}')

                else:
                    word_list = [letter if letter in used_letters else '-' for letter in word.lower()]
                    print(' '.join(word_list).lower().capitalize())
                    print("Congratulations! You've found the word", word, "!!")
                    _hangman.win()
                    print(f'Wins: {_hangman.wins} Losses: {_hangman.losses}')

                # ==============================================================
                # to ask the user if he wants to play again or not
                _play_again = input('\nDo you want to play again? (y or Y) ').lower()

                if (_play_again == 'y' or _play_again == 'yes'):
                    _rounds += 1

                else:
                    _stop_game = True
                    print("Press Enter key to exit.\n")



        def _exit():
            exit()

        # =====================================================

        i = 100

        self.wins_label = tk.Label(self.screen,text = f'Wins: {i}',font = (self._font),fg='green',)
        self.wins_label.place(x=45,y=15)

        self.losses_label = tk.Label(self.screen, text=f'Losses: {i}', font=(self._font), fg='red')
        self.losses_label.place(x=155, y=15)

        # =====================================================

        # Creates a Tkinter-compatible photo image, which can be used everywhere Tkinter expects an image object.
        img = ImageTk.PhotoImage(Image.open('../hangmanpic0.jpg'))

        # The Label widget is a standard Tkinter widget used to display a text or image on the screen.
        self._image = tk.Label(self.screen, image=img)
        # The Pack geometry manager packs widgets in rows or columns.
        self._image.pack(side="bottom", fill="both", expand="yes")
        self._image.place(x=95, y=50)

        # =====================================================

        self.word_list_label = tk.Label(self.screen, text='', font=(self._font), fg='green', )
        self.word_list_label.place(x=95, y=160)
        # =====================================================
        _draw_alphabet_buttons()
        # =====================================================
        # Game Logic is here


        # =====================================================
        self.quit_button = tk.Button(self.screen, text='New Game',width=11, font=(self._font),fg='green',command=_exit)
        self.quit_button.place(x=30, y=350)

        self.newGame_button = tk.Button(self.screen, text='Quit', width=11, font=(self._font), fg='red', command=_exit)
        self.newGame_button.place(x=140, y=350)
        # =====================================================
        self.screen.mainloop()



'''
Main
'''

if __name__ == "__main__":
    main()