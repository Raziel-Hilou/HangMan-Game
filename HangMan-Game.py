import os


def open_screen():
    HANGMAN_ASCII_ART = """
      _    _                                         
     | |  | |                                        
     | |__| | __ _ _ __   __ _ _ __ ___   __ _ _ __  
     |  __  |/ _` | '_ \ / _` | '_ ` _ \ / _` | '_ \ 
     | |  | | (_| | | | | (_| | | | | | | (_| | | | |
     |_|  |_|\__,_|_| |_|\__, |_| |_| |_|\__,_|_| |_|
                          __/ |                      
                         |___/			Marvel heroes\n"""

    MAX_TRIES = 6

    print(HANGMAN_ASCII_ART, "\nMax tries is: \t", MAX_TRIES)


def choose_word(file_path, index):
    """This function will collect word from chosen file by the user input.
    :parameter file_path: path to file that containing the words.
    :parameter index: chose word by input index 1 to last word.
    :type file_path: str.
    :type index: int.
    :return: return the secret word.
    :rtype: str.
    """

    open_file = open(file_path, "r")
    read_file = open_file.read().lower()
    list_file = read_file.split(" ")
    len_words_in_file = len(list_file)

    if index > len_words_in_file:
        new_index = 0
        print("\nYour index input is out of range, only", len_words_in_file, """words in file.\nYou play now with the first word.\nGood-Luck(:""")

    else:
        new_index = index - 1

    return list_file[new_index]


def check_valid_input(letter_guessed):
    """This function runs tests to see if the received character is valid or invalid.
    :parameter letter_guessed: the received user_input.
    :type letter_guessed: str.
    :return: return 'True' if input is valid , return 'False' if input invalid.
    :rtype: bool.
    """

    if len(letter_guessed) > 1 and not letter_guessed.isalpha():
        print("X")
        return False

    elif len(letter_guessed) > 1:
        print("X")
        return False

    elif not letter_guessed.isalpha():
        print("X")
        return False

    else:
        return True


def try_update_letter_guessed(letter_guessed, old_letters_guessed):
    """This function will update or won't update the list: old_letters_guessed by function 'check_valid_input'.
    :parameter letter_guessed: the received user_input.
    :parameter old_letters_guessed: old letters already received.
    :type letter_guessed: str.
    :type old_letters_guessed: list.
    :return: 'True' if letter_guessed added to old_letters_guessed.
             'False' if letter_guessed won't added to old_letters_guessed.
    :rtype: bool.
    """

    sort_list = sorted(old_letters_guessed)

    if check_valid_input(letter_guessed) is True and letter_guessed not in old_letters_guessed:
        old_letters_guessed.append(letter_guessed)
        return True

    elif check_valid_input(letter_guessed) is True and letter_guessed in old_letters_guessed:
        print("X\n" + "-->".join(sort_list))
        return False


def check_if_the_guess_is_correct(letter_guessed, secret_word):
    """This function will run in code after all check have been made on letter_guessed (user_input).
    :parameter letter_guessed: the received user_input.
    :parameter secret_word: the secret word player need to guess.
    :type letter_guessed: str.
    :type secret_word: str.
    :return: 'True' if letter_guessed in secret_word.
             else: 'False'.
    :rtype: bool.
    """
    if letter_guessed in secret_word:
        return True
    else:
        return False


def check_win(secret_word, old_letters_guessed):
    """This function check if the player has guessed the secret word and won the game.
    :parameter secret_word: The secret word the player has to guess.
    :parameter old_letters_guessed: The list contains the letters the player has guessed so far.
    :type secret_word: str.
    :type old_letters_guessed: list.
    :return The function returns 'True' if all the letters in the secret word are included in the list of letters that the user guessed.
            Otherwise, the function returns 'False'.
    :rtype: bool.
    """

    lst_old_letters = []
    lst_secret_word_1 = list(secret_word)

    for letter in old_letters_guessed:
        if letter in secret_word:
            lst_old_letters.append(letter)
        else:
            pass

    lst_secret_word_2 = []

    for letter in lst_secret_word_1:
        if letter not in lst_secret_word_2:
            lst_secret_word_2.append(letter)

    if len(lst_secret_word_2) == len(lst_old_letters):
        return True
    else:
        pass


