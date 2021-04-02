
from hangman import Hangman






# _hangman.generateHangmanPics()

# for _img in _hangman.hangmanpics:
#
#     print(_img)


import string


def _hangman():
    _hangman = Hangman()
    _rounds = 0
    # print(_hangman.wins)
    # print(_hangman.losses)

    _stop_game = False

    while(not _stop_game or _rounds > 9):
        # getting user input
        _newgame_start = True
        print('Hangman by Hisham\n')
        word = _hangman.getRandomWord()
        print(f'Help !! the word is {word}')

        word_letters = set(word.upper())  # letters in the word
        alphabet = set(string.ascii_uppercase)
        used_letters = set()  # what the user has guessed
        # to store letters that user inputs and is not in the word !!
        missed_letters = ''

        lives = 0

        while len(word_letters) > 0 and lives <7:

            print(f'You have {8-lives} lives left and you have used these letters: ', ' '.join(used_letters))

            word_list = [letter if letter in used_letters else '-' for letter in word.upper()]

            # what current word is (ie W - R D)
            # print('Current word: ', ' '.join(word_list))
            print(' '.join(word_list))

            print('Misses : ', missed_letters.rstrip(','))

            print(_hangman.hangmanpics[lives])
            # print('You have', lives, 'lives left and you have used these letters: ', ' '.join(used_letters))

            user_letter = input('Please enter a single letter: ').upper()

            if user_letter in alphabet - used_letters:
                used_letters.add(user_letter)

                if user_letter in word_letters:
                    word_letters.remove(user_letter)
                    # print('HHHHHHHHHH found a letter !!!!!!!')

                else:
                    lives += 1 # takes away a life if wrong
                    missed_letters += user_letter + ','

            elif user_letter in used_letters:
                print('\nYou have already used that letter. Guess another letter.')

            else:
                print('\nThat is not a valid letter.')

        #==============================================================
        # gets here when len(word_letters) == 0 OR when lives == 0
        if lives == 7:
            print(_hangman.hangmanpics[lives])
            print("Sorry! You've lost. The word was", word)
            _hangman.lose()
            print(f'Wins: {_hangman.wins} Losses: {_hangman.losses}')

        else:
            print("Congratulations! You've found the word", word, "!!")
            _hangman.win()
            print(f'Wins: {_hangman.wins} Losses: {_hangman.losses}')

        # ==============================================================
        # to ask the user if he wants to play again or not
        _play_again = input('\nDo you want to play again? (y or Y) ').lower()

        if(_play_again == 'y' or _play_again =='yes'):
            _rounds+=1

        else:
            _stop_game = True
            print("Press Enter key to exit.\n")


    print(f'You had completed 8 rounds and the final score is {_hangman.wins} wins and {_hangman.losses} losses')

if __name__ == '__main__':

    _hangman()
