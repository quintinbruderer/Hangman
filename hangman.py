import random

top_english_words = ''
trial_count = 1
letter_history = []
user_word_guess = []
user_letter_guess = ''

head = ' ' # head = 'o'
body = ' ' # body = '|'
right_arm = ' ' # right_arm = '/'
right_leg = ' ' # right_leg = '/'
left_arm = ' ' # left_arm = '\\'
left_leg = ' ' # left_leg = '\\'
#  o
# /|\
#  |
# / \

def print_hangman():
    hangman_character = [
        [' ', '|', '-', '-', '-', '-', '\\', ' ', ' '],
        [' ', head, ' ', ' ', ' ', ' ', ' ', '\\', ' '],
        [right_arm, body, left_arm, ' ', ' ', ' ', ' ', ' ', '|'],
        [' ', body, ' ', ' ', ' ', ' ', ' ', ' ', '|'],
        [right_leg, ' ', left_leg, ' ', ' ', ' ', ' ', ' ', '|'],
        ['_', '_', '_', '_', '_', '_', '_', '_', '|']
    ]
    for row in hangman_character:
        for cell in row:
            print(cell, end='')
        print()

with open('English_20k.txt') as english_no_swears:
    top_english_words = english_no_swears.read()
top_english_words = top_english_words.split() #reads text document, then converts to list

for word in top_english_words[:]:
    if len(word) < 4 or len(word) > 9:
        top_english_words.remove(word) #removes words smaller than 3 letters and larger than 9 from list

random.shuffle(top_english_words)
random_word = top_english_words[random.randint(0, len(top_english_words)-1)].lower()
                                            #shuffles words, then picks a random index
random_word_list = list(random_word) #used for comparing user word guess to random word

for letter in random_word:
    user_word_guess.append('_')

#------------  Game Start  -------------

#print(random_word) debugging purposes
print(
    '\nWelcome to Quinn\'s Python Hangman Game!\n'
)

while trial_count <= 6:
    print_hangman()
    print('\n', ' '.join(user_word_guess), '\n')
    user_letter_guess = input('Enter First Letter: ')[0].lower()

    if user_letter_guess not in letter_history:
        letter_history.append(user_letter_guess)
        if user_letter_guess in random_word:
            for index, letter in enumerate(random_word):
                if user_letter_guess == random_word[index]:
                    user_word_guess[index] = user_letter_guess
            if user_word_guess == random_word_list:
                print("YOU WIN!!!")
                break
        else:
            print('Wrong Guess')
            if trial_count == 1:
                head = 'o'
            elif trial_count == 2:
                body = '|'
            elif trial_count == 3:
                left_leg = '\\'
            elif trial_count == 4:
                right_arm = '/'
            elif trial_count == 5:
                right_leg = '/'
            elif trial_count == 6:
                left_arm = '\\'
            trial_count += 1
    else:
        print('Already Guessed %s. Try again\n' % user_letter_guess, 'Past Guessed Letters', letter_history)

else:
    print("You Lose...", 'The word was %s' % random_word)
    print_hangman()
