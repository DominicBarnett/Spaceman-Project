import random

def load_word():
    '''
    A function that reads a text file of words and randomly selects one to use as the secret word
        from the list.

    Returns: 
           string: The secret word to be used in the spaceman guessing game
    '''
    f = open('words.txt', 'r')
    words_list = f.readlines()
    f.close()
    
    words_list = words_list[0].split(' ') #comment this line out if you use a words.txt file with each word on a new line
    secret_word = random.choice(words_list)
    return secret_word



secret_word = load_word()
secret_word_length = len(secret_word)

def is_guess_in_word(guess, secret_word_list):
    '''
    A function to check if the guessed letter is in the secret word

    Args:
        guess (list): The letter the player guessed this round
        secret_word (list): The secret word

    Returns:
        bool: True if the guess is in the secret_word, False otherwise

    '''
    #TODO: check if the letter guess is in the secret word
    for letter in secret_word_list:
        if letter == guess:
            return True

    return False





def list_to_string(list):
    str = ""
    for letter in list:
        str += letter
    return str

def add_guessed_letters(guess, guessed_letters_list, secret_word_list):
    for i in range(len(secret_word_list)):
        if secret_word_list[i] == guess:
            guessed_letters_list[i] = guess


def spaceman(secret_word):
    '''
    A function that controls the game of spaceman. Will start spaceman in the command line.

    Args:
      secret_word (string): the secret word to guess.

    '''
    alphabet_list = ["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"]
    secret_word_list = []
    guessed_letters_list = []

    
    for letter in secret_word:
        secret_word_list.append(letter)
        guessed_letters_list.append("_")
    

    game_over = False
    
    print("Welcome to Spaceman!")
    print(f'The secret word contains: {len(secret_word_list)} letters', list_to_string(secret_word_list))
    print("You have 7 incorrect guesses, please enter one letter per round")
    print("-------------------------------------------------------")
    allowed_fails = 7
    
    while game_over == False and allowed_fails > 0:

        #TODO: Ask the player to guess one letter per round and check that it is only one letter
        guess = input("Enter a letter: ")
        
        if len(guess) > 1:
            print("please enter only one letter")
            print("-------------------------------------------------------")
        if guess.isalpha():
            try:
                alphabet_list.remove(guess)
            except ValueError:
                guess = input("Enter a letter: ")
            pass
    
        
        letter_in_word = is_guess_in_word(guess, secret_word_list)
        
        if letter_in_word:
            print("Your guess appears in the word!")
            print(f"Guessed word so far: {list_to_string(guessed_letters_list)} ")
            add_guessed_letters(guess, guessed_letters_list, secret_word_list)
            print(f"These letters haven't been guessed yet: {list_to_string(alphabet_list)}")
            print("-------------------------------------------------------")
        elif secret_word_list == guessed_letters_list:
            print('Congrats You win!!')
            game_over = True
            return game_over
        elif allowed_fails == 0:
            print("Game over, You lose")
        else:
            allowed_fails -= 1  
            print("Sorry your guess was not in the word, try again")
            print(f"You have {allowed_fails} incorrect guesses left")
            print(f"Guessed word so far: {list_to_string(guessed_letters_list)} ")
            print(f"These letters haven't been guessed yet: {list_to_string(alphabet_list)}")
            print("-------------------------------------------------------")

        

            
        #TODO: check if the game has been won or lost



 #TODO: check that guess is only one character


#These function calls that will start the game

spaceman(secret_word)