def print_hangman(num_of_tries):
    """This function Print one of the man's snapshots
     depends on the number of incorrect guesses made by the player.
     :parameter num_of_tries: The number of incorrect guesses made by the player so far.
     :type num_of_tries: int.
     :return The function return man's snapshots.
     :rtype str.
     """

    HANGMAN_PHOTOS = {
        "picture 1":
        "x-------x",

        "picture 2":
        """x-------x
|
|
|
|
|""",

        "picture 3":
        """x-------x
|       |
|       0
|
|
|""",

        "picture 4":
        """x-------x
|       |
|       0
|       |
|
|""",

        "picture 5":
        """x-------x
|       |
|       0
|      /|\\
|
|""",

        "picture 6":
        """x-------x
|       |
|       0
|      /|\\
|      /
|""",

        "picture 7":
        """x-------x
|       |
|       0
|      /|\\
|      / \\
|"""
}

    if num_of_tries == 1:
        print(HANGMAN_PHOTOS["picture 1"])
        return True

    elif num_of_tries == 2:
        print(HANGMAN_PHOTOS["picture 2"])
        return True

    elif num_of_tries == 3:
        print(HANGMAN_PHOTOS["picture 3"])
        return True

    elif num_of_tries == 4:
        print(HANGMAN_PHOTOS["picture 4"])
        return True

    elif num_of_tries == 5:
        print(HANGMAN_PHOTOS["picture 5"])
        return True

    elif num_of_tries == 6:
        print(HANGMAN_PHOTOS["picture 6"])
        return True

    elif num_of_tries == 7:
        print(HANGMAN_PHOTOS["picture 7"])
        return True

    else:
        return False


def show_hidden_word(secret_word, old_letters_guessed):
    """This function returns a string which consists of letters and underlines.
        The string displays the letters from the old_letters_guessed list that are in the secret_word string,
        (in their appropriate position).
        The rest of the letters in the string (which the player has not yet guessed) as underlines.

    :parameter secret_word: The secret word the player has to guess.
    :parameter old_letters_guessed : The list contains the letters the player has guessed so far.
    :type secret_word: str.
    :type old_letters_guessed: list.
    :return: Letters guessed so far, and the remaining letters(these letters will be replaced by an underline).
    :rtype: str
    """

    hint = ""

    for letter in secret_word:
        if letter in old_letters_guessed:
            hint = hint + letter + " "

        else:
            hint = hint + "_  "

    return hint


def main():
    # Phase 1: Open the game
    open_screen()

    # Phase 2: Chek file path
    while True:
        global FILE_PATH
        FILE_PATH = input("Enter file path:\t")
        try:
            open(FILE_PATH, "r")
        except FileNotFoundError:
            print("\nYour input file path is invalid, please try again\n")
            continue
        else:
            break

    FILE_INDEX = int(input("Enter index:\t"))
    SECRET_WORD = choose_word(FILE_PATH, FILE_INDEX)
    LST_OLD_LETTERS_GUESSED = []
    NUM_OF_TRIES = 1
    print("\nLet's start!\n")
    print_hangman(NUM_OF_TRIES)
    print("\n")
    print(show_hidden_word(SECRET_WORD, LST_OLD_LETTERS_GUESSED))

    # Phase 3: Running the game loop
    while True:

        if check_win(SECRET_WORD, LST_OLD_LETTERS_GUESSED) is True:
            print("\nYou Won!\n")
            break

        else:
            pass

        user_input = input("Guess letter: \t").lower()

        if check_valid_input(user_input) is False:
            print("Your input was invalid, try again")
            continue
        else:
            pass

        if try_update_letter_guessed(user_input, LST_OLD_LETTERS_GUESSED) is False:
            print("your input has already been chosen, try again")
            continue

        else:
            pass

        if check_if_the_guess_is_correct(user_input, SECRET_WORD) is True:
            print("\n")
            print(show_hidden_word(SECRET_WORD, LST_OLD_LETTERS_GUESSED))
            print("\n")
            continue

        else:
            NUM_OF_TRIES += 1
            print("\nWrong answer ):\n")
            print_hangman(NUM_OF_TRIES)
            print(show_hidden_word(SECRET_WORD, LST_OLD_LETTERS_GUESSED))

        if NUM_OF_TRIES == 7:
            print("\nYou Lost ):")
            print("The secret word is: \t", SECRET_WORD)
            break

    # Phase 4: exit or play again
    while True:
        try:
            user_chose_play_or_exit = int(input("\nPlay Again?  \tpress 0:\nexit?       \tpress 1:"))
            if user_chose_play_or_exit == 0:
                os.system("cls")
                main()
                break

            elif user_chose_play_or_exit == 1:
                print("\nGood-Bye (:\n")
                break

            elif user_chose_play_or_exit != 1 or user_chose_play_or_exit != 0:
                print("\nYour input invalid, try again.")
                continue

        except ValueError:
            print("\nYour input invalid, try again.")
            continue


if __name__ == '__main__':
    main()
