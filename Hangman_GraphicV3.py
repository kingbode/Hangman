from hangmangraphic import Hangman

from tkinter import *
import tkinter as tk
import string
from PIL import ImageTk, Image
from tkinter import messagebox

class main():


    def __init__(self):

        def initialize_hangman():
            _tmp_wins = 0
            _tmp_losses = 0

            try:
                if(self.hangman != None):
                    _tmp_wins = self.hangman.wins
                    _tmp_losses = self.hangman.losses
            except:
                pass

            self.hangman = Hangman()
            self.user_letter = ''
            self.to_display_word_list = ''
            self.used_letters = set()
            self.missed_letters = ''
            self.alphabet = set(string.ascii_lowercase)
            self.word = self.hangman.getRandomWord()
            self.word_letters = set(self.word.lower())  # letters in the word
            self.lives = 1
            self.alphabetButtons = string.ascii_uppercase
            self._alphabet_buttons = {}
            self.hangman.wins += _tmp_wins
            self.hangman.losses += _tmp_losses


        initialize_hangman()

        self.screen = Tk()
        self.screen.geometry('320x410')
        self.font_ = 'calibri 13 bold'
        # And Image should be in the same folder where there is script saved
        self.icon_ = PhotoImage(file='hangman.png')
        # Icon set for program window
        self.screen.iconphoto(False, self.icon_)
        self.screen.title('Hangman')
        #How to make a Tkinter window not resizable?
        self.screen.resizable(False, False)


        #======================================================

        # =====================================================
        # your function is here !!!

        def _ch_Button_act(_ch):

            # to update the label with button text !! === Action as what you need !!
            # self.word_list_label.configure(text=self._alphabet_buttons[_ch]['text'])
            # to disable the button
            self._alphabet_buttons[_ch]['state'] = DISABLED
            # update user letter variable..!! global
            self.user_letter = _ch

            # update the word\dashed word !!
            self.word_list = [letter if letter in self.used_letters else '-' for letter in self.word.lower()]

            # what current word is (ie W - R D)
            self.to_display_word_list = ' '.join(self.word_list).lower().capitalize()

            _update_word_letters(self.to_display_word_list)

            # user_letter = will be updated by _ch_Button_act()

            if self.user_letter.lower() in self.alphabet - self.used_letters:
                self.used_letters.add(self.user_letter.lower())

                if self.user_letter.lower() in self.word_letters:
                    self.word_letters.remove(self.user_letter.lower())
                    # _drawImage(self.hangman.hangmanpics[self.lives])
                    # update the word\dashed word !!
                    self.word_list = [letter if letter in self.used_letters else '-' for letter in self.word.lower()]

                    # what current word is (ie W - R D)
                    self.to_display_word_list = ' '.join(self.word_list).lower().capitalize()

                    _update_word_letters(self.to_display_word_list)

                else:
                    _drawImage(self.hangman.hangmanpics[self.lives])
                    self.lives += 1  # add a life if wrong

                # ==============================================================
                # gets here when len(word_letters) == 0 OR when lives == 0
                if self.lives > 8:
                    _final_Result(self.word, False)

                    self.hangman.lose()
                    _update_wins_losses(self.hangman.wins, self.hangman.losses)

                elif(len(self.word_letters)==0):
                    self.word_list = [letter if letter in self.used_letters else '-' for letter in self.word.lower()]
                    _update_word_letters(' '.join(self.word_list).lower().capitalize())
                    _final_Result(self.word, True)
                    self.hangman.win()
                    _update_wins_losses(self.hangman.wins, self.hangman.losses)

        def _draw_alphabet_buttons():

            _chOffset = 8

            for _chOffset in range(4):
                x = 30
                y = 190
                xOffset = 0
                yOffset = _chOffset * 38

                for _ch in self.alphabetButtons[0 + _chOffset * 7:7 + _chOffset * 7]:
                    char_button = tk.Button(self.screen, text=_ch, width=3, font=(self.font_), fg='black',
                                            command=lambda _ch=_ch: _ch_Button_act(_ch))
                    char_button.place(x=x + xOffset, y=y + yOffset)
                    self._alphabet_buttons[_ch] = char_button

                    xOffset += 37

        def _disable_draw_alphabet_buttons():

            for _ch_button in self._alphabet_buttons.keys():
                self._alphabet_buttons[_ch_button]['state'] = DISABLED




        # to update the image !!
        def _drawImage(_image):
            # Creates a Tkinter-compatible photo image, which can be used everywhere Tkinter expects an image object.
            img = ImageTk.PhotoImage(Image.open(_image))
            # The Label widget is a standard Tkinter widget used to display a text or image on the screen.
            self._image_label.configure(image=img)
            self._image_label.image = img


        def _final_Result(_word, _status):
            # Creates a Tkinter-compatible photo image, which can be used everywhere Tkinter expects an image object.
            # _drawImage(_image)
            if (not _status):
                messagebox.showinfo("LOSER!!", f"Sorry! You've lost. The word was {_word}", icon='info')
            else:
                messagebox.showinfo("Winner!!", "Congratulations! You've found the word", icon='info')

            # clear everything !!
            initialize_hangman()
            _draw_alphabet_buttons()
            # update the word\dashed word !!
            self.word_list = [letter if letter in self.used_letters else '-' for letter in self.word.lower()]
            # what current word is (ie W - R D)
            self.to_display_word_list = ' '.join(self.word_list).lower().capitalize()
            _disable_draw_alphabet_buttons()
            _update_word_letters(self.to_display_word_list)
            _updated_testWord(self.word)
            _drawImage(self.hangman.hangmanpics[0])
            _update_wins_losses(self.hangman.wins, self.hangman.losses)




        def _update_word_letters(_word):
            self.word_list_label.configure(text=_word)

        def _update_wins_losses(_wins, _losses):
            self.wins_label.configure(text=f'Wins: {_wins}')
            self.losses_label.configure(text=f'Losses: {_losses}')

        def ExitApplication():

            MsgBox = tk.messagebox.askquestion('Quit?!', 'Are you sure?', icon='question')
            if MsgBox == 'yes':
                self.screen.destroy()
                # exit()

        def newGame():

            MsgBox_ = tk.messagebox.askquestion('New Game', 'Do you want to play another game?', icon='question')
            if MsgBox_ == 'yes':
                pass
                _draw_alphabet_buttons()
            else:
                _disable_draw_alphabet_buttons()

        # =====================================================
        # to help see the word

        def _updated_testWord(_word):
            self.test_label.configure(text=_word)
        # =====================================================


        # to draw/update the buttons
        _draw_alphabet_buttons()
        # =====================================================
        # Initialization
        i = 0

        self.wins_label = tk.Label(self.screen, text=f'Wins: {i}', font=(self.font_), fg='green', anchor="w",justify=LEFT)
        self.wins_label.place(x=85, y=15)

        self.losses_label = tk.Label(self.screen, text=f'Losses: {i}', font=(self.font_), fg='red',anchor="e",justify=RIGHT)
        self.losses_label.place(x=175, y=15)

        self.quit_button = tk.Button(self.screen, text='New Game', width=11, font=(self.font_), fg='green',
                                     command=lambda : newGame())
        self.quit_button.place(x=30, y=350)

        self.newGame_button = tk.Button(self.screen, text='Quit', width=11, font=(self.font_), fg='red', command=ExitApplication)
        self.newGame_button.place(x=140, y=350)

        # =====================================================
        # Creates a Tkinter-compatible photo image, which can be used everywhere Tkinter expects an image object.
        img = ImageTk.PhotoImage(Image.open('hangmanpic0.jpg'))

        # The Label widget is a standard Tkinter widget used to display a text or image on the screen.
        self._image_label = tk.Label(self.screen, image=img, justify=CENTER)
        # The Pack geometry manager packs widgets in rows or columns.
        self._image_label.pack(side="bottom", fill="both", expand="yes")
        self._image_label.place(x=110, y=50)

        self.word_list_label = tk.Label(self.screen, text='', font=(self.font_), fg='green', justify=CENTER)
        self.word_list_label.place(x=125, y=160)

        self.test_label = tk.Label(self.screen, text='', font=(self.font_), fg='blue', )
        self.test_label.place(x=5, y=75)
        # =====================================================

        # =====================================================
        # Game Logic is here

        self.word_list = [letter if letter in self.used_letters else '-' for letter in self.word.lower()]

        # what current word is (ie W - R D)
        self.to_display_word_list = ' '.join(self.word_list).lower().capitalize()

        _update_word_letters(self.to_display_word_list)

        _updated_testWord(self.word)

        # let us do the trick of looping inside hangman function
        self.screen.mainloop()


'''
Main
'''

if __name__ == "__main__":

    main()