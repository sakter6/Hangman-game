import random

# group of random words
words = ['allow', 'audio', 'apple', 'basic', 'brain', 'brown', 'crash', 'civil', 'cream', 'delay', 'draft', 'dozen',
         'equal', 'entry', 'error', 'funny', 'forum', 'frame', 'globe', 'giant', 'green', 'horse', 'human', 'hence',
         'ideal', 'image', 'issue', 'jelly', 'juice', 'joint', 'known', 'logic', 'lucky', 'lying', 'magic', 'movie',
         'minor', 'north', 'nurse', 'never', 'ocean', 'often', 'ought', 'paint', 'power', 'peace', 'queen', 'quick',
         'quiet', 'river', 'reach', 'radio', 'seven', 'scale', 'sugar', 'table', 'total', 'trend', 'upset', 'urban',
         'usage', 'virus', 'value', 'visit', 'world', 'where', 'wrong', 'yield', 'young', 'youth']

# display statement
print("     ***   Hangman   ***")
# picking random word from group of words
word = random.choice(words)
guess = '-----'
wrong_guesses = 0

# loop to replace dash with letter when user enters right letter
while guess != word:
    print(f'secret word: {guess}')
    letter = input("guess a letter: ")
    if letter in word:
        afterguess = ""
        for i in range(len(word)):
            if letter == word[i]:
                afterguess = afterguess + letter
            elif guess[i] != "-":
                afterguess = afterguess + guess[i]
            else:
                afterguess = afterguess + "-"

        guess = afterguess
    # check for wrong guess
    else:
        print("wrong letter, you get a strike!")
        wrong_guesses = wrong_guesses + 1
    # Hangman drawings for wrong guesses
    if wrong_guesses == 1:
        print('''
-----
|    | 
|    
|    
|         
|    
|-----''')
    elif wrong_guesses == 2:
        print('''
-----
|    | 
|    0
|    
|         
|    
|-----''')
    elif wrong_guesses == 3:
        print('''
-----
|    | 
|    0
|    |
|    |     
|    
|-----''')
    elif wrong_guesses == 4:
        print('''
-----
|    | 
|    0
|   /|
|    |     
|    
|-----''')
    elif wrong_guesses == 5:
        print('''
-----
|    | 
|    0
|   /|\\
|    |     
|    
|-----''')
    elif wrong_guesses == 6:
        print('''
-----
|    | 
|    0
|   /|\\
|    |     
|   / 
|-----''')
    elif wrong_guesses == 7:
        print('''
-----
|    | 
|    0
|   /|\\
|    |     
|   / \\
|-----''')

        # check for winner
    if wrong_guesses == 7:
        print("YOU LOST! The secret word was:", word)
        break
    if guess == word:
        print("YOU WIN! The secret word was:", word)
        break
